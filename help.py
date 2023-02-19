#!/usr/env/bin python3

# filename: help.py
# author: OshDubh
# description: gets a list of all of the local functions, then lists them and their docstrings to build a complete help functio
# date created: 23:23 on the 18th of February, 2023
# date last modified: 11:51 on the 19th of February, 2023

# import local packages to get their docstrings 
from init import init

commands = {
	"help": help.__doc__,
	"init": init.__doc__,
	"setup": "Instructions for performing first-time setup of text-to-biden.",
	"image": "Process new, and give tags to, google images.",
	"music": "Adds a background music track to a given video.",
}

def help(command_list):
	"""Get general info on the available commands."""

	output = "" # the built string that this function returns

	# output all of the available commands, since no specific command was supplied
	if not command_list:
		output += "Available commands:\n"

		for command in commands:
			output = output + " - " + command + "\n"

		output = output + "Type 'help [command]' to get more info on a specific command.\n"

	# give the info on a given command, if the given option was a command
	else:
		for s in command_list:
			if s in commands:
				output = output + s + ": " + commands[s] + "\n"
			else:
				output = output + '"' + s + '"' + " is not a valid command. Use [help] to see a list of all the available commands.\n"

	return output # pass the built string back out

# build a list of the commands for processing by the parent 
def command_list():
	return list(commands.keys())
