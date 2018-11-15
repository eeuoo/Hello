import sys, os 

import datetime
now = datetime.datetime.now()

sa = sys.argv #0:실행파일 1:메세지 부분

default_message = "new {}".format(now.strftime('%Y-%m-%d'))
commit_msg = default_message
has_msg = len(sa) >= 2

if has_msg:
    sa[1] = commit_msg

else:
    input_msg = input("디폴트 메시지라도 괜찮습니까? (yes: Enter or input massage)")
    if input_msg != '':
        commit_msg = input_msg

print("commit ...", commit_msg)
os.system("git add --all")
os.system('git commit -am "{}"'.format(commit_msg))
os.system("git push")
