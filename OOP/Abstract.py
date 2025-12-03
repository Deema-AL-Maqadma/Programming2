# Abstract Base Class
from abc import ABCMeta, abstractmethod
class Programming(metaclass=ABCMeta):
    @abstractmethod
    def has_oop(self):
        pass
    # no abstractmethod so dosnot have be in the objects
    def has_name(self):
        pass
class Python(Programming):
    # لازم اعمل override للميثود لانها abistract
    def has_oop(self):
        return "Yes"
class Pascal(Programming):
    def has_oop(self):
        return "NO"

# one = Programming()لا يمكن عمل اوبجكت من الكلاس الابستراكت
one = Python()
print(one.has_oop())
two = Pascal()
print(two.has_oop())

