import datetime as datetime
import time as tm
from typing import List

ar_time=[900,910,915,945,950,1010,1030]
dp_time=[1000,1100,930,1015,1145,1115,1200]
ar_time.sort()
dp_time.sort()
n=len(dp_time)
tr=[]
p=1
'''for i in range(len(ar_time)):
    for j in range(len(dp_time)):
        if ar_time[i]<dp_time[j]:
            if(j==n-1):
                tr.append(p)
                p += 1
        elif ar_time[i]>dp_time[j]:
            tr.append(p)
            p -= 1
print(tr)
print("no of  max platform required:",max(tr))

st='9:10'
#print(ar_time.strftime('%H:%M'))
#ar_time.append(str(datetime.datetime.strftime("%H:%M")))
print(st)
#if tm.strftime('%H:,%M:')<'9:10':
t=tm.st()
print(t.hour*1000+t.minute*100)
# importing the datetime module
st='9:10'
import datetime as datetime
#timestamp = datetime.timestamp(now)

current_date = datetime.time(8,10)
print("Original date and time object:", current_date)

print("Date and Time in Integer Format:",
	current_date.hour*10000 +
	current_date.minute*100 )

print("Date and Time in Integer Format:",
      int(current_date.strftime("%H%M")))

time_list=[datetime(' 09:00')]
#time_list_formatted = [int(current_date.strftime("%H%M"))for current_date in datetime(ar_time)]

time_list_formatted = [int(x.strftime(format='%H%M')) for x in time_list]
print(time_list_formatted)'''
max_cnt=0
cnt=0
i=0
j=0
while i<n and j<n:
    if ar_time[i]<dp_time[j]:
        cnt+=1
        i+=1
    else:
        cnt-=1
        j+=1
    i+=1
    if max_cnt<cnt:
        max_cnt=cnt
print(max_cnt)