
def plus(a, b):
    return a + b
print( plus (1, 2) )


def minus (a, b):
    return a - b
print ( minus (2, 1))


def multiply ( a, b ):
    return a * b
print ( multiply (237, 475))


def division ( a, b ):
    return a / b
print ( division ( 2, 1))


cmd = input( "a op b>>")
cmds = cmd.split(' ')
print(cmds[0], cmds[1], cmds[2])


if cmds == '+':
    print ( plus (int.cmds[0], int.cmds[2])) 
elif cmds == '-':
    print ( minus (int.cmds[0], int.cmds[2])) 
elif cmds == '*':
    print ( multiply (int.cmds[0], int.cmds[2])) 
elif cmds == '/':
    print ( division (int.cmds[0], int.cmds[2])) 
        