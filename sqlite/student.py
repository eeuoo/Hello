with open("students.csv","w",encoding = 'utf8') as file:
    file.write("이햇님,여,20,95\n이햇살,남,19,84\n박달님,남,18,88\n박달빛,여,21,90\n최바다,여,27,99\n최 산,남,30,95\n김부각,여,51,83\n김자반,남,48,85")

with open("students.csv","r",encoding = 'utf8') as file:
    for line in file:
        print(line)

