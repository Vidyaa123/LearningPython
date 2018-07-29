# '''
# A Few Things to Try Full name greeting. Write a program that asks for a
# person’s first name, then middle, and then last. Finally, it should greet the
# person using their full name.
# '''
# #Enter your Name

# First_Name = input("Enter your First name:")
# Middle_Name = input("Enter your Middle name if you have one:")
# Last_Name = input("Enter your Last  name:")

# print ("Hello" + " " + First_Name + " " + Middle_Name + " " + Last_Name)

# '''
# Bigger, better favorite number. Write a program that asks for a person’s
# favorite number. Have your program add 1 to the number, and then suggest the
# result as a bigger and better favorite number. (Do be tactful about it,
# though.)
# '''


# Fav_No = input("Please Enter your favorite Number:")

# Add_No = int(Fav_No)+ 1
# print(Add_No)


# Angry boss. Write an angry boss program that rudely asks what you want.
# Whatever you answer, the angry boss should yell it back to you and then fire
# you. For example, if you type in I want a raise, it should yell back like
# this: WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!! 


# a = input("What do u want:")
# print("WHADDAYA MEAN " + a + "?!? YOU'RE FIRED!!")

# Table of contents.
# Here’s something for you to do in order to play around more with center,
# ljust, and rjust: write a program that will display a table of contents so
# that it looks like this: Table of Contents

# Chapter 1: Getting Started page 1 Chapter 2: Numbers page 9 Chapter 3: Letters
# page 13
chapter = ['Chapter 1', 'Chapter 2', 'Chapter 3', 'Chapter 4', 'Chapter 5']
title = ['Getting Started', 'Basic Python', 'Advanced Python', 'NLTK', 'Data Analaysis']
page = ['page 1', 'page 10', ' page 50', 'page 120','page 210']

for i  in range(0,len(chapter)):
	print(chapter[i].ljust(15),end="")
	print(title[i].center(30),end="")
	print(page[i].rjust(10))
	print()


# pow(base, power)
# 365%7
# abs(-7)
import math
print("Power :", pow(2,10))
print("Modulus :", 365%7)
print("Absolute value :",abs(-7))
#### Random Numbers - Optional

# Research how to generate a random number with Python.

# Then try to generate your random Civilization III world by generating a land 'X' tile or a water 'o' tile randomly:
# import random
# random.random(10,10)
# - oooXXXoo
# - oooXoXoo
# - XXXooXoo

import random
import numpy as np
tile = ['X','o']
print(np.random.choice(tile,size = (10,10)))
#print (''.join(civili))

	


