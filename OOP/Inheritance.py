#  Inheritance
class Food:# Base class
    def __init__(self, name,price):
        self.name=name
        self.price=price
        print(f"{self.name} is ceated from Base class")

    def eat(self):
        print("Eat method from Base class")


class Apple (Food):# Derived class
    def __init__(self,name,price,amount):
        # over ride of Base class constructor
        #Food.__init__(self,name) #create instance from base class
        super().__init__(name,price) # تؤدي نفس الوظيفة دون الحاجة لكتابة اسم الكلاس
        self.amount=amount # صفة خاصة بالكلاس الابن اما باقي الصفات تمت وراثتها من الاب
        print(f"{self.name} is ceated from Derived class and price is {self.price} and amount is {self.amount}")

    def get_from_tree(self):
        print("Get from tree from derived class...")


     # Override نفس الميثود بنفس الاسم لكلا الكلاسين
    def eat(self):
        print("Eat method from Derived class")


#food1 = Food("Pizza",200) # عند التنفيذ ينفذ ما بداخل الكونستركتر
food2 = Apple("Pizza",150,400) # ينفذ الكونستركتر للاب ثم الكونستركتر للابن
food2.eat()
food2.get_from_tree()
#--------------------------------------------------------------------------------------------
# Multipe Inheritance
class BaseOne:
    def __init__(self):
        print("Base One")

    def func_one(self):
        print("ONE")
class BaseTwo:
    def __init__(self):
        print("Base Two")

    def func_Two(self):
        print("Two")

class Derived(BaseOne, BaseTwo):
    pass
# method reselution order توضح ترتيب الوراثة من الكلاسات
print(Derived.mro())
my_obj = Derived()
# يحدد الكلاس سلس جاي منها الميثود
print(my_obj.func_one)
print(my_obj.func_Two)
# ينفذ الميثود للاوبجكت
my_obj.func_one()
my_obj.func_Two()
#--------------------------------------------
class Base:
    pass

class DerivedOne(Base):
    pass

class DerivedTwo(DerivedOne): # Base & DerivedOne عنده خاص كلا الكلاسين 
    pass




