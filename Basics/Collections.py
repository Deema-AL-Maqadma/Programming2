
#Python Lists
mylist=[3,5,6,8,4,2,1,9,57,3,4,4]
print(mylist)
mylist.append(78)
print(mylist)
print(mylist.count(4))
print(mylist)
mylist.insert(4,6)
print(mylist)
mylist.remove(57)
print(mylist)
print(mylist.pop())
print(mylist)
mylist.reverse()
print(mylist)
mylist.sort()#3 تعدل بشكل مباشر
print(mylist)
mylist.sort(reverse=True)#ترتب تنازلي
print(mylist)
mylist2=sorted(mylist)#ترتب الليست فليست اخرى
print(mylist2)
mylist2.reverse()#تعكس الليست
print(mylist2)
mylist.clear()
print(mylist)
#----------------------------------------------------------------
#Python Tuples
mytuble=(1,2,3) #لانشاء تبل اما باسناد قيم مباشرة
mytuble= tuple((1,2,3)) #او من خلال الكونستركتر ويقبل ارقيمنت واحد بحيث لازم احط اقواس التبل داخل الكونستركتر
print(mytuble)
print(len(mytuble))
print(mytuble[-3:-1])
if 2 in mytuble:
    print("True")
#لا يمكن التعديل على التبل لكن بطريقة غير مباشرة عن طريق انشاء ليست تحتوي على عناصر التبل واعدل على الليست ثم ارجع اسند الليست للتبل
mylist=list(mytuble)
print(type(mylist)) #نوعها ليست
mylist[1]=5
print(mylist)
mytuble=tuple(mylist) # ينشئ تبل من الليست يلي عملناها
print(mytuble)
mytuble2 =(1,4,7,8,9)
mytuble3 = mytuble + mytuble2 # لدمج اكثر من تبل ويقبل التكرار
print(mytuble3) 
print(mytuble3.count(1)) #لحساب تكرار القيمة للعنصر
print(mytuble3.index(5))# لاحضار موقع العنصر في التبل
#----------------------------------------------------------------
#Python Sets
myset={10,20,30,40}
print(myset) #في كل مرة يطبع بترتيب مختلف
print(len(myset)) #لايجاد طول المجموعة
#ما بقدر اتعامل مع عنصر محدد لعم وجود اندكس للعناصرولا يمكن حذف عنصر محدد لكن يمكن اضافة عنصر على الست كالتالي
myset.add(50) #لاضافة عنصر واحد
print(myset)
myset.update((60,70,80))
print(myset)
myset.update((60,70,80,70,30,20))# عند طباعتها يتم حذف التكرار كله تبقى عناصر فريدة فقط
print(myset)
# لحذف عنصر معين في الست من خلال عدة دوال كالتالي
myset.remove(30)#في حال كان العنصر غير موجود بيعطيني ايرور وبيوقف البرنامج
print(myset)
myset.discard(90)# في حال كان العنصر غير موجود يكمل بشكل طبيعي
print(myset)
print(myset.pop())#تحذف عنصر بشكل عشوائي
print(myset)
myset.clear()# لتفريغ الست من العناصر
print(myset)
del myset#لحذف الست نفسها تصبح غير موجودة
# لدمج اكثر من ست معا كالتالي
myset1 = {1,2,3}
myset2 ={4,5,6}
print(myset1.union(myset2))
print(myset1 | myset2)# اتحاد عناصر الاولى والثانية
myset1.update(myset2)# تحديث على الست الاولى واضافة الست الثانية لها
myset1.update({4,5,6})# نفس الطريقة
print(myset1)
myset1=set({55,44,33})
print(myset1)
myset2=myset1.copy()#نسخ القيم
print(myset2)
print("********************************************")
set1={2,4,3,5,6}
set2={4,7,8,6,3}
print(set1.difference(set2))# تطبع كا هو موجود عند الاولى فقط
print(set1.intersection(set2))#تطبع العناصر المشتركة
set1.intersection_update(set2)#العناصر المشتركة حطها للمجموعة الاولى
print(set1)
print(set1.symmetric_difference(set2))#العناصر الغير مشتركة في المجموعتن
set2.symmetric_difference_update(set1)#عدل على المجموعة الثانية واسندلها عناصر الغير مشتركة
print(set2)
set1.difference_update(set2) #ناتج الافلرق بينهم حدث على المجموعة الاولى بقيم الديفيرنس السابق
print(set1)
print(set1.isdisjoint(set2))#تفحص هل المجموعتين ليس فيهم عناصر مشتركة
print(set1.issuperset(set2)) #هل المجموعة الثانية جزئية من الاولى
print(set1.issubset(set2)) # هل الاولى جزئية من الثانية
#-------------------------------------------------------------------------------------------------------------------------
# Python Dictionaries
mydic={
    "name":"Ahmad",
    "age":19,
    "city":"Gaza",
    "name":"Deema"#update the value of key name الان يتعامل مع القيمة الحديثة 
}
print(mydic)
print(len(mydic))
mydic.update({"tal":175,"hair":"black"})#تحديث على القاموس كله بالتالي يتم اضافة القيم الجديدة له
print(mydic)
print(len(mydic))
#Access dictionary Items 
print(mydic["name"])
print(mydic.get("name"))
#للتعديل على قيمة العنصر بناء على المفتاح
mydic["age"]=20 #Change Values
print(mydic)
# Add Items/Adding an item to the dictionary is done by using a new index key and assigning a value to it:
mydic["ID"] = "4776984"
print(mydic)
#Remove Items 
mydic.pop("name")#لازم امررلها قيمة الكي يلي هحذفه
print(mydic)
mydic.popitem()#تحذف اخر عنصر تم اضافته في القاموس
del mydic["age"]#ممكن من خلالها احذف عنصر او احذف القاموس كاملا
print(mydic)
mydic.clear()# تفرغه من العناصر
# لعمل نسخة من القاموس يوجد عدة طرق
mydic2=mydic.copy()
mydic2=dict(mydic)
print(mydic2)
#Nested Dictionaries(two dimentional) A dictionary can also contain many dictionaries, this is called nested dictionaries.Create a dictionary that contain three dictionaries:
students ={
 "std1": {"name":"wafaa" ,"age":10},
 "std2": {"name":"ahmed" ,"age":12},
 "std3": {"name":"ali" ,"age":15}
}
print(students['std1']['age']) # 10
#The dict() Constructor It is also possible to use the dict() constructor to make a new dictionary:
mydict = dict(name="ahmed",age="15")
print(mydict)
print(mydict.values())
print(mydict.keys())
print(mydict.items())
#لانشاء قاموس من قيم معينة
names=("Deema","Ali","Omar")
age=20
print(dict.fromkeys(names,age))
