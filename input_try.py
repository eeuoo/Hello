cmd = input("input(usage: 이름, 나이, 성별)>>")
print(cmd)

# 1 값 존재여부 체크
if cmd == '':
    print("정확히 입력해 주세요")
    exit()

# 2 ',' 값이 있는지 체크
if ',' not in cmd:
    print("다시 입력하세요")
    exit()

cmds = cmd.split(',')

# 3 3개의 값이 있는지 체크
if (len(cmds) != 3):
        print("안돼요. 다시 입력하세요.")
        exit()

outmsg = "당신의 이름은 {}, 나이는 {}, 성별은 {}입니다."
print(cmds[0], cmds[1], cmds[2])

print(outmsg.format(cmds[0], cmds[1], cmds[2]))
