#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 16:01:17 2018

@author: Vidyaa
"""

import random
from six.moves import input
import numpy 
import math

# =============================================================================
# “99 Bottles of Beer on the Wall.” Write a program that prints out the lyrics to that beloved classic, “99 Bottles of Beer on the Wall.”
# 
# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down and pass it around, 98 bottles of beer on the wall.
# 
# 98 bottles of beer on the wall, 98 bottles of beer.
# Take one down and pass it around, 97 bottles of beer on the wall.
# 
# 97 bottles of beer on the wall, 97 bottles of beer.
# Take one down and pass it around, 96 bottles of beer on the wall.
# ........
# 
# 2 bottles of beer on the wall, 2 bottles of beer.
# Take one down and pass it around, 1 bottle of beer on the wall.
# 
# 1 bottle of beer on the wall, 1 bottle of beer.
# Take one down and pass it around, no more bottles of beer on the wall.
# 
# No more bottles of beer on the wall, no more bottles of beer. 
# Go to the store and buy some more, 99 bottles of beer on the wall.
# =============================================================================

i = 99
while i > 1:
     print(str(i) + " bottles of beer on the wall, " +str(i) + " bottles of beer.")
     i -= 1
     if i > 1:
         print("Take one down and pass it around, " + str(i) + " bottles of beer on the wall.")
     else:
         print("Take one down and pass it around, " + str(i) + " bottle of beer on the wall.")
     print("\n")
     
print("1 bottle of beer on the wall, 1 bottle of beer.") 
print("Take one down and pass it around, no more bottle of beer on the wall.")
print("\n")
print("No more bottles of beer on the wall, no more bottles of beer. ")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")

#####Deaf grandma ########

# =============================================================================
# Deaf grandma. Whatever you say to Grandma (whatever you type in), she should respond with this: HUH?! SPEAK UP, GIRL! unless you shout it (type in all capitals). If you shout, she can hear you (or at least she thinks so) and yells back:
# Deaf grandma extended. What if Grandma doesn’t want you to leave? When you shout BYE, she could pretend not to hear you. Change your previous program so that you have to shout BYE three times in a row. Make sure to test your program: if you shout BYE three times but not in a row, you should still be talking to Grandma.
# =============================================================================

say = ""
count = 0
while count < 3:
    say  = input("Say Something to Grandma :")
    if say.isupper():
        print("NO, NOT SINCE " +  str(random.choice(range(1930, 1950))) +"!")
        if say == 'BYE':
            count += 1
        else:
            count = 0
    else:
        print("UH?! SPEAK UP, GIRL!")
   
        
print("Bye Bye GRANDMA!")   

# =============================================================================
# Leap years. Write a program that asks for a starting year and an ending year and then puts all the leap years between them (and including them, if they are also leap years). Leap years are years divisible by 4 (like 1984 and 2004). However, years divisible by 100 are not leap years (such as 1800 and 1900) unless they are also divisible by 400 (such as 1600 and 2000, which were in fact leap years). What a mess!
# =============================================================================

start_year = int(input("Enter Starting year: "))
end_year = int(input("Enter Ending year: "))
for year in  range(start_year-1, end_year):
   if year%4 == 0:
       if (year%100!=0):
           print(year)
       elif (year%100 == 0 and year%400 == 0):
           print (year)
           
   
     
# =============================================================================
# Building and sorting an array. Write the program that asks us to type as many words as we want (one word per line, continuing until we just press Enter on an empty line) and then repeats the words back to us in alphabetical order. Make sure to test your program thoroughly; for example, does hitting Enter on an empty line always exit your program? Even on the first line? And the second?
# Hint: There’s a lovely array method that will give you a sorted version of an array: sorted(). Use it!        
# =============================================================================

arr = []
words = " "
while words != '':
   words = input("Enter a word:")
   arr.append(words)
arr.pop ()
arr.sort()
print(arr)
 
# =============================================================================
# Table of contents. Write a table of contents program here. Start the program with a list holding all of the information for your table of contents (chapter names, page numbers, and so on). Then print out the information from the list in a beautifully formatted table of contents. Use string formatting such as left align, right align, cente 
# =============================================================================
chapter = ['Chapter 1', 'Chapter 2', 'Chapter 3', 'Chapter 4', 'Chapter 5']
title = ['Getting Started', 'Basic Python', 'Advanced Python', 'NLTK', 'Data Analaysis']
page = ['page 1', 'page 10', ' page 50', 'page 120','page 210']

for i  in range(0,len(chapter)):
	print(chapter[i].ljust(15),end="")
	print(title[i].center(30),end="")
	print(page[i].rjust(10))
	print()


# =============================================================================
# Write a function that prints out "moo" n times.
# =============================================================================

#n=input("Number of times to print moo:")

def moo(n):
    return "moo" * n
for i in range(0,5):
    print(moo(i))
#moo(n)   
    
# =============================================================================
# Old-school Roman numerals. In the early days of Roman numerals, the Romans didn’t bother with any of this new-fangled subtraction “IX” nonsense.
# No Mylady, it was straight addition, biggest to littlest—so 9 was written “VIIII,” and so on.
# 

# Write a method that when passed an integer between 1 and 3000 (or so) returns a string containing the proper old-school Roman numeral. In other words, old_roman_numeral 4 should return 'IIII'. Make sure to test your method on a bunch of different numbers.
# 
# =============================================================================
# For reference, these are the values of the letters used: I = 1 V = 5 X = 10
# L = 50 C = 100 D = 500 M = 1000

# =============================================================================
# Hint: Use the integer division and modulus methods.
# =============================================================================


nos = input("Enter number:")
no = int(nos)
number = [1000,500,100,50,10,5,1]
roman_number = ['M','D','C','L','X','V','I']
roman = ""
counter = 0
while no < 3000 and  no != 0:
    
    for i in number:
        quo = math.floor(no/i)
        rem = no%i
        roman = roman + roman_number[counter] * quo
        counter += 1
        no = rem
        if counter > 6:
            exit
print("Old Roman Numeral:", roman)

# =============================================================================
# “Modern” Roman numerals. Eventually, someone thought it would be terribly clever if putting a smaller number before a larger one meant you had to subtract the smaller one. As a result of this development, you must now suffer. Rewrite your previous method to return the new-style Roman numerals so when someone calls roman_numeral 4, it should return 'IV', 90 should be 'XC' etc.
# =============================================================================


nos = input("Enter number:")
no = int(nos)
number = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
roman_number = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
roman = ""
counter = 0
while no < 3000 and  no != 0:
    for i in number:
        quo = math.floor(no/i)
        rem = no%i
        roman = roman + roman_number[counter] * quo
        counter += 1
        no = rem
        if counter > 6:
            exit
print("Modern Roman Numeral:", roman)
