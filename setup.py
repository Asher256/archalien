#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2006-2007, Asher256
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
"""A script to install or uninstall Archalien.

"""

# Imports
import shutil
import sys
import os
from os.path import basename
from getopt import gnu_getopt, GetoptError
from glob import glob

# Global variables
PJ = os.path.join
VERBOSE = False
PREFIX = '/usr'
INSTALLDIR = ''
DESTDIR = PJ(INSTALLDIR, PREFIX)

# All files
FILES = [(PJ('share', 'archalien'), glob(PJ('src', '*.py')))]

# Supplementary dirs
SUPPLDIRS = ['bin']

def postinstall():
    """This function is called after the installation.
    
    """
    if makedirs(PJ(DESTDIR, 'bin')):
        return True
    
    init_py = os.path.realpath(PJ(DESTDIR, 'share', '__init__.py'))
    wrapper = PJ(DESTDIR, 'bin', 'archalien')
    vprint('Creating %s...' % wrapper)
    
    try: 
        fileobj = open(wrapper, 'w', 0755)
    except IOError:
        print 'Cannot open %s for writing (the permission is denied).' % \
              wrapper
        return True
    
    fileobj.write('#!/bin/sh\n' + \
                  'exec /usr/bin/env python \'' + init_py + '\' "$@"')
    fileobj.close()
    return False

def postuninstall():
    """This function is called after an uninstallation.

    """
    if remove(PJ(DESTDIR, 'bin', 'archalien')):
        return True
    return False

def usage():
    """This function is called when the user uses --help.
    
    """
    print __doc__[0:-2]
    print
    print 'Usage: %s [OPTIONS] install|uninstall' \
          % basename(sys.argv[0])
    print
    print "OPTIONS :"
    print "          -p, --prefix          the prefix (default: '/usr')"
    print "          -i, --installdir      installation directory " + \
                                          "(default : '/')"
    print "          -v, --verbose         verbose mode"
    print
    sys.exit(0)

def vprint(string):
    """Print string of --verbose is defined.
    
    """
    if VERBOSE != False:
        print string

def more_informations():
    """Suggest to the user to read the help. 
    
    """
    print "--help for more informations."
    sys.exit(1)

def handle_arguments():
    """Handle all options in the arguments.

    The command is returned (install or uninstall)

    """
    try:
        args = sys.argv[1:]
        optlist = gnu_getopt(args, 'hvp:i:', ['prefix=', 'installdir=', 'help', 'verbose'])
    except GetoptError:
        print 'Error when parsing arguments.'
        more_informations()
    
    if len(optlist[1]) < 1:
        print 'You must enter \'install\' or \'uninstall\' ' + \
              'in the first argument.'
        more_informations()
    elif len(optlist[1]) > 1:
        print 'You must enter only one command : \'install\'' + \
              ' or \'uninstall\'.'
        more_informations()

    for option, value in optlist[0]:
        if option in ['-h', '--help']:
            usage()
        elif option in ['-v', '--verbose']:
            globals()['VERBOSE'] = True
        elif option in ['-p', '--prefix']:
            globals()['PREFIX'] = value;
        elif option in ['-i', '--installdir']:
            globals()['INSTALLDIR'] = value;
    
    globals()['DESTDIR'] = PJ(INSTALLDIR, PREFIX)
    
    return optlist[1][0] # install|uninstall

def makedirs(directory):
    """Make a directory (like os.makedirs). It return True
    on error.

    """
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError:
            print 'I cannot create %s, the permission is denied' % directory
            return True
    elif not os.path.isdir(directory):
        print '%s must be a directory !' % directory
        return True

    return False

def copy(source, destination):
    """Copy a file into another.

    source AND destination must be a file path, not
    a directory path.

    False is returned on error, True else.
    
    """
    vprint('Copying %s into %s.' % (source, destination))

    # create the destination directory
    directory = os.path.dirname(destination)
    if makedirs(directory):
        return True
    
    # test if the source file is exists
    if not os.path.isfile(source):
        print '%s must be a file !' % source
        return True
    
    # copy the file
    try:
        shutil.copyfile(source, destination)
    except IOError:
        print 'I cannot copy %s in %s because the permission is denied.' % \
              (source, destination)
        return True
    
    return False

def remove(filename):
    """Remove a file. True is returned on error.
    
    """
    if os.path.exists(filename):
        vprint('Removing %s' % filename)
        try:
            os.remove(filename)
        except OSError:
            print "Cannot delete %s..." % filename
            return True

    return False

def removedirs():
    """Remove all remain dirs"""
    list = []
    
    for item in FILES:
        directory = PJ(PREFIX, item[0])
        list.append(directory)
    
    list = list + [PJ(DESTDIR, dir) for dir in SUPPLDIRS]
    
    for directory in list:
        if os.path.isdir(directory):
            try:
                os.removedirs(directory)
            except OSError:
                pass

def install():
    """Install all files."""
    for item in FILES:
        dst_file = PJ(DESTDIR, item[0])
        for src_file in item[1]:
            if copy(src_file, PJ(dst_file, basename(src_file))) == True:
                sys.exit(1)
    if postinstall():
        sys.exit(1)

def uninstall():
    """Uninstall all files."""
    for item in FILES:
        dst_dir = PJ(DESTDIR, item[0])
        for src_file in item[1]:
            dst_file = PJ(dst_dir, basename(src_file))
            if remove(dst_file) == True:
                sys.exit(1)
    
    if postuninstall():
        sys.exit(1)

    if removedirs():
        sys.exit(1)

if __name__ == '__main__':
    try:
        command = handle_arguments()
        
        if command == 'install':
            print 'Installation...\n'
            install()
            vprint('')
            print 'All files are installed !'
        if command == 'uninstall':
            print 'Uninstall..\n'
            uninstall()
            print 'Done.'
    except KeyboardInterrupt:
        print "Interrupted."

# vim:ai:et:sw=4:ts=4:sts=4:tw=78:fenc=utf-8
