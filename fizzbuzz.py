# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 20:23:06 2016

@author: Chris

Description: Write a program that prints the numbers from 1 to 100. 
But for multiples of three print "Fizz" instead of the number and 
for the multiples of five print "Buzz". For numbers which are 
multiples of both three and five print "FizzBuzz".
"""

numberRange = range(1,101,1)

for i in numberRange:
    if i%3 == 0 and i%5 == 0:
        print ("FizzBuzz")
    elif i%3 == 0:
        print ("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print (i)