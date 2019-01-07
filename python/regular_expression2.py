import re

string = "aaaaaaa<hr>This"

pattern = re.compile("<(.*)>")         # cf. re.compile("<.*>")

mm = re.findall(pattern, string)
print(mm)

for m in re.finditer(pattern, string):
    print(m.groups(1))
