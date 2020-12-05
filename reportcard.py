#welcome
usr_name = input("enter your name  :")#prog1
print ("welcome ," + usr_name)
#prog2
print("enter your test scores")
print("=======================")

# get scores from the user and accumulate the total
total_score = 0        # initialize the variable for accumulating scores
total_score += int(input("enter test score: "))
total_score += int(input("enter test score: "))
total_score += int(input("enter test score: "))
total_score += int(input("enter test score: "))
total_score += int(input("enter test score: "))
total_score += int(input("enter test score: "))

# calculate average score
average_score = round(total_score / 6)

# format and display the result
print("=======================")
print("Total Score: ", total_score,
      "\nAverage Score:", average_score)
