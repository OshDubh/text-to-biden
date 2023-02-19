#!/usr/env/bin python3

# filename: init.py
# author: OshDubh
# description: Initialises a new project folder
# date created: 11:19 on the 19th of February, 2023
# date last modified: 11:19 on the 19th of February, 2023

# external imports
import os

def init(name):
    """Initialises a new project in the 'Projects' folder, with the given title. Returns the name of the project folder"""
    # create the "Projects" folder if it hasn't been created yet
    if not os.path.isdir('./Projects'):
        os.mkdir('./Projects')

    # create a new project folder with the given name
    path = os.path.join('./Projects', name)
    os.mkdir(path)
    return path # pass the path back to the parent process so we know where to work