#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2011 ~ 2012 Deepin, Inc.
#               2011 ~ 2012 Wang Yong
# 
# Author:     Wang Yong <lazycat.manatee@gmail.com>
# Maintainer: Wang Yong <lazycat.manatee@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import subprocess
import sys
import traceback

def kill_process(proc):
    '''
    Kill process.

    @param proc: Subprocess instance.
    '''
    try:
        if proc != None:
            proc.kill()
    except Exception, e:
        print "function kill_process got error: %s" % (e)
        traceback.print_exc(file=sys.stdout)

def get_command_output_first_line(commands, in_shell=False):
    '''
    Run command and return first line of output.
    
    @param commands: Input commands.
    @return: Return first line of command output.
    '''
    process = subprocess.Popen(commands, stdout=subprocess.PIPE, shell=in_shell)
    process.wait()
    return process.stdout.readline()

def get_command_output(commands, in_shell=False):
    '''
    Run command and return output.
    
    @param commands: Input commands.
    @return: Return command output.
    '''
    process = subprocess.Popen(commands, stdout=subprocess.PIPE, shell=in_shell)
    process.wait()
    return process.stdout.readlines()

def run_command(command):
    '''
    Run command silencely.
    
    @param command: Input command.
    '''
    subprocess.Popen("nohup %s > /dev/null 2>&1" % (command), shell=True)
