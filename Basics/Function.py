# Function/ is a reusable block of code do a task
def function_name():
    print("The statement inside method...")
function_name() # call the function name to run the code
#---------------------------------------------------------------------
# def                      => function keyword [Define]
# say_hello()              => function Name
# name                     => Parameter
# print(f"Hello {name}")   => Task
# say_hello("Deema")       => Deema is the argument

def say_hello(name):
    print(f"Hello {name}")
say_hello("Deema")
#---------------------------------------------------------------------
def addition(n1,n2):
    if type(n1)!= int or type(n2)!=int:
        print("Only Integers Allowed...")
    else:
        print(f"-> Result = {n1+n2}")
addition(10,50)
#---------------------------------------------------------------------
def full_name(first,middel,last):
    print(f"Hello {first.strip().capitalize()} {middel.upper():.1s} {last.capitalize()}")
full_name("    Deema  ","mohammed","al-maqadma")
#---------------------------------------------------------------------
def say_hello(*peoples): #عدد غير محدد من الارقيمنت يتعامل معهم كلهم
    for name in peoples:
        print(f"Hello {name}")
say_hello("Deema","Omar","Ahmed")
#---------------------------------------------------------------------
def show_details(name,*skills):# جيدة للتعامل في حال عدم معرفة عدد الارقيمنت
    print(f"Hello {name} ypur skills is :")
    for skill in skills:
        print(skill)
# نفس الميثود للتعامل معها بعدد مختلف من القيم
show_details("Deema","js","css","html","python")
show_details("Ahmed","data since","js","css","html","python")
#---------------------------------------------------------------------
# function default parameters
# وضع قيم افتراضية للمتغيرات في حال لم يدخلها المستخدم وتكون القيمة الافتراضية اخر الارقيمنت كلها في حال كانت اول صفة الها قيمة افتراضية بالتالي يجب وضع قيم افتراضية لباقي المتغيرات حتى لا يعطيني ايرور او تبديل مكان الصفة لاخر ارقيمنت
def say_hello(name,age,country="Unknoun"):
    print(f"Hello {name} ,Your age is {age} and your country is {country}")
say_hello("Deema",19,"Palistine")
say_hello("Ahmed",20)











