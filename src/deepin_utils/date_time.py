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

import time
import traceback
import sys
from contextlib import contextmanager 

def get_current_time(time_format="%Y-%m-%d %H:%M:%S"):
    '''
    Get current time with given time format.

    @param time_format: Time format, default is %Y-%m-%d %H:%M:%S
    @return: Return current time with given time format.
    '''
    return time.strftime(time_format, time.localtime())

def print_exec_time(func):
    '''
    Print execute time of function.
    
    @param func: Fucntion name.
    
    Usage:
    
    >>> @print_exec_time
    >>> def function_to_test():
    >>>     ...
    '''
    def wrap(*a, **kw):
        start_time = time.time()
        ret = func(*a, **kw)
        print "%s time: %s" % (str(func), time.time() - start_time)
        return ret
    return wrap

@contextmanager
def exec_time():
    '''
    Print execute time with given code block.
    
    Usage:

    >>> with exec_time():
    >>>     # Write any code at here.
    >>>     # ...
    '''
    start_time = time.time()
    try:  
        yield  
    except Exception, e:  
        print 'function exec_time got error %s' % e  
        traceback.print_exc(file=sys.stdout)
    else:  
        print "time: %f" % (time.time() - start_time)

