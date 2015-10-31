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

import itertools    

def unzip(unzip_list):
    '''
    Unzip [(1, 'a'), (2, 'b'), (3, 'c')] to ([1, 2, 3], ['a', 'b', 'c']).
    
    @param unzip_list: List to unzip.
    @return: Return new unzip list.
    '''
    return tuple(map(list, zip(*unzip_list))) 

def add_in_list(e_list, element):
    '''
    Add element in list, don't add if element has in list.
    
    @param e_list: List to insert.
    @param element: Element will insert to list.
    '''
    if not element in e_list:
        e_list.append(element)
        
def remove_from_list(e_list, element):
    '''
    Try remove element from list, do nothing if element not in list.
    
    @param e_list: List to remove.
    @param element: Element try to remove from list.
    '''
    if element in e_list:
        e_list.remove(element)

def map_value(value_list, get_value_callback):
    '''
    Return value with map list.
    
    @param value_list: A list to loop.
    @param get_value_callback: Callback for element in list.
    @return: Return a new list that every element is result of get_value_callback.
    '''
    if value_list == None:
        return []
    else:
        return map(get_value_callback, value_list)

def mix_list_max(list_a, list_b):
    '''
    Return new list that element is max value between list_a and list_b.

    @param list_a: List a.
    @param list_b: List b.
    @return: Return new list that element is max value between two list.
    
    Return empty list if any input list is empty or two list's length is not same.
    '''
    if list_a == []:
        return list_b
    elif list_b == []:
        return list_a
    elif len(list_a) == len(list_b):
        result = []
        for (index, item_a) in enumerate(list_a):
            if item_a > list_b[index]:
                result.append(item_a)
            else:
                result.append(list_b[index])
        
        return result        
    else:
        print "mix_list_max: two list's length not same."
        return []

def is_true(string_value):
    if isinstance(string_value, bool):
        return string_value
    else:
        try:
            return string_value.lower() == "true"
        except:
            return False

def is_seriate_list(test_list):
    '''
    Whether is seriate list.

    @param test_list: Test list.
    @return: Return True is test list is seriate list.
    '''
    for (index, item) in enumerate(test_list):
        if item != test_list[0] + index:
            return False
    
    return True

def get_disperse_index(disperse_list, value):
    '''
    Get index in disperse list.
    
    @param disperse_list: Disperse list.
    @param value: Match value.
    @return: Return index in disperse list.
    '''
    for (index, _) in enumerate(disperse_list):
        start_value = sum(disperse_list[0:index])
        end_value = sum(disperse_list[0:index + 1])
        if start_value <= value < end_value:
            return (index, value - start_value)
        
    # Return last one.
    return (last_index(disperse_list), disperse_list[-1])

def last_index(test_list):
    '''
    Return last index of list.
    
    @param test_list: Test list.
    @return: Return last index of list.
    '''
    return len(test_list) - 1

def is_long(string):
    '''
    Is string can convert to long type.
    
    @param string: Test string.
    @return: Return True if string can convert to long type.
    '''
    if string == "":
        return True
    
    try:
        long(string)
        return True
    except ValueError:
        return False

def is_int(string):
    '''
    Is string can convert to int type.
    
    @param string: Test string.
    @return: Return True if string can convert to int type.
    '''
    if string == "":
        return True
    
    try:
        int(string)
        return True
    except ValueError:
        return False

def is_float(string):
    '''
    Is string can convert to float type.
    
    @param string: Test string.
    @return: Return True if string can convert to float type.
    '''
    if string == "":
        return True
    
    try:
        float(string)
        return True
    except ValueError:
        return False

def is_hex_color(string):
    '''
    Is string can convert to hex color type.
    
    @param string: Test string.
    @return: Return True if string can convert to hex color type.
    '''
    HEX_CHAR = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                "a", "b", "c", "d", "e", "f",
                "A", "B", "C", "D", "E", "F",
                "#"
                ]
    
    if string == "":
        return True
    else:
        for c in string:
            if not c in HEX_CHAR:
                return False
            
        if string.startswith("#"):
            if len(string) > 7:
                return False
            else:
                return True
        else:            
            if len(string) > 6:
                return False
            else:
                return True    

def split_with(split_list, condition_func):
    pass_list = []
    rest_list = []
    for element in split_list:
        if condition_func(element):
            pass_list.append(element)
        else:
            rest_list.append(element)
            
    return (pass_list, rest_list)

def merge_list(a):
    '''
    Merge recursively list with flat list.
    
    @return: Return a flat list after merge from recursively list.
    '''
    return list(itertools.chain.from_iterable(a))

