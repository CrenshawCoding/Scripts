import csv
from os.path import exists
import os
from datetime import date, datetime

today = date.today()
file_name = 'rejection_data.csv'
file_name_new = 'rejection_data_temp.csv'
if not exists(file_name):
    open(file_name, 'x')
file = open(file_name, 'r+')
file_new = open(file_name_new, 'w')
fieldnames = ['Datum', 'keine_antwort', 'neuer_chat', 'Abgelehnt', 'chat_ende']
reader = csv.DictReader(file)
writer = csv.DictWriter(file_new, fieldnames=fieldnames)
option = None
time_format = "%d.%m.%Y"

def get_input():
    return input("Was ist passiert? ")
    
    
option = get_input()
data = []
if os.stat(file_name).st_size == 0:
    data = [{'Datum' : today.strftime(time_format), 'keine_antwort' : 0, 'neuer_chat' : 0, 'Abgelehnt' : 0, 'chat_ende' : 0}]
else:
    for row in csv.DictReader(file):
        data.append(row)
if datetime.strptime(data[-1]['Datum'], time_format).date() != today:
    print('debug')
    print(datetime.strptime(data[-1]['Datum'], time_format), "!=", today)
    writer.writerow({'Datum' : today.strftime(time_format), 'keine_antwort' : 0, 'neuer_chat' : 0, 'Abgelehnt' : 0, 'chat_ende' : 0})



lastrow = data[-1]
writer.writeheader()

for row in csv.DictReader(file):
    if datetime.strptime(row['Datum'], time_format) != today:
        writer.writerow(row)
        
if str(option) == 'a':
    writer.writerow({'Datum' : today.strftime(time_format), 'keine_antwort' : lastrow['keine_antwort'], 'neuer_chat' : lastrow['neuer_chat'], 'Abgelehnt' : int(lastrow['Abgelehnt']) + 1, 'chat_ende' : lastrow['chat_ende']})
elif str(option) == 'c':
    writer.writerow({'Datum' : today.strftime(time_format), 'keine_antwort' : lastrow['keine_antwort'], 'neuer_chat' : int(lastrow['neuer_chat']) + 1, 'Abgelehnt' : lastrow['Abgelehnt'], 'chat_ende' : lastrow['chat_ende']})
elif str(option) == 'k':  
    writer.writerow({'Datum' : today.strftime(time_format), 'keine_antwort' : int(lastrow['keine_antwort']) + 1, 'neuer_chat' : lastrow['neuer_chat'], 'Abgelehnt' : lastrow['Abgelehnt'], 'chat_ende' : lastrow['chat_ende']})
elif str(option) == 'e':
    writer.writerow({'Datum' : today.strftime(time_format), 'keine_antwort' : lastrow['keine_antwort'], 'neuer_chat' : lastrow['neuer_chat'], 'Abgelehnt' : lastrow['Abgelehnt'], 'chat_ende' : int(lastrow['chat_ende']) + 1})
else:
    option = invalid_input()
file.close()
file_new.close()
os.remove(file_name)
os.rename(file_name_new, file_name)
    