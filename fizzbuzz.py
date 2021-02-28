#!/usr/bin/env python

def showTime(startElement,endElement):
    for x in xrange(startElement,endElement):
        if x % 5 == 0 and x % 3 == 0:
            print "FizzBuzz"
        elif(x % 5 == 0):
            print "Fizz"
        elif(x % 3 == 0):
            print "Buzz"
        else:
            print x

showTime(1,101)
