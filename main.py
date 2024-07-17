#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
original_bill = float(input("How much was the total bill? $"))
tip_percentage = int(input("How much would you like to tip? E.g., 10, 15?"))
num_people = int(input("How many people will split the bill?"))
total_bill = original_bill * (tip_percentage / 100 + 1)
per_person = round(total_bill / num_people, 2)
print(f"Each person will pay ${per_person}")