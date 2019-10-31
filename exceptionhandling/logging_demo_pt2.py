#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 08:20:40 2019

@author: giudittaparolini
"""

import logging

logging.basicConfig(filename="mylog.log", level=logging.DEBUG)
logging.critical("Critical")
logging.error("Error")
#printed only up to that point
logging.warning("Warning")
logging.info("Info")
logging.debug("Debug")
