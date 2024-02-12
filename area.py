import math as mt 

print("KEY IN THE REQUIRED VALUES SO AS TO GET THE TRIANGLE'S AREA")
hyp = int(input("Hypotenus: "))
base = int(input("Base: "))
height = int(input("height: "))

shape = (hyp + base + height)/2

area = mt.sqrt(shape*(shape-hyp)*(shape-base)*(shape-height))
print(f"The area of the triangle is: {area}")