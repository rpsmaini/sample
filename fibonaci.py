def fibo (n):
    a = 0
    b = 1

    print(a)
    print(b)
    
    for i in range(2,n):
        c = a+b
        a=b
        b=c
        print(c)
    
def mul_table(n):
    for i in range(1,11):
        print(n*i)

print("hello")
choice = input("which function to execute(f/m): ")
x = int(input("terms upto: "))
if(choice == 'f'):
    fibo(x)
else:
    mul_table(x)
print("hello")
input("press enter key to exit.")