#FUNCTIONS AND IMPORTS (20PTS TOTAL)
# Be sure to comment all your functions as shown in notes
import import_me
#PROBLEM 1 (how many upper case - 4pts)
# Make a function takes a string as a parameter, then prints how many upper case letters are contained in the string.
# A loop that compares each letter to the .upper() or .lower() of itself will suffice.

def letters(word, uppercase = 0):
    uppercase = 0
    for i in word:
        if i != i.lower():
            uppercase += 1

    print("Uppercase =", uppercase)

letters("HeLLo WorLD")

# PROBLEM 2 (Biggest, smallest, average - 4pts)
# Make a function which takes 3 numbers as parameters.
# The function then prints the largest, the smallest, and their average, rounded to 2 decimals.
# Display the answers in a "nicely" formatted way.

def number(num1, num2, num3):

    largest = max(num1, num2, num3)
    print("Largest number =", largest)

    smallest = min(num1, num2, num3)
    print("Smallest number =", smallest)

    average = (num1 + num2 + num3) / 3
    print("Average = {:.2}".format(average))

number(4, 6, 8)


# PROBLEM 4 (add me, multiply me - 4pts)
# Make a function which takes in two integers and RETURNS their sum AND their product.
def sum_product(num1, num2):
    sum = num1 + num2
    product = num1 * num2
    return sum, product

print(sum_product(3, 4))

# PROBLEM 5 (Login - 4pts)
# Make a file called import_me.py in this same project
# Inside this new module/file, make a login function which works according to the flow diagram PasswordFlowchart.png in this folder
# Substitute your name for Rohan's, and use whatever generic password you want.

import_me.information("Simone Turner", "HappyCoding")

# PROBLEM 6 (main - 4pts)
# import the file import_me from Problem 5
# Create a main program using the format if __name__ == "__main__": 
# Place every call from problems 1 through 5 into this program.

