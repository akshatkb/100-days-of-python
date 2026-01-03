welcomeMsg = "Welcome to the tip calculator!"
print(welcomeMsg)
amt = int(input("What was the total bill? $"))
totalAmt = amt * (int(input("How much tip would you like to give? 10, 12, or 15? "))/100 + 1)
people = int(input("How many people to split the bill? "))

# print(tipPercent)
eachPersonBill = round((totalAmt /people), 2)
print(f"Each person should pay ${eachPersonBill}")