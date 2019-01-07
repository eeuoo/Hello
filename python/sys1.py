import sys, os

# import mysys
# mysys.clear()

from mysys import clear
clear()

print("__file__ ==>", __file__)
print("dirname ==>", os.path.dirname(__file__))
print("absname ==>", os.path.abspath(__file__))

print(sys.argv, len(sys.argv))

def print_sys_vars():
    for i in [sys.version, sys.copyright, sys.platform]:
        print("--->", i)

sa = sys.argv
if len(sa) < 2:
    print_sys_vars()
    sys.exit()

with open(sa[1],'r', encoding = 'utf8'):
    for line in file:
        print(line)


        