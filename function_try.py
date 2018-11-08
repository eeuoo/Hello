Q = 0

while (Q >= 0):
    
    cmd = input("a op b>>")
    Q = len(cmd) 
    
    if Q == 0:
        break

    def plus(a, b):
        return a + b

    def minus (a, b):
        return a - b

    def multiply ( a, b ):
        return a * b

    def division ( a, b ):
        if b == 0:
             return a
        return a / b
        
    cmds = cmd.split(' ')

    # a,op, b = cmds

    a = int(cmds[0])
    b = int(cmds[2])
    op = cmds[1]

    if op == '+':
        r = ( plus(a, b)) 
    elif op == '-':
        r = ( minus(a, b))
    elif op == '*':
        r = ( multiply(a, b))
    elif op == '/':
        r = ( division(a, b)) 


    if op in '/' :
        print ( "정답 {:.2f}".format(r) )
    else :
        print ( "정답 {:d}".format(r) )
            
