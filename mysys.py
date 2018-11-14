import os

def clear():

# os.system('cls' if os.name == 'nt' else 'clear')

    if os.name == 'nt':
        os.system('CLS')
    else:  # posix
        os.system('clear')
