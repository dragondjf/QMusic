#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import json
from PyQt5.QtCore import qVersion

applicationName = 'QMusic'
applicationVersion = '3.0.0'
organizationDomain = 'dragondjf.github.io'
organizationName = "dragondjf"
windowIcon = os.sep.join(['skin', 'images', 'QMusic.png'])
windowTitle = u'QMusic'

if qVersion().startswith('5.3'):
    isWebengineUsed = False
else:
    isWebengineUsed = True
