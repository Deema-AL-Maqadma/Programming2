#-------------------------------------------------
# --->>>  Answers of Assignment 2 
# --->>>  Presented to: Eng. Ebtisam Dawoud
# --->>>  Deema Mohammed AL-Maqadma
# --->>>  ID : 2320230766
#-------------------------------------------------
# Q/6 :   Write a Python function to multiply all the numbers in a list

def multiply_numbers(my_list):
    result = 1
    for number in my_list:
        result *= number
    return result

my_list = [1, 2, 3, 4]
print(f"---> Original List: {my_list}")
print(f"---> The multiplication value: {multiply_numbers(my_list)}")

