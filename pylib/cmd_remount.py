#!/usr/bin/python
# Copyright (c) TurnKey GNU/Linux - http://www.turnkeylinux.org
#
# This file is part of UserAUFS
#
# UserAUFS is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3 of the License, or (at your
# option) any later version.

"""Remounts a union mount to perform reconfiguration operations

<operation> :=
    ins:<index>:<branch> |
    mod:<branch> |
    append:<branch> |
    prepend:<branch> |
    del:/path/to/branch

<branch> := /path/to/branch[=<permission> [ + <attribute> ]]
    <permission> := rw | ro
    <attribute> := wh | nolwh

See aufs(5) for meaning of remount operations and branch flags.

"""
import sys
import help
import useraufs

from utils import fatal

@help.usage(__doc__)
def usage():
    print >> sys.stderr, "Syntax: %s <mount-path> [<operation> ...]" % sys.argv[0]
    
def main():
    args = sys.argv[1:]
    if len(args) < 1:
        usage()

    mnt = args[0]
    operations = args[1:]

    try:
        useraufs.remount(mnt, operations)
    except useraufs.Error, e:
        fatal(e)
    
if __name__=="__main__":
    main()

