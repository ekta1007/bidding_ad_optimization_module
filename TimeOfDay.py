TimeOfDay.py
#time > [00:6:00: early morning, 6:00-12:00 morning 12:00-6:00 afternoon 6:00 night]

import datetime
import random , csv
full_list_all=[]
#2013-02-23 11:05:19
dict_day={'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6,'Sunday':7}
with open("D:/Desktop/day_modified.csv", "r") as source:
	header=source.readline().replace('\n','') # header
	list_all=[line.replace('\n','') for line in source]
for j in range(0,len(list_all)):
    date,time_full=list_all[j].split(',')[1].split(' ')
    time=int(time_full.split(':')[0])
    month,day,year = (int(x) for x in date.split('/'))    
    ans=datetime.date(year,month,day)
    ans= (ans.strftime("%A"))
    day_of_week=dict_day[ans]
    if time>= 0 and time <= 6 :
        time_of_day=('Early Morning')
    elif time> 6 and time <=12 :
        time_of_day=('Morning')
    if time> 12 and time <= 18 :
        time_of_day=('Afternoon')
    if time> 18 and time <= 24 :
        time_of_day=('Night')
    xx=list_all[j].split(',')[0:]+[time_full,ans,day_of_week,time_of_day] # Storing all the time-specific variables for further analysis
    full_list_all.append(xx)
print 'dumping all values in csv'
header=header.split(',')[0:]
x=['time', 'day of week', 'day_of_week_in_number', 'time of day']
header=header+x
sink =open("D:/Desktop/day_modified_1.csv", "wb") 
mywriter = csv.writer(sink,dialect='excel')
mywriter.writerow(header)
for i in range(0,len(full_list_all)):                                  
    mywriter.writerow(full_list_all[i]) #full_list_all is a list, likewise header is a list writerow writes as list 
sink.close()
