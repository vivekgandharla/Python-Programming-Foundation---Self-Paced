import sys
print('''
Select your gender:
        1. Male
        2. Female
''')
gender = int(input("Select your gender (1 or 2): "))
if gender not in (1, 2):
    print("Invalid input")
    sys.exit()

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
age = int(input("Enter your age in years: "))

if gender == 1:
    # BMR calculation for males
    bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
else:
    # BMR calculation for females
    bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

print("Your BMR is:", bmr)