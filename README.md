# pands-problem-sheet
This repository contains all of the problem sheets which we completed through the module 'Programming and Scripting'

The work carried out these problems were first done each week within the 'Programming2021Coursework' repository https://github.com/ShaneKelly89/Programming2021Coursework.git where they can be located each week alongside the labs which were also carried out each week. 

# Descprition of Tasks 

## Task 1 Body Mass Index

This is a program that calculate a persons Body Mass Index using their height and weight.

The Program contains the caluculation for BMI: weight divided by height in meters squared.
```python
bmi = weight / (HeightInMeters * HeightInMeters)
```

As the program asked the user to input their height in centimeters, this number must be divded by 100. When the program is ran (Running the Program) the user will first be asked to enter their weight in kilograms (kg).

The user will then be asked to enter their height in centimeters (cm).
The program will then output that persons BMI and the program will end.



## Running the Program 

```python
py bmi.py
```
Follow the instructions provided in the Summary 

## Task 2 Reverse Second String


This program will ask the user to input a string variable, and will then output every second letter in reverse order.

The call ``` 
[::-2]  ``` is used in this program to achieve the required output. 

For the purpose of this task, the user is being asked to enter the following string:
```The quick brown fox jumps over the lazy dog.``` 

The program will loop through loop through every second letter in the string backwards.
The expected output is: ```.o zletrv pu o wr ch h```

## Running the Program 

```python
py secondstring.py 
```
Follow the instructions provided in the Summary 

## Task 3 Collatz 

This is program designed to intake a positive integer and output the successive value of the given calculation. 
When the program is ran (See Running the Program), the user will be asked to enter a positive integer. 

This is a program that will intake any positive integer and output the successive values of the following calculation:

When the value to be calculated is even, the next value will be calculated by dividing that number by 2:

``` python
if (number % 2) == 0: 
        number = number / 2
``` 

When the number is an odd number, the next value will be calculated by multiplying the number by 3 and adding 1:
```python
else:                      
        number = (number * 3) + 1
``` 

When the value of the calculation is equal to 1, the program will end: 
```python
numberToStop = 1 
while number != numberToStop
```

## Running the Program 

```python
py secondstring.py 
```
For the purpose of the task, the user is asked to the positive integer ```10.```

The expected output is: ```10 5 16 8 4 2 1.```

# Task 4 Weekday or Weekend?

This is task 04, where we are asked to write a program that will compute what day it is and respond to user with a response depending on if it the weekend or a weekday. 

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

# Task 5 Square Root 

This is a program which takes in a positive floating-point number as input, and outputs the approximation of its square root.

Newton's method was researched and used in this program to find the square root: 
```python
a = float(value)  
    for i in range(number_iters):
        value = 0.5 * (value + a / value)
    return value  
```

This was then used to created a function for square root, named 'sqRt' within the program. When a positive integer is entered, the function will produce it's approx. square root.


## Running the Program 
```python
py squareroot.py
```
For the purpose of this program, the user is asked to put input the value ```14.5```.

The expected out for this is ```3.8```.

## Task 6 No. of 'e' 

In this task we are asked to read in a text file, and output the number of e's within that file. For the purpose of this task, I used the poem Sheamus Heaney poem 'Mid Term Break'.\
https://www.poetryfoundation.org/poems/57041/mid-term-break

This progra will read in a text file, and then output the total number of e's within that file. 

First, the txt file 'heaney.txt' was created. This file was then read into the program. 



```python
filename = "heaney.txt"
def totalWords():
    with open(filename) as f:
        words = str(f.read()) 
        return words
```
The text is then coded into a variable 

```python
poem = totalWords()
```
which the program then uses to output the total number of e's 
```python
print(poem.count('e'))
```

## Running the Program 

```python
py es.py
```

# Reference List 
https://www.w3schools.com/python/python_string_formatting.asp
https://www.w3schools.com/python/python_howto_reverse_string.asp
https://scipython.com/book/chapter-2-the-core-python-language-i/examples/string-striding/
https://www.w3schools.com/python/python_numbers.asp
https://realpython.com/python-while-loop/
https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
https://www.w3schools.com/python/python_conditions.asp



