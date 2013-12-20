#!/usr/bin/env python
# 
# This code was created off Michael DeHaan's ansible-playbook Python
# script, as recommended by his answer on Google Groups about how to 
# call a Playbook from Python.
# See https://groups.google.com/forum/#!topic/ansible-project/V1PoNJcXV_w
# for further details. 
# Original file I worked from: 
# https://github.com/ansible/ansible/blob/devel/bin/ansible
#
##

import sys, os

import ansible.playbook
import ansible.constants as C
from ansible import errors, callbacks, utils
from ansible.color import ANSIBLE_COLOR, stringc
from ansible.callbacks import display
from pkg_resources import resource_string


def colorize(lead, num, color):
    """ Print 'lead' = 'num' in 'color' """
    if num != 0 and ANSIBLE_COLOR and color is not None:
        return "%s%s%-15s" % (stringc(lead, color), stringc("=", color), stringc(str(num), color))
    else:
        return "%s=%-4s" % (lead, str(num))


def hostcolor(host, stats, color=True):
    if ANSIBLE_COLOR and color:
        if stats['failures'] != 0 or stats['unreachable'] != 0:
            return "%-37s" % stringc(host, 'red')
        elif stats['changed'] != 0:
            return "%-37s" % stringc(host, 'yellow')
        else:
            return "%-37s" % stringc(host, 'green')
    return "%-26s" % host


def deploy(args):
    # create parser for CLI options
    parser = utils.base_parser(
        constants=C,
        usage = "%prog playbook.yml",
        connect_opts=True,
        runas_opts=True,
        subset_opts=True,
        check_opts=True,
        diff_opts=True
    )
    options, args = parser.parse_args(args)

    if len(args) == 0:
        parser.print_help(file=sys.stderr)
        return 1

    inventory = ansible.inventory.Inventory(options.inventory)
    inventory.subset(options.subset)
    if len(inventory.list_hosts()) == 0:
        raise errors.AnsibleError("provided hosts list is empty")

    sshpass = None
    sudopass = None
    options.ask_pass = options.ask_pass or C.DEFAULT_ASK_PASS
    if options.connection == "local":
        options.ask_pass = False
    options.ask_sudo_pass = options.ask_sudo_pass or C.DEFAULT_ASK_SUDO_PASS
    (sshpass, sudopass) = utils.ask_passwords(ask_pass=options.ask_pass, 
        ask_sudo_pass=options.ask_sudo_pass)
    options.sudo_user = options.sudo_user or C.DEFAULT_SUDO_USER

    extra_vars={}
   
    playbook = '/home/matt/Envs/t2r/lib/python2.7/site-packages/underwear/django-stack.ym'
    inventory.set_playbook_basedir(os.path.dirname(playbook))
    stats = callbacks.AggregateStats()
    playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
    runner_cb = callbacks.PlaybookRunnerCallbacks(stats, 
        verbose=utils.VERBOSITY)

    pb = ansible.playbook.PlayBook(
        playbook=playbook,
        module_path=options.module_path,
        inventory=inventory,
        forks=options.forks,
        remote_user=options.remote_user,
        remote_pass=sshpass,
        callbacks=playbook_cb,
        runner_callbacks=runner_cb,
        stats=stats,
        timeout=options.timeout,
        transport=options.connection,
        sudo=options.sudo,
        sudo_user=options.sudo_user,
        sudo_pass=sudopass,
        extra_vars=extra_vars,
        private_key_file=options.private_key_file,
        only_tags=[],
        skip_tags=None,
        check=options.check,
        diff=options.diff
    )

    failed_hosts = []
    unreachable_hosts = []

    try:

        pb.run()

        hosts = sorted(pb.stats.processed.keys())
        display(callbacks.banner("PLAY RECAP"))
        playbook_cb.on_stats(pb.stats)

        for h in hosts:
            t = pb.stats.summarize(h)
            if t['failures'] > 0:
                failed_hosts.append(h)
            if t['unreachable'] > 0:
                unreachable_hosts.append(h)

        retries = failed_hosts + unreachable_hosts

        if len(retries) > 0:
            filename = pb.generate_retry_inventory(retries)
            if filename:
                display("           to retry, use: --limit @%s\n" % filename)

        for h in hosts:
            t = pb.stats.summarize(h)

            display("%s : %s %s %s %s" % (
                hostcolor(h, t),
                colorize('ok', t['ok'], 'green'),
                colorize('changed', t['changed'], 'yellow'),
                colorize('unreachable', t['unreachable'], 'red'),
                colorize('failed', t['failures'], 'red')),
                screen_only=True
            )

            display("%s : %s %s %s %s" % (
                hostcolor(h, t, False),
                colorize('ok', t['ok'], None),
                colorize('changed', t['changed'], None),
                colorize('unreachable', t['unreachable'], None),
                colorize('failed', t['failures'], None)),
                log_only=True
            )
        print ""
        if len(failed_hosts) > 0:
            return 2
        if len(unreachable_hosts) > 0:
            return 3

    except errors.AnsibleError, e:
        print e
        display("ERROR: %s" % e, color='red')
        return 1

    return 0


