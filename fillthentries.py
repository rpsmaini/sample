#this program is made with iteration
i = int(input("enter the number of enteries you want to fill   :"))
while i > 0:
    usr_name = str(input("enter your name   :"))
    print("hello " + usr_name + " enter your marks as directed")
    usr_p = int(input("enter your marks of physics  :"))
    usr_c = int(input("enter your marks of chemistry  :"))
    usr_m = int(input("enter your marks of maths  :"))
    i -= 1
    if i == 0:
        print("all entries are filled")
        input("press enter to exit")

