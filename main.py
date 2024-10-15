import art

#Add header / greeting
print(art.logo)
print("Welcome to the Tip Calculator!")
print("To calculate your tip total, please answer the following questions.")

#Create variables for calculating
total_bill = int(input("How much was your total bill? $"))
tip_percentage = int(input("How much tip% would you like to give? 10, 15, or 20? "))
num_people = int(input("How many people to split the bill? "))

#Calculate tip amount
bill_due = round(((total_bill * (tip_percentage / 100 + 1)) / num_people), 2)

print("Each person will pay $" + str(bill_due))
