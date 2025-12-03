#--------------------------------------------------------------
name = "    Deema, Mohammed, AL-Maqadma"
#Strings are Arrays
print(name[0])

#Slicing من بداية الترقيم لعند الرقم النهاية بيوقف عنده وهو ليس من ضمن الحل
print(name[2:4]) # em
print(name[:]) # Deema Mohammed AL-Maqadma
print(name[1:]) # eema Mohammed AL-Maqadma

#Negative Indexing 
print(name[-4:-2]) # ad
print(name[:-1]) # Deema Mohammed AL-Maqadm

#String Length/ To get the length of a string, use the len() function
print(len(name)) # يحسب الفراغات من ضمن الطول

#String Methods //
#The strip() method removes any whitespace from the beginning or the end:
print(name)
print(name.strip()) # تحذف المسافات الفارغة من البداية والنهاية
#The lower() method returns the string in lower case:
print(name.lower())
#The upper() method returns the string in upper case:
print(name.upper())
#The replace() method replaces a string with another string:
print(name.replace("e", "i"))
#The split() method splits the string into substrings if it finds instances of the separator:
print(name.split(",")) 
#The center() method will center align the string, using a specified character (space is default) as the fill character
print(name.center(40)) # space
print(name.center(40, "*")) 
#The index() method returns the position at the first occurrence of the specified value.
print(name.index("a"))
#The find() method finds the first occurrence of the specified value.The find() method returns -1 if the value is not found
print(name.find("z"))
#Check String
text = "hello,Sanaa "
x = "naa" in text # مخزن داخلها هل القيمة صحيحة ام لا
print(x)
text = "hello,Sanaa "
x = "naa" not in text
print(x)
#String Format بنستخدم الميثود الجاهزة فورمات
name ="Ahmed"
age = 34
print("My name is {}".format(name))
print("My name is {}, and I am {} years".format(name ,age))
print(f"my name is : {name} and my age is {age}") # طريقة اخرى اسهل وافضل
#format floating point number
number =10.25478964
print("My number is {:.2f}".format(number))
# ممكن اتحكم بمكان المتغير بوضع قيمة الاندكس
a,b,c = "one" , "two","three"
print("numbers : {} {} {}".format(a,b,c)) # numbers : one two there
print("numbers : {1} {2} {0}".format(a,b,c)) # numbers : two there one
