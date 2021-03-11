# This Is A Terminal For Windows Made In Python

import subprocess
import os
import platform

os.system('') # allows colours to be printed in Command Prompt and Powershell natively

class colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

user = subprocess.run(['whoami'], capture_output=True).stdout.decode('UTF-8').strip()
coloredUser = f'{colors.YELLOW}{user}'

hostname = subprocess.run(['hostname'], capture_output=True).stdout.decode('UTF-8').strip()
coloredHostname = f'{colors.BLUE}{hostname}'


fullPrompt = f'{colors.BOLD}{colors.RED}[{coloredUser}{colors.GREEN}@{coloredHostname}{colors.RED}]{colors.WHITE}$ {colors.RESET}'

if platform() == "Windows":
    system("title " + "Terminal v0.1") # Does not work on Linux

print("Terminal v0.1 By SkepticalPotato2k And LukasDoesDev")

while True:
    print()
    commandInput = input(prompt)
    
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
                script = ' '.join(raw)

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


