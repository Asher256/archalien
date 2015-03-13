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
"""Misc functions.

"""

import os
import sys

def command_required(*cmd_list):
    """This function tests if all programs passed in 
    the arguments is available in the enrironment 
    variable 'PATH'.

    """
    path = os.getenv('PATH')
    if path != None:
        path_list = path.split(os.pathsep)
    else:
        print "The environment variable PATH is not defined."
        sys.exit(1)

    for command in cmd_list:
        error = True

        for path in path_list:
            command_path = os.path.join(path, command)
            if os.access(command_path, os.X_OK):
                error = False
                break

        if error:
            print 'The command \'%s\' is not found.' % command
            sys.exit(1)

def fix_input_pkg(input_pkg):
    """Verify and fix the input package path.

    It returns the input package, modified.

    """
    if not os.path.isfile(input_pkg):
        print '\'%s\' doesn\'t exist.' % input_pkg
        sys.exit(1)
    
    if not os.access(input_pkg, os.R_OK):
        print '\'%s\' is not accessible in reading.' % input_pkg

    (input_name, input_ext) = os.path.splitext(input_pkg)

    if input_ext != '.deb':
        print 'The extension of \'%s\' must be *.deb.' % input_pkg
        sys.exit(1)

    # Convert to the absolute path
    input_pkg = os.path.abspath(input_pkg)

    return input_pkg

