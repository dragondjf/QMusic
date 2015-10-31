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

import dbus
import os

def auth_with_policykit(action, 
                        bus_name,
                        object_path,
                        interface_name,
                        interactive=1,
                        ):
    system_bus = dbus.SystemBus()
    obj = system_bus.get_object(bus_name, object_path, interface_name)

    policykit = dbus.Interface(obj, interface_name)
    pid = os.getpid()

    subject = ('unix-process', 
               { 'pid' : dbus.UInt32(pid, variant_level=1),
                 'start-time' : dbus.UInt64(0),
                 }
               )
    details = { '' : '' }
    flags = dbus.UInt32(interactive)
    cancel_id = ''
    (ok, notused, details) = policykit.CheckAuthorization(subject, action, details, flags, cancel_id)

    return ok

def is_dbus_name_exists(dbus_name, request_session_bus=True):
    if request_session_bus:
        bus = dbus.SessionBus()
    else:
        bus = dbus.SystemBus()
    return bus.name_has_owner(dbus_name)

