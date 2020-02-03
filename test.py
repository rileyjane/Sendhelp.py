print(
    "Hello, welcome. This program will ask you to input your grade and based on the number inputed, will inform you "
    "of your letter grade")

number_grade = int(input("Please enter test score:"))

if number_grade >= 90:
    print("You received an A on the test! Congrats!")
elif 80 <= number_grade < 90:
    print("You received a B on the test!")
elif 70 <= number_grade < 80:
    print("You received a C on the test")
else:
    print("You failed the test")


