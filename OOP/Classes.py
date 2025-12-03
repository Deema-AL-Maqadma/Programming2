# clases
class Member:
    def __init__(self):
        print("A new member has been added")
Member() # لو عملت رن هيك بيكون انشات اوبجكت من الكلاس دون اي اضافات ويمكن الاشارة للاوبجكت بواسطة متغير
print(dir(Member)) #لطباعة محتويات الاوبجكت
print(dir(str)) # يحضر كل البيانات الخاصة بها والميثود
member1 =Member()
member2 =Member()
member3 =Member()
print(member1.__class__) # لاحضار الكلاس الخاص بهاد الاوبجكت يعني هاد الاوبجكت تابع لاي كلاس
#----------------------------------------------------------------------------
print("#"*50)
my_string ="Deema"
print(type(my_string))
print(my_string.__class__)
print(dir(my_string))
print("#"*50)
# كيفية تعامل البايثون مع الاوبجكت عن طريق مناداة على الكلاس ثم على الميثود داخله وبمرر الاوبجكت تبعي لهاي الميثود
print(str.upper(my_string))
#  dir()لمعرفة محتويات اي شي اي كلاس او اوبجكت نستخدم ميثود 
print(dir(str))
print("#"*50)




#----------------------------------------------------------------------------
class Skill:
    def  __init__(self):
        self.skills=["CSS","JS","Html"]
    
    def __str__(self):
        return f"This is my skill {self.skills}"

    def __len__(self):
        return len(self.skills)


profile = Skill()
# لمعرفة بيانات الاوبجكت في حال لم يكن هناك ميثود سترينغ يحضر تفاصيل تخزين الاوبجكت في الذاكرة
print(profile)
# لمعرفة الكلاس الذي ينتمي له هذا الاوبجكت
print(profile.__class__)
#لاحضار طول الوبجكت لازم اكون معرفة ميثود الطول داخل الكلاس ولا هيعطيني ايرور
print(len(profile))
# لو بدي اعدل على قيمة المجموعة الخاصة بالاوبجكت بالتالي التحديث للقيم تلقائيا
profile.skills.append("Python")
profile.skills.append("C#")
print(profile)
print(len(profile))


