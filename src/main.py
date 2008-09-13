#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Just-in-time development for Python - develop your application on-the-fly

code created by Albert Zeyer <ich@az2000.de>, 2008-11-09
code under GPL
"""

import sys
import time



x = 1
while True:
	time.sleep(1)
	x = x + 1
	
	sys.stdout.write("Hallo, x = ")
	sys.stdout.write(str(x))
	sys.stdout.write("\n")
	sys.stdout.flush()
	
