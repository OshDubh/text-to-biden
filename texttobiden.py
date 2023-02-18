#!/usr/env/bin python3

# filename: texttobiden.py
# author: OshDubh
# description: the main file for the texttobiden program, the one that should be run to create content
# date created: 22:26 on the 18th of February, 2023
# date last modified: 22:26 on the 18th of February, 2023

# imports
import os
import sys

def help(command_list):
    """returns all commands, or gives info on a specific command"""
    # variables
    commands = {
        "help": "Get general info on the available commands.",
        "init": "Initialise a new project",
        "image": "Process new, and give tags to, google images.",
        "music": "Adds a background music track to a given video",
    }

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


print(help(sys.argv[1:]))
