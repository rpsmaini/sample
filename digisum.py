n=int(input("enter your number :"))
sum=0
while(n>0):
    sum += int(n%10) 
    n = int(n/10)
print(sum)        