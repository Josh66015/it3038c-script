import datetime
#My project one is from a get time script to get the time right now 

#and display it. As well as specifically the year month day hour and 

#minutes.

#origional source :

#Get current date and time using Python. GeeksforGeeks. (2022, June 22). Retrieved October 9, 2022, 
#from https://www.geeksforgeeks.org/get-current-date-and-time-using-python/ 

#To run the program you will neeed to have python installed on your device.

#In github copy raw content of it3038c-scripts/projects/project1.py.

#Open python and create a new file by pressing file new file.

#Paste the contents into file hit save name it P1.py then run.

#Sample expected output:

#The current time is :
#2022-10-09 16:17:42.774770
#Year : 2022
#Month :  10
#Day :  9
#Hour :  16
#Minute :  17
#Second : 25
#Microsecond : 547727

 
current_time = datetime.datetime.now()

print("The current time is :")

print(current_time)
 
print("Year :", current_time.year)
 
print("Month : ", current_time.month)
 
print("Day : ", current_time.day)
 
print("Hour : ", current_time.hour)
 
print("Minute : ", current_time.minute)

print("Second :", current_time.second)
 
print("Microsecond :", current_time.microsecond)