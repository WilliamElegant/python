#!/usr/bin/python
# _*_ coding:utf8 _*_

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't know"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

w = 'this is the left of string ...'
e = 'the right of the string'

print w + e

hilarious = True
joke_evaluation = "Is this joke funny? %r" 

print joke_evaluation % hilarious
