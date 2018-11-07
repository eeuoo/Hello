
def plus(a, b):
    return a + b
print( plus (1, 2) )


def minus (a, b):
    return a - b
print ( minus (2, 1))


def multiply ( a, b ):
    return a * b
print ( multiply (2, 1))


def division ( a, b ):
    return a / b
print ( division ( 2, 1))


cmd = input( "a op b>>")
cmds = cmd.split(' ')
print(cmds[0], cmds[1], cmds[2])

a = int(cmds[0])
b = int(cmds[2])

if cmds[1] == '+':
    print ( plus(a, b)) 
elif cmds[1] == '-':
    print ( minus(a, b)) 
elif cmds[1] == '*':
    print ( multiply(a, b)) 
elif cmds[1] == '/':
    print ( division(a, b)) 
    
        