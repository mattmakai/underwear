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

import sys, os, stat

import ansible.playbook
import ansible.constants as C
import ansible.utils.template
from ansible import errors, callbacks, utils
from ansible.color import ANSIBLE_COLOR, stringc
from ansible.callbacks import display

import underwear

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
    parser.add_option('-e', '--extra-vars', dest="extra_vars", action="append",
        help="set additional variables as key=value or YAML/JSON", default=[])
    options, args = parser.parse_args(args)

    if len(args) == 0:
        parser.print_help(file=sys.stderr)
        return 1

    inventory = ansible.inventory.Inventory(options.inventory)
    inventory.subset(options.subset)
    print "number of hosts: %s" % str(len(inventory.list_hosts()))
    if len(inventory.list_hosts()) == 0:
        raise errors.AnsibleError("provided hosts list is empty")

    sshpass = None
    sudopass = None
    su_pass = None
    vault_pass = None
    options.ask_pass = options.ask_pass or C.DEFAULT_ASK_PASS
    if options.connection == "local":
        options.ask_pass = False
    options.ask_sudo_pass = options.ask_sudo_pass or C.DEFAULT_ASK_SUDO_PASS
    (sshpass, sudopass, su_pass, vault_pass) = \
        utils.ask_passwords(ask_pass=options.ask_pass, 
        ask_sudo_pass=options.ask_sudo_pass, ask_su_pass=options.ask_su_pass,
        ask_vault_pass=options.ask_vault_pass)
    options.sudo_user = options.sudo_user or C.DEFAULT_SUDO_USER
    options.su_user = options.su_user or C.DEFAULT_SU_USER

    extra_vars={}
    for extra_vars_opt in options.extra_vars:
        if extra_vars_opt.startswith("@"):
            # Argument is a YAML file (JSON is a subset of YAML)
            extra_vars = utils.combine_vars(extra_vars, utils.parse_yaml_from_file(extra_vars_opt[1:]))
        elif extra_vars_opt and extra_vars_opt[0] in '[{':
            # Arguments as YAML
            extra_vars = utils.combine_vars(extra_vars, utils.parse_yaml(extra_vars_opt))
        else:
            # Arguments as Key-value
            extra_vars = utils.combine_vars(extra_vars, utils.parse_kv(extra_vars_opt))

    playbook = underwear.__path__[0] + '/django-stack.yml'
    inventory.set_playbook_basedir(os.path.dirname(playbook))
    stats = callbacks.AggregateStats()
    playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
    runner_cb = callbacks.PlaybookRunnerCallbacks(stats, 
        verbose=utils.VERBOSITY)
    
    if not os.path.exists(playbook):
        raise errors.AnsibleError("the playbook: %s could not be found" % \
            playbook)
        if not (os.path.isfile(playbook) or \
            stat.S_ISFIFO(os.stat(playbook).st_mode)):
            raise errors.AnsibleError( \
                "the playbook: %s does not appear to be a file" % playbook)
   

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
        only_tags=['all',],
        skip_tags=None,
        check=options.check,
        diff=options.diff
    )

    failed_hosts = []
    unreachable_hosts = []

    try:

        pb.run()

        hosts = sorted(pb.stats.processed.keys())
        print hosts
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
        display("ERROR: %s" % e, color='red')
        return 1

    return 0


