#!/usr/bin/python
# _*_ coding: utf-8 _*_

cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_drivern = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "有 ",cars," 可用。"
print "只有 ", drivers," 个司机。"
print "将有 ",cars_not_drivern," 辆车没人开。"
print "我们能运送 ", carpool_capacity, " 名乘客。"
print "我们今天有 ", passengers, " 名乘客。"
print "平均每辆车要搭载 ", average_passengers_per_car, " 名乘客。"
print ""
