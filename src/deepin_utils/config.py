#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011 Deepin, Inc.
#               2011 Hou Shaohui
#
# Author:     Hou Shaohui <houshao55@gmail.com>
# Maintainer: Hou ShaoHui <houshao55@gmail.com>
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

from ConfigParser import RawConfigParser as ConfigParser
from collections import OrderedDict
from contextlib import contextmanager 
from file import touch_file
import gobject    
import os
import sys
import traceback

class Config(gobject.GObject):
    '''
    Config module to read *.ini file.
    '''
    
    __gsignals__ = {
        "config-changed" : (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE,
                            (gobject.TYPE_STRING, gobject.TYPE_STRING, gobject.TYPE_STRING))
        }
    
    def __init__(self, 
                 config_file, 
                 default_config=None):
        '''
        Init config module.

        @param config_file: Config filepath.
        @param default_config: Default config value use when config file is empty.
        '''
        gobject.GObject.__init__(self)
        self.config_parser = ConfigParser()
        self.remove_option = self.config_parser.remove_option
        self.has_option = self.config_parser.has_option
        self.add_section = self.config_parser.add_section
        self.getboolean = self.config_parser.getboolean
        self.getint = self.config_parser.getint
        self.getfloat = self.config_parser.getfloat
        self.options = self.config_parser.options
        self.items = self.config_parser.items
        self.config_file = config_file
        self.default_config = default_config
        
        # Load default configure.
        self.load_default()
                
    def load_default(self):            
        '''
        Load config items with default setting.
        '''
        # Convert config when config is list format.
        if isinstance(self.default_config, list):
            self.default_config = self.convert_from_list(self.default_config)
            
        if self.default_config:
            for section, items in self.default_config.iteritems():
                self.add_section(section)
                for key, value in items.iteritems():
                    self.config_parser.set(section, key, value)
                
    def load(self):            
        ''' 
        Load config items from the file.
        '''
        self.config_parser.read(self.config_file)
    
    def has_option(self, section, option):
        return self.config_parser.has_option(section, option)
    
    def get(self, section, option, default=None, debug=False):
        ''' 
        Get specified the section for read the option value. 
        
        @param section: Section to index item.
        @param option: Option to index item.
        @param default: Default value if item is not exist.
        @return: Return item value with match in config file.
        '''
        try:
            return self.config_parser.get(section, option)
        except Exception, e:
            if debug:
                print "function get got error: %s" % (e)
                traceback.print_exc(file=sys.stdout)
            
            return default
            
    def set(self, section, option, value, debug=False):  
        '''
        Set item given value.

        @param section: Section to setting.
        @param option: Option to setting.
        @param value: Item value to save.
        '''
        if not self.config_parser.has_section(section):
            if debug:
                print "Section \"%s\" not exist. create..." % (section)
            self.add_section(section)
            
        self.config_parser.set(section, option, value)
        self.emit("config-changed", section, option, value)
        
    def write(self, given_filepath=None):    
        '''
        Save configure to file. 
        
        @param given_filepath: If given_filepath is None, save to default filepath, otherwise save to given filepath.
        '''
        if given_filepath:
            f = file(given_filepath, "w")
        else:
            f = file(self.config_file, "w")
        self.config_parser.write(f)
        f.close()
        
    def get_default(self):    
        '''
        Get default config value.
        
        @return: Return default config value.
        '''
        return self.default_config
    
    def set_default(self, default_config):
        '''
        Set default config value and load it.
        
        @param default_config: Default config value.
        '''
        self.default_config = default_config
        self.load_default()
        
    def convert_from_list(self, config_list):
        '''
        Convert to dict from list format.
        
        @param config_list: Config value as List format.
        @return: Return config value as Dict format.
        '''
        config_dict = OrderedDict()
        for (section, option_list) in config_list:
            option_dict = OrderedDict()
            for (option, value) in option_list:
                option_dict[option] = value
            config_dict[section] = option_dict
        
        return config_dict    
    
    @contextmanager
    def save_config(self, debug=False):
        # Load default config if config file is not exists.
        if not os.path.exists(self.config_file):
            touch_file(self.config_file)
            self.load_default()
        try:  
            # So setting change operations.
            yield  
        except Exception, e:  
            if debug:
                print 'function save_config got error: %s' % e  
                traceback.print_exc(file=sys.stdout)
        else:  
            # Save setting config last.
            self.write()
            
    def get_config(self, selection, option, default=None):
        try:
            return self.get(selection, option, default)
        except:
            return dict(dict(self.default_config)[selection])[option]
        
gobject.type_register(Config)
