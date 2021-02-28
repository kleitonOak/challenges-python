#!/usr/bin/env python
def fibonacci(startElement,endElement):
    a, b = 0, 1
    for x in xrange(startElement,endElement):
        print a
        a, b = b, a + b

fibonacci(0,10)
print "==================="

def fibonacciGenerator(endElement):
    a, b = 0, 1
    for i in xrange(endElement):
        yield "{}: {}".format(i+1, a)
        a, b = b, a + b

for item in fibonacciGenerator(10):
    print item
