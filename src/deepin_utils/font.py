#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2011 ~ 2013 Deepin, Inc.
#               2011 ~ 2013 Wang Yong
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

import pangocairo

def font_name_just_contain_english(font_name):
    for font_char in font_name.decode('utf-8'):
        if not (
                # Is is english char?
                (font_char >= u'\u0041' and font_char <=u'\u005a') or (font_char >= u'\u0061' and font_char <=u'\u007a')
                # Is is space char?
                or font_char == ' '
                # Is is number char?
                or (font_char >= u'\u0030' and font_char <=u'\u0039')):
            return False
    return True

def get_font_families(filter_terminal_font=False):
    '''Get all font families in system.'''
    fontmap = pangocairo.cairo_font_map_get_default()
    font_families = fontmap.list_families()
    if filter_terminal_font:
        font_families = filter(lambda f:
                               f.is_monospace()
                               or f.get_name() == "文泉驿等宽微米黑",
                               filter(lambda f:
                                      not f.get_name() in ["Droid Sans Japanese", "MT Extra", "Monospace"],
                                      font_families))
    return sorted(map(lambda f: f.get_name(), font_families))

