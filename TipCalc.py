#Tip Calculator

#welcome message
print("Tip Calculator")

#total of bill
bill = float(input("What was the total bill?: $"))

#What tip do you want to give?
tip_question = int(
    input("What percentage tip would you like to give? 10, 12, or 15?: "))
tip_percentages = {10: 0.1, 12: 0.12, 15: 0.15}

tip_value = tip_percentages.get(tip_question)
tip_add = bill * tip_value

#how many people to split the bill?
people = int(input("How many people are going to split the bill?: "))

# the amount needed for each person
single_account = (bill + tip_add) / people

print(single_account)