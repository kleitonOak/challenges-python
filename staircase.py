#!/usr/bin/env python

def stairCase(sizestair):
	first = "#"
	shit = first
	for x in xrange(sizestair):
		if(x > 0):
			shit += first
		print shit.rjust(sizestair)	
	
stairCase(4)