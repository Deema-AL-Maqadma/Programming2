# Encapsulaton / restrict access to the data stored in attributes and methods
# public
class Member:
    def __init__(self,name):
        self.name=name
one = Member("Deema")
print(one.name)
# يمكن التعديل على قيمتها بكل سهولة من خارج الكلاس
one.name="Ali"
print(one.name)
#-----------------------------------------------------------------------
# protected
class Member:
    def __init__(self,name):
        self._name=name
one = Member("Deema")
print(one._name)
# يمكن التعديل على قيمتها بكل سهولة من خارج الكلاس
one._name="Ali"
print(one._name)
#-----------------------------------------------------------------------
# private
class Member:
    def __init__(self,name):
        self.__name=name

    def say_hello(self):
        return f"Hello {self.__name}"
    
    def get_name(self): # Getter
        return self.__name
    
    def set_name(self,new_name): # Setter
        self.__name= new_name

one = Member("Deema")
print(one.say_hello())

#print(one.__name) #لا يمكن طباعتها كالتالي لانها خاصة
# يمكن طباعة والوصول للصفة المعرفة خاصة من خلال التالي
print(one._Member__name)
# لا يمكن التعديل على قيمتها بكل سهولة من خارج الكلاس
#one.__name="Ali"
# لكن يمكن من خلال التالي الوصول لها والتعديل على قيمتها
one._Member__name = "ZAIN"
print(one._Member__name)
print(one.get_name())
one.set_name("Omar")
print(one.get_name())
#------------------------------------------------------------------------------------
print("#"*50)
class Member:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say_hello(self):
        return f"Hello {self.name}"
#لما يكون عندي ميثود ترجع قيمة ولا تاخذ بارارميتر سوى سيلف يمكن استخدامها في جملة الطباعة كصفة وليس كميثود واذلك من خلال وضع @ بروبيرتي بالتالي يتعامل معها كصفة وليس ميثود
    @property
    def age_in_days(self):
        return self.age*365
    
one = Member("Deema",19)
print(one.name)
print(one.age)
print(one.say_hello()) # method
print(one.age_in_days) # attribute