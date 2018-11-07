# 시간과 날짜
import datetime

# dt = datetime.date(1999,11,10)
# print(dt)
# print(dt.year, dt.month, dt.day)
#
# tm = datetime.time(11,10,15)
# print(tm)
# print(tm.hour, tm.minute, tm.second)
#
# dttm = datetime.datetime(1988,1,10,12,13,14)
# print(dttm)
# print(dttm.year, dttm.month, dttm.day, dttm.hour, dttm.minute, dttm.second)
#
# dttm = datetime.datetime.now() # system date
# print(dttm)

dttm = datetime.datetime(1988,1,10,12,13,14)
# print(dttm)
print(dttm.year, dttm.month, dttm.day, dttm.hour, dttm.minute, dttm.second)

s = dttm.strftime('%Y-%m-%d %p %I:%M:%S') # 1988-01-10 PM
print(s)
