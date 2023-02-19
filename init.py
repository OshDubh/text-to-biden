#!/usr/env/bin python3

# filename: init.py
# author: OshDubh
# description: Initialises a new project folder
# date created: 11:19 on the 19th of February, 2023
# date last modified: 12:17 on the 19th of February, 2023

# external imports
import os

def init(name):
	"""Initialises a new project in the 'Projects' folder, with the given title. Returns the name of the project folder"""
	# create the "Projects" folder if it hasn't been created yet
	if not os.path.isdir('./Projects'):
		os.mkdir('./Projects')

	name = name[0] # it's passed as a list, so convert the first arg to string 
	# create a new project folder with the given name
	path = os.path.join('./Projects', name)

	# catch if the file already exists
	try:
		os.mkdir(path)
		print(path, "was created.")
		return path # pass the path back to the parent process so we know where to work

	except FileExistsError:
		print("Project folder already exists.", name, "was selected as the current project folder")
		return path # pass the path back 