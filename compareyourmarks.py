#enter display message
usr_name = input("enter your name  :")
print ("welcome ," + usr_name)

#enter input from user
aA = int(input("enter your marks of maths  :"))
bB = int(input("enter your marks of chemistry  :"))
cC = int(input("enter your marks of pysics  :"))
dD = int(input("enter your marks of IT  :"))
#conditoning
f = 0 #initialising
if aA < 60:
    print("got less marks in maths ")
if bB < 60:
    print ("got less marks in chemistry")
    f=1
if cC < 60:
    print ("got less marks in physics")
    f=1
if dD < 60:
    print ("got less marks in IT")
    f=1
if f==0:
    print(" got good marks in all subjects ")
#end the programme
print ("bye ," + usr_name)
input("press enter to exit")
