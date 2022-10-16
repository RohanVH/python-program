# demonstrate quadratic equation program
from math import sqrt
print("Quadratic equations")
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
r=b**2-4*a*c
if r>0:
    x1=((-b)+sqrt(r)/(2*a))
    x2=((-b)+sqrt(r)/(2*a))
    print(f"the roots are real and distinct{float(x1)} and {float(x2)}")
elif r==0:
    x=(-b)/(2*a)
    print(f"the roots are real and equal {x}")
else:
    part1=(-b)/(2*a)
    part2=(-r)/(2*a)
    x1=complex(part1,part2)
    x2=complex(part1,part2)
    print("both roots are imaginary\n the roots are %f and %f",(x1,x2))