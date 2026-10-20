A = int(input("Enter a number: "))
B = int(input("Enter second number: "))
C = int(input("Enter third number: "))

if (A%2 == 0):
    print("A is even")
if (B%2 == 0):
    print("B is even")
if (C%2 == 0):
    print("C is even")

if (A > B and A > C):
    print("A is the largest number")
elif  (B > C):
    print("B is the largest number")
else:
    print("C is the largest number")

if (A%7 ==0):
    print("First number is divisible by 7")
else:
    print("First number is not divisible by 7")