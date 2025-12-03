# Static 
class Member(): # لو ضغطت على اسم الكلاس على الاشارة البرتقالية تظهر كل الانستنس الاوبجكت من هذا الكلاس
    # class atributes
    not_allowed_names=["Hell","Shet","Baloot"]
    users_num = 0

    # class method
    @classmethod
    def show_users_count(cls):
        print(f"We have {cls.users_num} users in our system ")

    # static method
    @staticmethod
    def say_hello():
        print("--->>> Hello from static method...")


    def __init__(self,first_name,middle_name,last_name,gender):
        # instanse atributes
        self.fname=first_name
        self.mname=middle_name
        self.lname=last_name
        self.gender=gender
        Member.users_num+=1

    def full_name(self):
        # لازم احدد اسم الكلاس يلي فيه هاي الصفة لانها مربوطة بالكلاس وليس الاوبجكت
        if self.fname in Member.not_allowed_names:
            raise ValueError("Name Not Allowed...")
        else:
            return f"{self.fname} {self.mname} {self.lname}"
    
    def  name_with_title(self):
        if self.gender=="Male":
             return f"Hello MR {self.fname}"
        elif self.gender=="Female":
             return f"Hello Miss {self.fname}"
        else:
            return f"Hello {self.fname}"
        
    def get_all_info(self):
        return f"{self.name_with_title()}, Your full name is: {self.full_name()}"
    def delete_user(self):
        Member.users_num-=1
        return f"User {self.fname} Deleted..."
    

print(Member.users_num)
member_one = Member("Deema","Mohammed","AL-Maqadma","Female")
member_two = Member("Ahmed","Mohammed","AL-Maqadma","Male")
print(member_one.get_all_info())
print(member_two.get_all_info())
print(Member.users_num)
print(member_two.delete_user())
print(Member.users_num)
print("#"*50)
Member.show_users_count()
print("#"*50)
#كيف يتم تنفيذ الميثود لاوبجت معين من الكلاس وكيف البايثون يتعامل خلف الكواليس
print(member_one.full_name())
print(Member.full_name(member_one))
print("#"*50)
Member.say_hello()
print("#"*50)



#-------------------------------------------------------------------------
