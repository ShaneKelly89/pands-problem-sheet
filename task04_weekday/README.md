# Task 4 Weekday or Weekend?

This is task 04, where we are asked to write a program that will compute what day it is and respond to user with a response depending on if it the weekend or a weekday. 
 

## Summary of the program

This is a program which when ran will out a response based on what day of the week it is. To figure out what day is it, the program utilizes the following code:
```python
datetime.today().strftime('%A')   
```

A list is created containing all days of the week. 
The days of the weeks are split into 'weekday' and 'weekend', with a response given depending on what day it is. 

The program then loops through the code, and provides the output. 
```python
today = datetime.today().strftime('%A')  
if today in weekend:
    print("It is the weekend today!!")
elif today in weekday:
    print("Today is a weekday, hard luck!")  
```


The user will simply need to run the program, and the program will output the response depending on whay day of the week it is.



## Running the Program 
```python
weekday.py  
```


## References
https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date

https://www.w3schools.com/python/python_conditions.asp
## Author
Shane Kelly 

