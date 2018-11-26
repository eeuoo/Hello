import re

the_zen = """ The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to d
Although that way may not be obvious at first unless you're Dutc
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those! """


# 마침표 이후 개행이 없는 라인에 개행 추가
# s = re.sub("\.[^\n]", '.\n', the_zen)

m = re.findall("(.*)is better than", the_zen, re.MULTILINE)
m2 = re.findall("is better than(.*)", the_zen, re.MULTILINE)
# print(m)
# print(m2)

m3 = re.findall("(.*) is.* better than (.*)\.", the_zen, re.MULTILINE)

# print(m3)

for i in m3:
    print( "{} > {}".format(i[0].lower(),i[1]))