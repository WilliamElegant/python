#!/usr/bin/python
# _*_ coding:utf-8 _*_

""" this is a test of triple-quotes
do you like this world?
yes, I do like it

"""

x = "I have called you thousands times \n , but you don't like to be home."
print x

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a a line."
backslash_cat = "I'm \\ a \\ cat."

print tabby_cat,"\n", persian_cat,"\n", backslash_cat


# while True:
for i in ["/","-","|","\\","|"]:
	print "%r \r" % i
