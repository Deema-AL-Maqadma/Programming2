# Deema Mohammed AL-Maqadma
help("keywords") # python reserved words (also know as keywords)
x = 5 #A variable in Python is only a label, or reference to the object stored in the memory, and not a named memory location
print(type(x)) # will get to know the type of the value at run-time
#-----------------------------------------------------------------
num1= 10 #integer
num2= 10.5 #float
num3= 6j+10 #complex
print(num1)
print(float(num1))
print(complex(num1))
#-----------------------------------------------------------------
i=0
while i<4:
    print(i, end=" ")
    i+=1
    if i==3:
        break
else:
    print(0)
