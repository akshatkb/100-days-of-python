height = input("How tall are you in meter ?")
weight = input("How much do you weight in kilograms ?")

bmi = int(weight) / float(height) ** 2
print(f"Your BMI is: {bmi}")