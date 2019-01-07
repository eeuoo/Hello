def write_file():
    with open("a.csv","w",encoding='utf8') as file:
        file.write("이름,성별,나이\n")
        file.write("홍길동,남,24")

def read_file():
    with open ("a.csv","r",encoding='utf8') as file:
        for line in file:
            print(line)

write_file()
read_file()