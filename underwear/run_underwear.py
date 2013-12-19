#!/usr/bin/env python
# 
# This code was created off Michael DeHaan's ansible-playbook Python
# script, as recommended by his answer on Google Groups about how to 
# call a Playbook from Python.
# See https://groups.google.com/forum/#!topic/ansible-project/V1PoNJcXV_w
# for further details. 
# Original file I worked from: 
# https://groups.google.com/forum/#!topic/ansible-project/V1PoNJcXV_w
#
##

import sys

import ansible.playbook
import ansible.constants as C
from ansible import errors, callbacks, utils

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

    print "application deployment hook worked"

