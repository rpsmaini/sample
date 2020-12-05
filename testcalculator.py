# display a title
print("the test calculators")
print()
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
average_score = round(total_score / 5)

# format and display the result
print("=======================")
print("Total Score: ", total_score,
      "\nAverage Score:", average_score)
print()
print("bye")
input("press enter key to exit")
