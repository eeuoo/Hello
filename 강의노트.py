import random
import sqlite3

fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")

name_list = '김미'

for full_name in range(0,100):
    sung = random.choice(fam_names)
    myname = random.choice(first_names) + random.choice(first_names)

    full_name = ",{}{}".format(sung, myname)
    
    name_list += full_name

print(name_list)