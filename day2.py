#Data Types

#String

# print("Hello" [0])


# Integer

# print(123 + 345)

# print(123_456_789)

#Float

# 3.14159
# print(3.14159)

# Boolean

# True
# False


### Day 2 len num_char type error type checking type conversion

# num_char = len(input("What is your name?"))

# newNumChar = str(num_char)

# print("Your name has " + newNumChar + " characters.")
# print(type(num_char))

# a = float(123)
# print(type(a))

## code challenge: combine two digits in a number to add them ex 35 = 3 + 5 = 8\

# two_digit_number = input("Type a two digit number: \n")

# letterOne = two_digit_number[0]
# letterTwo = two_digit_number[1]

# numberOne = int(letterOne)
# numberTwo = int(letterTwo)

# print(numberOne + numberTwo)


#### BMI INDEX ####

# height = input("enter your height in feet: ")
# weight = input("enter your weight in pounds: ")

# BMI = float(weight) / float(height) ** 2
# print (int(BMI))



### Rounding numbers, integers, float ####

# print(round(8/3))

# print(round(8/3, 2))

# print(8/3)
# print(8//3)

# += -= /= *=

#f-String
# score = 0
# height = 1.8
# isWinning = True
# print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

### Day 2.3 Exercise ###

# age = input("What is your current age?")

# ageInt = int(age)

# years = 90 - ageInt
# days = years * 365
# weeks = years * 52
# months = years * 12

# print(f"You have {days} days, {weeks} weeks and {months} months left.")


### Day 2 Final Project ####
print("Welcome to the tip calculator")

bill = input("What was the total bill? ")
percentageTip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

percentTip = int(percentageTip) / 100

endTip = float(bill) * percentTip

endBill = float(endTip) + float(bill)

split = int(endBill) / int(people)

# finalSplit = round(split, 2)
finalSplit = "{:.2f}".format(split)

print(f"Each person should pay ${finalSplit}")

