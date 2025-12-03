#-------------------------------------------------
# --->>>  Answers of Assignment 2 
# --->>>  Presented to: Eng. Ebtisam Dawoud
# --->>>  Deema Mohammed AL-Maqadma
# --->>>  ID : 2320230766
#-------------------------------------------------
# Q/4 :    Write a Python function to find the Max of three numbers

def max_Numbers(n1,n2,n3):
    max_num = n1
    if n1>n2 and n1>n3:
        max_num=n1
    elif n2>n1 and n2>n3:
       max_num=n2
    elif n3>n1 and n3>n2:
       max_num=n3
    else:
       return "Not found the smallest..."
    return max_num

n1 = int(input("Enter a number :"))
n2 = int(input("Enter a number :"))
n3 = int(input("Enter a number :"))

print(f"---> The max num is: {max_Numbers(n1,n2,n3)}")

