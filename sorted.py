numbers = [2,4,3,1,5]
strs = ["sss", 'aaa', '세종대왕', '가나다라', '한글']
sort_numbers = sorted(numbers)     # cf. reversed(numbers)
print("sort_numbers=", sort_numbers)
print("numbers=", numbers)

sort_strs = sorted(strs)
print("sort_strs=", sort_strs)

numbers.sort()
print("asc>>", numbers)

numbers.sort(reverse=True)
print("desc>>", numbers)
