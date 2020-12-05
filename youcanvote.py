#enter display message
print("welcome to YOU CAN VOTE program")
#enter input from user
usr_name = str(input("enter your nationality  :"))
usr_age = int(input("enter your age  :"))
usr_anti = str(input("are you anti nationalist ?  : (y/n)"))

# using condition
if usr_name =="indian" and usr_age >= 18 and usr_anti == "n":
               print("you can vote")
elif usr_age <= 18 and usr_name =="indian":
    print ("wait till 18")
else:
    print("you cannot vote")
#end the program
input("press enter to exit")                    
                    

