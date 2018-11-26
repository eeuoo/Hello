
import re

string = "123?45yy7890 hi 999 heLLo"

# pattern = re.compile("[0-9]{1,3}")
pattern = re.compile("(\d{1,3})")

mm = re.findall(pattern, string)
print(mm)

for m in re.finditer(pattern, string):
    print(m.groups())
