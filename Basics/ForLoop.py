#   for loop
# for item in iterable_object :
#     Do sth with items
#-----------------------------------------------------------
myNum=[1,2,3,4,5,6,7,8,9]
for num in myNum:
    if num %2==0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
else:
    print("The loop is finished !")
#-----------------------------------------------------------
name = "Deema"
for letter in name:
    print(f"[ {letter.upper()} ]")
#-----------------------------------------------------------
mySkills={
    "Html":"50%",
    "Css":"60%",
    "PHP":"70%",
    "JS":"80%",
    "Python":"90%"
}
print(mySkills['JS'])
print(mySkills.get("Python"))
for skill in mySkills:
    print(skill)# print the key
    print(f"My progress in lang {skill} is: {mySkills[skill]}")# print the key and value
# طريقة اخرى تؤدي نفس الغرض وهي عن طريق استخدام ميثود
print(mySkills.items())
# dict_items([('Html', '50%'), ('Css', '60%'), ('PHP', '70%'), ('JS', '80%'), ('Python', '90%')])
for skill_key, skill_progress in mySkills.items():
    print(f"{skill_key} => {skill_progress}") # نفس الفكرة لطباعة العناصر مع قيمها
#-----------------------------------------------------------
# Nested loops
peoples={
    "Deema":{
         "Html":"60%",
         "Css":"80%",
         "PHP":"50%"
    },
    "Ali":{
         "Html":"50%",
         "Css":"60%",
         "PHP":"70%"
    },
    "Ahmad":{
         "Html":"90%",
         "Css":"70%",
         "PHP":"50%"
    }
}
print(peoples["Deema"])# لطباعة القيم المرتبطة فيه values
print(peoples["Deema"]['Css'])
for name in peoples: #بيمشي على المفتاح الرئيسي
    print(f"Skills and progress for {name} is:")
    for skill in peoples[name]:#كل عنصر لحاله يعني values for keys
        print(f"{skill.upper()} => {peoples[name][skill]}")
print("#"*50)
# طريقة اخرى اسهل في التعامل مع القاموس الجزئي من قاوس اخر كالتالي
for main_key, main_value in peoples.items():
        print(f"Skills and progress for {main_key} is:")
        for child_key, child_value in main_value.items():
            print(f"- {child_key} => {child_value}")

#-----------------------------------------------------------
# Break, Continue, Pass
nums =[1,2,3,5,7,10,13,14,15,19]
# Continue
for num in nums:
    if num==13:
        continue # skip on value
    print(num)
print("#"*50)
# Break
for num in nums:
    print(num)
    if num==13:
        break # stop the loop
print("#"*50)
# Pass
for num in nums:
    if num==13:
        pass # skip this and continue
    print(num)
print("#"*50)








