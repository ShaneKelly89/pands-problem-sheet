
#Bmi.py
#This program will be used to calculate a person's bmi
#Author Shane Kelly

#Firstly, I must code for 'weight' and have the user enter their weight 
#weight = int(input("Enter weight here\n"))

#Second, I must do the same for 'height'
#height = float(input("Enter Height here\n"))

#I will then need to compute the calculation for bmi 

weight = int(input("Enter weight here\n"))  #coding for weight
height = float(input("Enter Height here in centimeters\n"))     #coding for height
HeightInMeters = (height / 100) #This line added in response to comments at the end 
bmi = weight / (HeightInMeters * HeightInMeters)     #creating the calculation for bmu
print ("bmi is {}".format(bmi))   #https://www.w3schools.com/python/python_string_formatting.asp

#Enter weight here first result below (changes made to Height (1.8))
#65
#Enter Height here
#180
#bmi is 0.002006172839506173

#Trial and error found height is expected to be in meters for this formula 
#to work. As such, I made adjustments. 