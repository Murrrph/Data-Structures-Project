#!/usr/bin/env python2.7

import sys
import random



greetings = ("hi", "hello", "how are you,")

responses = ["well hello there", "hey", "wassup?"]

input = raw_input("Please enter a message: ")

def respond_to_greeting(input):
	 
	for word in input.split():
		if word.lower() in greetings:
			return random.choice(responses)
	return "*smiles and nods*"			
			

output = respond_to_greeting(input)
print output

