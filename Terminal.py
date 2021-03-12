# This Is A Terminal For Windows Made In Python

import subprocess
import os
import platform

os.system('') # allows colours to be printed in Command Prompt and Powershell natively

class colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    ORANGE = '\033[35m'
    ORANG = '\x1b[38;2;255;165;0m'
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

if platform.system() == "Windows":
    os.system("title " + "Terminal v0.1") # Does not work on Linux

# Might be useful for clearing the terminal screen
CLEAR_SCREEN = 'clear'
if platform.system() == 'Windows':
    CLEAR_SCREEN = 'cls'
    
# Usage:

system(CLEAR_SCREEN) # This works on both windows and linux :D


print("Terminal v0.1 By SkepticalPotato2k And LukasDoesDev")

def runCommand(cmd):
    if cmd.startswith('cd'):
        if cmd == 'cd':
            print('No directory specified')
        elif cmd == 'cd..':
            os.chdir('..')
        else:
            # Split for each space
            raw = cmd.split(' ')
            # Remove the "@eval" from the start
            raw.pop(0)
            # Join the list together to create the script location
            directory = ' '.join(raw)

            if os.path.isdir(directory):
                os.chdir(directory)
                
            else:
                print('Invalid directory specified')
    else:
        # if command is a comment.
        if cmd.startswith('#'):
            pass # You cannot have empty blocks. You have to have code or the pass keyword
        else:
            os.system(cmd)

while True:
    print()
    prompt = f'{colors.BOLD}{colors.RED}[{coloredUser}{colors.GREEN}@{coloredHostname} {colors.ORANGE}{os.path.basename(os.getcwd())}{colors.RED}]{colors.WHITE}$ {colors.RESET}'
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
                runCommand(command)
    else:
        runCommand(commandInput)
    


