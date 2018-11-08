def fn():
    print("fn called")

def exp(x):
    return x ** 2 

exp3 = exp(3)
print(exp3)

print(exp(9))


def get_fruits():
    return ['오렌지', '사과', '바나나']

print(get_fruits()[1])

def get_name():
    return ('Kent', 'Beck')
name = get_name()
print(name)

def full_name(first_name, last_name):
    return first_name + ' ' + last_name

name = get_name
print(name, )    

def var_param(a, *vp):
    print(type(vp))
    print(a, len(vp), vp[len(vp) - 1])

var_param('A','B','c')

def default_param(a, vp = 100):
    print(a, vp)

default_param(1)
