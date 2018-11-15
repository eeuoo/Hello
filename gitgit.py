import os 
import datetime

now = datetime.datetime.now()

# cmd창에서 실행하려면 sys가 있어야 하지만, Visual Studio에선 실행 가능

default_message = "new {}".format(now.strftime('%Y-%m-%d'))
commit_msg = default_message

input_msg = input ("디폴트로 진행 enter or 메시지 입력 -->")

if input_msg == '':
    print(commit_msg)

elif input_msg != '':
    commit_msg = input_msg

print("commit ...", commit_msg)
os.system("git add --all")
os.system('git commit -am "{}"'.format(commit_msg))
os.system("git push")


