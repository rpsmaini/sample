a=int(input("enter your number:"))
b=int(input("enter your number:"))

def getStep(num1, num2):
    return 1 if (num1 < num2) else -1

skip = getStep(a, b)
for num in range(a, b+skip, skip):
    print(num)