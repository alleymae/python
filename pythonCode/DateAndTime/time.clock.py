#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import time

def procedure():
	time.sleep(2.5)

#measure process time
t0 = time.clock()
procedure()
t1 = time.clock()
print t0, t1
print t1 - t0, "seconds process time"

#measure wall time
t0 = time.time()
procedure()
print time.time() - t0, "seconds wall time"
