from math import sin, log, sqrt, pow

u = int(input("U >>> "))
y = int(input("Y >>> "))
x = int(input("X >>> "))

T = sin(2*u)*log(2*pow(y, 2)+sqrt(x))

print("Natija: ", T)
