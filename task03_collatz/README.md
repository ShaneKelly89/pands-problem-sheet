# Task 3 Collatz 

This is task 03, where we are asked to write a program to intake a positive integer and output the successive value of the given calculation. 
 

## Summary of the program
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

## References
https://realpython.com/python-while-loop/
## Author
Shane Kelly 
