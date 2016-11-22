#!/usr/bin/python
# _*_ coding:utf-8 _*_

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type another file name again:"
another_file = raw_input(">")

another_txt = open(another_file)
print  another_txt.read()
