#!/usr/bin/python
# _*_ coding:utf-8 _*_

from sys import argv
script = argv

print "Script %s is going to create a new file." % script

new_file_name = raw_input("Please set the file name:")
new_file = open(new_file_name,'w') 

line1 = raw_input("input the line 1:")
line2 = raw_input("input the line 2:")
line3 = raw_input("input the line 3:")

new_file.write(line1)
new_file.write(line2)
new_file.write(line3)

#print "you have input:"
#print new_file.read()

new_file.close()

print "over!"
