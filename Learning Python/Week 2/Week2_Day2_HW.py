#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 10:24:38 2018

@author: Vidyaa
"""

# There is something small that needs fixing. Can you spot it and fix it? (Hint, we only want A-Z and a-z)

for i in range(65,65+26*2+6):
	if ord(chr(i)) <= 90 or ord(chr(i)) >= 97:
		print(i, "equivalent to ",chr(i))

# Make a function that prints A-Z and a-z

def alphabet():
	for i in range(65,65+26*2+6):
		if ord(chr(i)) <= 90 or ord(chr(i)) >= 97:
			print(i, "equivalent to ",chr(i))


alphabet()


# Make a function that asks the user for a message, and turns it into a list of numbers. (It's a cypher ;)) 
Letter = []    

def cypher(message):
	for letter in message:
		Letter.append(ord(letter))
	return Letter

message = input("Enter your secret message:")
Letter  = cypher(message)
print("Its a SECRET WOO HOO... ", Letter)


# Optional: Write a function that does a ceaser cypher (Google), ask the user a number, and shift their message by that number.

Letter = []    

def cypher(message,rot):

	for letter in message:
		if rot.lower() == 'left':
			Letter.append(ord(letter) - 3)
		elif rot.lower() == 'right':
			Letter.append(ord(letter) + 3)
	return Letter

message = input("Enter your secret message: ")
rot = input("Rotate left or right: ")
Letter  = cypher(message, rot)
print("Its a CEASER SECRET HAAH HAAH HAA... ", Letter)
