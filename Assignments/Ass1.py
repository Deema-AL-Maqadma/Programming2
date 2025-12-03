# Deema Mohammed AL-Maqadma
# Answers of Assignment 1 

#-------------------------------------------------
# whats the output of //
# 1/
num1=3
num2=num1+4
num1=num1+num2+9
print("num1=", num1," num2=",num2)
# output : num1= 19  num2= 7
# ---------------------------------------------------
# 2/ 
number=123
print(number//100)
print(number//10%2)
print(number%10)
# output : 1
#          0
#          3

#------------------------------------------------------
# Deema Mohammed AL-Maqadma
# Q1. Take three numbers from the user and print the greatest number
num1=float(input("Enter the num1 :"))
num2=float(input("Enter the num2 :"))
num3=float(input("Enter the num2 :"))
greatest=None
if num1>num2 and num1>num3:
    greatest=num1
elif num2>num1 and num2>num3:
    greatest=num2
elif num3>num1 and num3>num2:
    greatest=num3
# greatest = max (num1,num2,num3)
print(f"The Gradest Number Is : {greatest}")


#------------------------------------------------------
# Deema Mohammed AL-Maqadma
# Q2. Write a program that displays the following menu:
import math
PI = math.pi
def cube_volume():
    slide = float(input("Enter the slide length of the cube : "))
    return slide
def cylinder_volume():
    radius = float(input("Enter the radius of the cylinder : "))
    height = float(input("Enter the height of the cylinder : "))
    return PI * (radius ** 2) * height
def cone_volume():
    radius = float(input("Enter the radius of the cone : "))
    height = float(input("Enter the height of the cone : "))
    return (1/3) * PI * (radius ** 2) * height

while True:
    print ("""
---> Welcome to the Calculator :
1. Calculate cube volume.
2. Calculate cylinder volume.
3. Calculate cone volume.
4. Exit.""")
    choice = int(input("Enter Your Choice (1-4) : "))
    if choice==1:
        print(f"The Cube Volume : {cube_volume():.2f}")
    elif choice==2:
        print(f"The cylinder Volume : {cylinder_volume():.2f}")
    elif choice==3:
        print(f"The cone Volume : {cone_volume():.2f}")
    elif choice==4:
        print("The Program has been Exited... ")
        break
    else :
        print("Invalid Choice!, Please try again.")

        
#------------------------------------------------------
# Deema Mohammed AL-Maqadma
# Q3. Write a program that calculates the width and area of the street
length = float(input("Enter the  length of the street in meters : "))
if length <= 60:
    width = 4
elif length <= 80:
    width = 6
else:
    width = 8
area = length * width
print(f"Street Length: {length}\nStreet Width: {width}\nStreet Area: {area} sqm\n")
