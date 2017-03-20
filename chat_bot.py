#!/usr/bin/env python2.7

import sys
import os
import time
import random



greetings = ("hi", "hello", "how are you,")

responses = ["well hello there", "hey", "wassup?"]

# input = raw_input("Please enter a message: ")

def respond_to_greeting(input):
	 
	for word in input.split():
		if word.lower() in greetings:
			return random.choice(responses)
	return "*smiles and nods*"			
			

# Open input file for dialogue
fin = open("chat_bot_input.txt")

# Create output file for dialogue or append if it already exists
if( not os.path.exists("chat_bot_output.txt") ):
	fout = open("chat_bot_output.txt", 'w')
	fout.write('\n')
else:
	fout = open("chat_bot_output.txt", 'a')
	fout.write('\n')

# Begin log with date of conversation
gmtime = time.gmtime()
fout.write(str(gmtime.tm_mday) + '-' + str(gmtime.tm_mon) + '-' + str(gmtime.tm_year) + '\n')

# Engage in dialogue
for input in fin:

	# Write user input to log
	fout.write("user:\t\t" + input.strip() + '\n')

	# Determine chat bot response and write it to log
	output = respond_to_greeting(input)
	fout.write("chat_bot:\t" + output.strip() + '\n')

# print output

# Leave some space for the next entry
fout.write('\n')

# Close files
fin.close()
fout.close()

