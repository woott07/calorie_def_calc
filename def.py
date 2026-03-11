# BMR Calculator

gender = input("Enter M for Man, W for Woman: ")
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
age = float(input("Enter your age: "))
print("for Easy Fatloss enter 1")
print("for Moderate Fatloss enter 2")
print("for Hard Fatloss enter 3")
target = input("Enter your target: ")
if gender == "M":
    bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
    print("Your BMR is:", bmr)
elif gender == "W":
    bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
    print("Your BMR is:", bmr)
else:
    print("Invalid input")
TDEE = ("Weekly Training")
print(TDEE, "0x 1x 2x 3x 4x 5x 6x 7x 14x")
training = input("Enter your training level: ")
if training == "0x":
    tdee = bmr * 1.2
if training == "1x":
    tdee = bmr * 1.375
if training == "2x":
    tdee = bmr * 1.55
if training == "3x":
    tdee = bmr * 1.725
if training == "4x":
    tdee = bmr * 1.9
if training == "5x":
    tdee = bmr * 2.2
if training == "6x":
    tdee = bmr * 2.4
if training == "7x":
    tdee = bmr * 2.6
if training == "14x":
    tdee = bmr * 2.8
print("Your TDEE is:", tdee)
if target == "1":
    defi1 = tdee - 500
    print("Your Deficit is:", defi1)
if target == "2":
    defi2 = tdee - 750
    print("Your Deficit is:", defi2)
if target == "3":
    defi = tdee - 1000
    print("Your Deficit is:", defi)
