

## WAP to find Maximum among given 5 number??




num1=int(input("Enter The 1st Number: "))
num2=int(input("Enter The 2nd Number: "))
num3=int(input("Enter The 3rd Number: "))
num4=int(input("Enter The 4th Number: "))
num5=int(input("Enter The 5th Number: "))
if num1>num2 and num1>num3 and num1>num4 and num1>num5:
    print("num1 Maximum")
elif num2>num3 and num2>num4 and num2>num5:
    print("num2 is maximum")
elif num3>num4 and num3>num5:
    print("num3 is maximum")
elif num4>num5:
    print("num4 is maximum")
else:
    print("num5 is maxuimum")

