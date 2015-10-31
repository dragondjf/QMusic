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

import math
import os
import sys
import traceback

def get_parent_dir(filepath, level=1):
    '''
    Get parent directory with given return level.
    
    @param filepath: Filepath.
    @param level: Return level, default is 1
    @return: Return parent directory with given return level. 
    '''
    parent_dir = os.path.realpath(filepath)
    
    while(level > 0):
        parent_dir = os.path.dirname(parent_dir)
        level -= 1
    
    return parent_dir

def get_current_dir(filepath):
    return os.path.dirname(os.path.realpath(filepath))

def write_file(filepath, content, mkdir=False):
    '''
    Write file with given content.

    @param filepath: Target filepath to write.
    @param content: File content to write.
    '''
    if mkdir:
        touch_file_dir(filepath)
    
    f = open(filepath, "w")
    f.write(content)
    f.close()

def read_file(filepath, check_exists=False):
    '''
    Read file content.
    
    @param filepath: Target filepath.
    @param check_exists: Whether check file is exist, default is False.
    
    @return: Return \"\" if check_exists is True and filepath not exist.
    
    Otherwise return file's content.
    '''
    if check_exists and not os.path.exists(filepath):
        return ""
    else:
        r_file = open(filepath, "r")
        content = r_file.read()
        r_file.close()
        
        return content
    
def remove_path(path):
    if os.path.isfile(path):
        remove_file(path)
    elif os.path.isdir(path):
        remove_directory(path)
    else:
        print "%s is not directory or file" % path
    
def remove_file(path):
    '''
    Remove file if file exist.
    
    @param path: Target path to remove.
    '''
    if os.path.exists(path):
        os.remove(path)

def create_directory(directory, remove_first=False):
    '''
    Create directory.
    
    @param directory: Target directory to create.
    @param remove_first: If you want remove directory when directory has exist, set it as True.
    '''
    if remove_first and os.path.exists(directory):
        remove_directory(directory)
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        
def remove_directory(path):
    """
    Remove directory recursively, equivalent to command `rm -rf path`.

    @param path: Target directory to remove.
    """
    if os.path.exists(path):
        for i in os.listdir(path):
            full_path = os.path.join(path, i)
            if os.path.isdir(full_path):
                remove_directory(full_path)
            else:
                os.remove(full_path)
        os.rmdir(path)        

def touch_file_dir(filepath):
    # Create directory first.
    dir = os.path.dirname(filepath)
    if not os.path.exists(dir):
        os.makedirs(dir)

def touch_file(filepath):
    '''
    Touch file, equivalent to command `touch filepath`.
    
    If filepath's parent directory is not exist, this function will create parent directory first.

    @param filepath: Target path to touch.
    '''
    # Create directory first.
    touch_file_dir(filepath)
        
    # Touch file.
    if os.path.exists(filepath):
        os.utime(filepath, None)
    else:
        open(filepath, 'w').close()

def read_first_line(filepath, check_exists=False):
    '''
    Read first line of file.
    
    @param filepath: Target filepath.
    @param check_exists: Whether check file is exist, default is False.
    @return: Return \"\" if check_exists is True and filepath not exist.
    
    Otherwise return file's first line.
    '''
    if check_exists and not os.path.exists(filepath):
        return ""
    else:
        r_file = open(filepath, "r")
        content = r_file.readline().split("\n")[0]
        r_file.close()
        
        return content

def eval_file(filepath, check_exists=False):
    '''
    Eval file content.
    
    @param filepath: Target filepath.
    @param check_exists: Whether check file is exist, default is False.
    @return: Return None if check_exists is True and file not exist.
    
    Return None if occur error when eval file.

    Otherwise return file content as python structure.
    '''
    if check_exists and not os.path.exists(filepath):
        return None
    else:
        try:
            read_file = open(filepath, "r")
            content = eval(read_file.read())
            read_file.close()
            
            return content
        except Exception, e:
            print "function eval_file got error: %s" % e
            traceback.print_exc(file=sys.stdout)
            
            return None

def get_dir_size(dirname):
    '''
    Get size of given directory.
    
    @param dirname: Directory path.
    @return: Return total size of directory.
    '''
    total_size = 0
    for root, dirs, files in os.walk(dirname):
        for filepath in files:
            total_size += os.path.getsize(os.path.join(root, filepath))
            
    return total_size

def format_file_size(bytes, precision=2):
    '''
    Returns a humanized string for a given amount of bytes.
    
    @param bytes: Bytes number to format.
    @param precision: Number precision.
    @return: Return a humanized string for a given amount of bytes.
    '''
    bytes = int(bytes)
    if bytes is 0:
        return '0 B'
    else:
        log = math.floor(math.log(bytes, 1024))
        quotient = 1024 ** log
        size = bytes / quotient
        remainder = bytes % quotient
        if remainder < 10 ** (-precision): 
            prec = 0
        else:
            prec = precision
        return "%.*f %s" % (prec,
                            size,
                            ['B', 'KB', 'MB', 'GB', 'TB','PB', 'EB', 'ZB', 'YB']
                            [int(log)])

def end_with_suffixs(filepath, suffixs):
    '''
    Whether file endswith given suffixs.
    
    @param filepath: Filepath to test.
    @param suffixs: A list suffix to match.
    @return: Return True if filepath endswith with given suffixs.
    '''
    for suffix in suffixs:
        if filepath.endswith(suffix):
            return True
        
    return False    
