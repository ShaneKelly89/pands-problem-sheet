
#This is a program which will have the days of the week within it
#The program will output, depending on what day is it, if it the weekend or if it is a weekday
#Author Shane Kelly
#Write a program that outputs whether or not today is a weekday.
#Firstly  I will here breakdown the task into seperate tasks before writing any code 
#1 : Create a list containing all 7 days of the week
#2 : Code for which days are weekdays and which are weekends
#3 : Use web search to find out what day it is when running program 
#4 write code that will output if it is a weekend or weekday 

from datetime import datetime
print(datetime.today().strftime('%A')) #Piece of code found via stackoverflow 
# https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date

days = ("Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
)

weekday = days[0:5]  #coding for weekdays via 'days' list 
weekend = days[5:7]  #coding for weekend via 'days' list 

#print(weekend)
#print(weekday)

#Need to run a loop through list, and provide response 'weekend' and 'weekday' 
#https://www.w3schools.com/python/python_conditions.asp
today = datetime.today().strftime('%A')  

if today in weekend:
    print("It is the weekend today!!")
elif today in weekday:
    print("Today is a weekday, hard luck!")
#The above code is checking which tuple 'today' is included in and providing the appropriate response