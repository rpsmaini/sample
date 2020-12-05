#enter a display message
print("welome to future money")
print()
choice = "y"
while choice.lower() == "y":
    #get input from the user
    monthly_investment = float(input("enter monthly investment:\t"))
    yearly_interest_rate = float(input("enter yearly interest rate:\t"))
    years = int(input("enter number of years:\t\t"))
    
    #convert yearly values into monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12
    
    #calculate future value
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount
    #display the result
        print("future value :t\t\t" + str(round(future_value, 2)))
        print()
    #end the programme
        
    choice = input("continue(y/n)?: ")
    print()

    print ("bye")
