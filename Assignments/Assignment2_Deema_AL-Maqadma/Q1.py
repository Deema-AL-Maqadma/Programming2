#-------------------------------------------------
# https://youtu.be/nHR-F3nzUH0?si=GP8qrPdGDla5gan6 رابط شرح الاكواد يوتيوب
# --->>>  Answers of Assignment 2 
# --->>>  Presented to: Eng. Ebtisam Dawoud
# --->>>  Deema Mohammed AL-Maqadma
# --->>>  ID : 2320230766
#-------------------------------------------------
# Q/1 :  Write a Python program to get unique values from a list
def get_unique_values(my_list):
    unique_set = set(my_list)
    unique_list = list(unique_set)
    return unique_list

my_Colors = ["Red","Blue","Black","Pink","Blue","Black"]
print(f"---> Original List: {my_Colors}")
print(f"---> List with uniqe values: {get_unique_values(my_Colors)}")

