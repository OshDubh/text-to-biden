#!/usr/env/bin python3

# filename: texttobiden.py
# author: OshDubh
# description: the main file for the texttobiden program, the one that should be run to create content
# date created: 22:26 on the 18th of February, 2023
# date last modified: 22:26 on the 18th of February, 2023

# external imports
import os
import sys

# local imports
from help import help, command_list
from init import init

# Process the cli and pass it to the relevant functions
commands = sys.argv # build a list of the input
commands.remove(__file__) # remove the filename from the options

# check if the first argument is a valid command
if not commands:
	print(help("")) # list all the available commands

# it was a valid command, pass to the right function
elif commands[0] in command_list():
	output = locals()[commands[0]](commands[1:]) # get the function name and then process the given arguments, passing the result back to output
	print(output)

# no valid command was given
else:
	print('"' + commands[0] + '"', 'is not a valid command. Use "help" to get a list of all available commands.')