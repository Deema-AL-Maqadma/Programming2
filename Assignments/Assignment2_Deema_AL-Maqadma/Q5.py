#-------------------------------------------------
# --->>>  Answers of Assignment 2 
# --->>>  Presented to: Eng. Ebtisam Dawoud
# --->>>  Deema Mohammed AL-Maqadma
# --->>>  ID : 2320230766
#-------------------------------------------------
# Q/5 :    Write a Python function to print the even numbers from a given list

def even_numbers(my_list):
    for item in my_list:   
        if item % 2 == 0: 
            print(f"The Number {item} Is Even")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"---> The original List: {my_list}")
print(f"---> The even number: ") 
even_numbers(my_list)

