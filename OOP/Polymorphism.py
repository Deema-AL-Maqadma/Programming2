# Polymorphism ميثود متعددة الاوجه و لها نفس الاسم لكن تؤدي مهام متعددة ومختلفة في كل مرة
n1 =2
n2 =4
print(n1+n2)
s1="DEEMA"
s2="MAQADMQ"
print(s1+" "+s2)
# نفس الميثود باماكن مختلفة ونتائج مختلفة
print(len([1,2,3,4,5,6]))
print(len("Deema AL-Maqadma"))
print(len({"Key_one":1,"Key_two":2}))
#-------------------------------------------------------------------------------
class A:
    def DO_STH(self):
        print("from class A ")
        raise NotImplementedError("Derived class must Implement this method...")
class B(A): # inheritanse
    def DO_STH(self):
        print("from class B ")
class C(A): # inheritanse
    def DO_STH(self):
        print("from class C ")

my_instancre= B()
my_instancre.DO_STH() # يوجد وراثة بالتلاي يصل لمحنويات كلاس الاب عند وجود نفس الميثود عند كلاهما تنفذ ما عند الابن
my_instancre2= C()
my_instancre2.DO_STH()


