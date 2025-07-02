import math 

side1 = int(input('Enter 3 integers, enter the First: '))
side2 = int(input('Second:'))
side3 = int(input('Third: '))

s = (side1+side2+side3)/2
print(s)

print(math.sqrt(s * (s - side1) * (s - side2) * (s - side3)))