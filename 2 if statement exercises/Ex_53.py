# program that reads the rating of a particular employee and calculates their
# yearly raise based on their rating. ony scores of 0.2, 0.4, 0.6 and higher
# can be used #

# prompting user input for name and rating.
name = input("Please enter the employee's name: ")
rating = float(input("Please enter the yearly rating (either 0.0, 0.4 or >= 0.6)\
 for this employee: "))
# Setting conditions for a correct rating input (disallowing intermediate scores
# between those instructed).
if rating == 0.0 or rating == 0.4 or rating >= 0.6:
    # Assigning performance reviews to scores
    if rating == 0.0:
        performance = "an unacceptable performance"
    elif rating == 0.4:
        performance = "an acceptable performance"
    elif rating >= 0.6:
        performance = "a meritous performance"
        # Calculating raise if applicable
    salary_inc = rating * 2400
    # Displaying output
    print("%s has had %s and therefore deserves a raise calculated at $%.2f" \
     % (name, performance, salary_inc))
    # Displaying message for an invalid score input
else:
    print("Please enter a correct rating score; either 0.0, 0.4 or >= 0.6 .")
