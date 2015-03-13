# -*- coding: utf-8 -*-
#
# Copyright (c) Asher256.
#  
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with This program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
"""Functions to handle all arguments.

"""

import sys
import os
from getopt import gnu_getopt, GetoptError

def usage():
    """This function is called when the user uses --help.
    
    """
    print 'Convert a Debian or an RPM Package into an Arch Linux package (' + \
          'and vice-versa).'
    print
    print 'Usage: %s [OPTIONS] debian_package.deb [arch_package.pkg.tar.gz]' \
          % os.path.basename(sys.argv[0])
    print
    print "OPTIONS :"
    print "          -h, --help            Show this help"
    print
    sys.exit(0)

def more_informations():
    """Suggest to the user to read the help. 
    
    """
    print "--help for more informations."
    sys.exit(1)

def handle_arguments():
    """Handle all options in the arguments.

    This function returns a dictionary contain 
    'input_pkg' and 'output_pkg' keywords.
    
    """
    result = {'input_pkg':'', 'output_pkg':''}

    try:
        args = sys.argv[1:]
        optlist = gnu_getopt(args, 'h', ['help'])
    except GetoptError:
        print 'Error when parsing arguments.'
        more_informations()

    if len(sys.argv) < 2:
        print 'No input file.'
        more_informations()

    for option, value in optlist[0]:
        if option in ['-h', '--help']:
            usage()
    
    result['input_pkg'] = optlist[1][0]

    if len(sys.argv) > 3:
        result['output_pkg'] = optlist[1][1]

    return result

# vim:ai:et:sw=4:ts=4:sts=4:tw=78:fenc=utf-8
