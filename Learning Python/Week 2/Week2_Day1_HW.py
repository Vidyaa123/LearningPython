#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 08:03:35 2018

@author: Vidyaa
"""

#Alice in Wonderland... Count all alphabets in the text file
#
#Using list and Dictionary 
#
import collections
import string

filename = "alice_in_wonderland.txt"


def count_letters(filename):
    with open(filename, 'r') as f:
        text = f.read()
        text = text.lower()
        letter_count = collections.Counter()
        dict_count = {ltr: 0 for ltr in string.ascii_lowercase}
        for char in text:
        	if char in string.ascii_lowercase:
        		letter_count[char] += 1
        		dict_count[char] += 1
        print("Using Lists ")
        for letter in string.ascii_lowercase:
        	print(letter, letter_count[letter])
    print("Using Dictionary ",dict_count)


count_letters(filename)


