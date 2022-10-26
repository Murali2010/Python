#circle_rectangle.py
import circleModule
import rectangle
#importing user defined modules

r=int(input("Enter radius"))

#using cirlceModule

a = circleModule.area(r)
c = circleModule.circumference(r)

print(a)
print(c)

#using rectangle module

l=float(input("Enter length"))
b=float(input("Enter breadth"))

ar=rectangle.area(l,b)
cr=rectangle.circumference(l,b)
print(ar)
print(cr)
