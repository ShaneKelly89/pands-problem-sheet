
#Bmi.py
#This program will be used to calculate a person's bmi
#Author Shane Kelly

#Firstly, I must code for 'weight' and have the user enter their weight 
#weight = int(input("Enter weight here\n"))

#Second, I must do the same for 'height'
#height = float(input("Enter Height here\n"))

#I will then need to compute the calculation for bmi 

weight = int(input("Enter weight here\n"))
height = float(input("Enter Height here in meters\n"))
HeightInMeters = (height / 100) #This line added in response to comments at the end 
bmi = weight / (HeightInMeters * HeightInMeters)
print ("bmi is {}".format(bmi))   #https://www.w3schools.com/python/python_string_formatting.asp

#Enter weight here first result below (changes made to Height (1.8))
#65
#Enter Height here
#180
#bmi is 0.002006172839506173

#Trial and error found height is expected to be in meters for this formula 
#to work. As such, I have changed the user output to ask the user to enter their hight in meters 