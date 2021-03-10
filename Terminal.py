# This Is A Terminal For Windows Made In Python

import os
import getpass
from os import system

system("title " + "Terminal v0.1")

print("Terminal 0.1 By SkepticalPotato2k And LukasDoesDev")

while True:
    print()
    commandInput = input(getpass.getuser() + "@Terminal $ ")
    
    if commandInput == 'exit':
        break
    elif commandInput.startswith('@eval'):
            if commandInput == '@eval':
                print('No script name specified')
            else:
                # Split for each space
                raw = commandInput.split(' ')
                # Remove the "@eval" from the start
                raw.pop(0)
                # Join the list together to create the script location
                script = raw.join(' ')

                # Open for reading
                scriptFile = open(script, 'r')
                # Make a list from the lines of the file
                lines = scriptFile.readlines()
 
                # Loop over the lines in the file
                for line in lines:
                # Remove whitespace (spaces, newlines etc.) at the beginning and at the end of the string
                    command = line.strip()
                # if command is a comment.
                    if command.startswith('#'):
                        pass # You cannot have empty blocks. You have to have code or the pass keyword
                else:
                    os.system(commandInput)
    else:
        # if command is a comment.
        if commandInput.startswith('#'):
            pass # You cannot have empty blocks. You have to have code or the pass keyword
        else:
            os.system(commandInput)


