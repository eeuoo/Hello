import os 

import datetime

now = datetime.datetime.now()


default_message = "new {}".format(now.strftime('%Y-%m-%d'))
commit_msg = default_message

input_msg = input ("디폴트로 진행 1 or 메시지 입력 -->")

if input_msg == '1':
    print(commit_msg)

else:
    if input_msg != '':
        commit_msg = input_msg

print("commit ...", commit_msg)
os.system("git add --all")
os.system('git commit -am "{}"'.format(commit_msg))
os.system("git push")
