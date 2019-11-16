
class Base1:pass
class Base4:pass
class Base5:pass
class Base2(Base4, Base5):pass
class Base3(Base1):pass
class MultiDerived(Base3, Base2):pass


class X:pass
class Y: pass
class Z:pass
class A(X,Y):pass
class B(Y,Z):pass
class M(B,A):pass
#In the multiple inheritance scenario, any specified attribute is searched first in the current class. If not found,
# the search continues into parent classes in depth-first, left-right fashion without searching same class twice.
print(MultiDerived.mro())
# output explanation
# 1. mdvd, b3, b2, b4, b5, b1, b5
# 2. simplify and remove repeated classes from left to right -> mdvd, b3, b2, b4, b5, b1

print(M.mro())
# output explanation
# 1. mbyzaxyz
# 2. simplify and remove repeated classes from left to right -> mbaxyz