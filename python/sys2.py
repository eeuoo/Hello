import sys, os

# import mysys
# mysys.clear()

print("SSSS>>", sys.path)

print("__file__ ==>", __file__)
print("dirname ==>", os.path.dirname(__file__))
print("absname ==>", os.path.abspath(__file__))

dir_name = os.path.dirname(__file__)
a_path = os.path.abspath(dir_name)
up_dir = os.path.join(a_path, '..')     #c:\workspace\hello
sys.path.append(os.path.abspath(up_dir))

print("a_path>>>>", a_path)
print("BASECAMP", os.path.abspath(up_dir))
print("+++++++", sys.path)
