# While loop
# while conditionis true
# code will run until condition become false
#--------------------------------------------------------
a=0
while a<5:
    print(a)
    a+=1
else:# جملة تنفذ بعد انتهاء اللوب
    print("Loop is Done !")
#--------------------------------------------------------
myf=["Deema","Ali","Ahmad","Zain"]
a=0
while a<len(myf):#لوب على عناصر الليست حتى يطبع كل العناصر فيها
    # الندكس يبدا من صفر بالتالي يكون الترتيب +1 والناتج بحوله لنص وبعبي الطول اصفار حسب الطول يلي بدي ياه 
    print(f"{str(a+1).zfill(2)} {myf[a]}")
    a+=1
else:
    print("All Frind printed on screen...")
#--------------------------------------------------------
myFavouriteWebs=[] # Empty list to fill later
maximumWebs= 5 # maximum allowed Webs
while maximumWebs>0:
    web=input("Website name without http:// :")# input the new website to the list
    myFavouriteWebs.append(f"https://{web.strip().lower()}")# Add to list
    maximumWebs-=1 # Decrease
    print(f"-> Website Added, {maximumWebs} places left .")
    print(myFavouriteWebs)
else:
    print("All websites prented...")
# Chek if the list not empty
if len(myFavouriteWebs)>0:
    myFavouriteWebs.sort()
    index=0
    print("---> My Websites: ")
    while index< len(myFavouriteWebs):
        print(myFavouriteWebs[index])
        index+=1
#--------------------------------------------------------
tries = 4
mainPassword = "Deema@123"
inputPassword= input("Write your password :")
while inputPassword!= mainPassword:
    tries-=1
    print(f"Wrong Password, {'last' if tries==0 else tries} chance left .")
    inputPassword= input("Write your password :")
    if tries==0:
        print("All tries is Finished.")
        break
        print("Will not print...")






