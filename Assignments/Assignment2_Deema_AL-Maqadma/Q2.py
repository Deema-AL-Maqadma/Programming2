#-------------------------------------------------
# --->>>  Answers of Assignment 2 
# --->>>  Presented to: Eng. Ebtisam Dawoud
# --->>>  Deema Mohammed AL-Maqadma
# --->>>  ID : 2320230766
#-------------------------------------------------
# Q/2 :   Write a Python program to copy a tuple

def copy_tuple(my_tuple):
    return tuple(my_tuple)

original_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"---> Original Tuple: {copy_tuple(original_tuple)}")

