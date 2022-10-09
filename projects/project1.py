import datetime
#My project one is from a get time script to get the time right now 

#and display it. As well as specifically the year month day hour and 

#minutes.

#To run the program you will neeed to have python installed on your device.

#In github copy raw content of it3038c-scripts/projects/project1.py.

#Open python and create a new file by pressing file new file.

#Paste the contents into file hit save name it P1.py then run.
 
current_time = datetime.datetime.now()

print("The current time is :")

print(current_time)
 
print("Year :", current_time.year)
 
print("Month : ", current_time.month)
 
print("Day : ", current_time.day)
 
print("Hour : ", current_time.hour)
 
print("Minute : ", current_time.minute)
