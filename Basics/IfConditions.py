#Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
a = 200
b = 33
if b > a:
  print("b is greater than a") 
elif a == b: 
  print("a and b are equal") 
else:
  print("a is greater than b")
#Short Hand If ... Else/ Syntax: Condition If True   If   Condition   Else   Condition If False
a = 2
b = 330
print("A") if a > b else print("B")
#----------------------------------------------------------------
# task 1/ chek if the number is even or odd
num =int(input("Enter a number :"))
if num%2==0:
  print(f"{num} is even")
else:
  print(f"{num} is odd ")
#----------------------------------------------------------------
# task 2/ chek if the number is divisible by 3 and 5
num =int(input("Enter a number :"))
if num%5==0 and num%3==0:
  print(f"{num} is divisible by 3 and 5")
else:
  print(f"{num} is not divisible by 3 and 5 ")
#----------------------------------------------------------------
# task 3/ chek if the number is divisible by 3 or 5
num =int(input("Enter a number :"))
if num%5==0 or num%3==0:
  print(f"{num} is divisible by 3 or 5")
else:
  print(f"{num} is not divisible by 3 or 5 ")
#----------------------------------------------------------------
# task 4/ chek if the number is even and not equal zero
num =int(input("Enter a number :"))
if num%2==0 and num!=0:
  print(f"{num} is true ")
else:
  print(f"{num} is false ")
#----------------------------------------------------------------
# task 5/ take three numbers from the user and print the smalest number
n1 = int(input("Enter a number :"))
n2 = int(input("Enter a number :"))
n3 = int(input("Enter a number :"))
if n1<n2 and n1<n3:
  print(f"{n1} is the smallest")
elif n2<n1 and n2<n3:
  print(f"{n2} is the smallest")
elif n3<n1 and n3<n2:
  print(f"{n3} is the smallest")
else:
  print("Not found the smallest...")
#----------------------------------------------------------------
# للتحقق هل ناجح ام راسب مع التقدير باستخدام الشرط المتداخل
score= int(input("Enter Score :"))
result = " "
if score>=50 and score<100:
  result="Successful !"
  if score>=90:
    result+=" ,Excellent"
  elif score>=80:
    result+=" ,Very Good"
  elif score>=70:
    result+=" , Good"
  elif score>=60:
    result+=" ,acsept Good"
  else:
    result+=" ,not Good"
elif score>=100 and score<0:
  result="Invalid Score!"
else:
  result="Fail..."
print(f"Result = {result}")
#----------------------------------------------------------------
# task 6/chek the year is leap year or not
year=int(input("Enter a year: "))
if year%4 == 0:
  if year%100 == 0:
    if year%400==0:
      print(f"{year} a leap year...")
    else:
       print(f"{year} not leap year...")
  else:
   print(f"{year} not leap year...")
else:
  print(f"{year} not leap year...")
#----------------------------------------------------------------
# task 4/ a program
choice =int(input("""
1/ calculate square area 
2/ calculate rectangle area       
3/ Exit
--->>> Choose an operation:"""))
if choice==1:
  side=int(input("Enter side :"))
  print(f"Square Area = {side*side}")
elif choice==2:
  length=int(input("Enter the length: "))
  width=int(input("Enter the width: "))
  print(f"The Rectangle Area = {length*width}")
elif choice==3:
  exit(0)
#-----------------------------------------------
n=10
if n>10:
  pass
print("Thx ^_^")