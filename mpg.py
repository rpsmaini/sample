# display a welcome message
print("the miles per gallon program")
print()

# get input from the user
miles_driven = float(input("enter miles driven:         "))
gallons_used = float(input("enter gallons of gas used:  "))

if miles_driven  <= 0:
    print("miles driven must be greater than zero. please try again.")
elif  gallons_used <= 0:
        print ("gallons must be greater than zero. please try again.")
else:
            # calculate and display miles per gallon
            mpg = round((miles_driven / gallons_used), 2)
            print("miles per gallon:          ", mpg)
            print()
            print("bye")
            input("press enter key to exit")
            
