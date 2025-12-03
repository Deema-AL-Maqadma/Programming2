#-------------------------------------------------
# --->>>  Answers of Assignment 2 
# --->>>  Presented to: Eng. Ebtisam Dawoud
# --->>>  Deema Mohammed AL-Maqadma
# --->>>  ID : 2320230766
#-------------------------------------------------
# Q/3 :    Write a Python program to sum all the odd items in a list

def sum(my_list):
    total = 0 
    for item in my_list:   
        if item % 2 != 0: 
            total += item 
    return total

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"---> The original List: {my_list}")
print(f"---> The sum of the odd number: {sum(my_list)}") 

