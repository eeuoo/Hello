from datetime import datetime,time,date

dt = datetime.strptime('20190312', '%Y%m%d')
print(isinstance(dt, date))
print(dt.strftime('%Y.%m.%d'))