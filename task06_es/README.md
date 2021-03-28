# Task 6 No. of 'e' 

In this task we are asked to read in a text file, and output the number of e's within that file. For the purpose of this task, I used the poem Sheamus Heaney poem 'Mid Term Break'.\
https://www.poetryfoundation.org/poems/57041/mid-term-break

## Summary of the Program
This is a program which reads in a text file, and then output the total number of e's within that file. 

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


## References 
//www.w3schools.com/python/ref_list_count.asp

## Author 
Shane Kelly 