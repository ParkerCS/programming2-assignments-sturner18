# LOOPS (16pts TOTAL)
# Simone Turner

# PROBLEM 1 (Fibonacci - 4pts)
## The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again.
# Every next number is the sum of the two previous numbers.
# I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,...
# Write a program that calculates and prints the Fibonacci sequence
# until the numbers get higher than 1000.

num1 = 1
num2 = 1
num3 = 2

print(num1)
print(num2)

for i in range(1, 1001):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    if num3 > 1000:
        break
    print(num3)

# PROBLEM 2 (Dice Sequence - 6pts)
# You roll five six-sided dice, one by one.
# What is the probability that the value of each die
# is greater than OR EQUAL TO the value of the previous die that you rolled?
# For example, the sequence “1, 1, 4, 4, 6” is a success,
# but “1, 1, 4, 3, 6” is not. Determine the
# probability of success using a simulation of a large number of trials.

from random import *
success = 0
for i in range(2000):
    roll1 = randrange(0, 7)
    roll2 = randrange(0, 7)
    if roll2 >= roll1:
        roll3 = randrange(0, 7)
        roll4 = randrange(0, 7)
        if roll4 >= roll3 and roll3 >= roll2:
            roll5 = randrange(0, 7)
            roll6 = randrange(0, 7)
            if roll6 >= roll5 and roll5 >= roll4:
                success += 1
                print("\n", roll1, "\n", roll2, "\n", roll3, "\n", roll4, "\n", roll5, "\n", roll6)

print("Success = {}".format(success))
probability = success / 2000
print("Probability = {:.2f}%".format(probability * 100))

# PROBLEM 3 (Number Puzzler - 6pts)
# A, B, C, and D are all different digits.
# The number DCBA is equal to 4 times the number ABCD.
# What are the digits?
# Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero.
# Use a quadruple-nested loop to solve.


for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            for d in range(1, 10):
                num = str(a) + str(b) + str(c) + str(d)
                num_reverse = str(d) + str(c) + str(b) + str(a)
                if int(num_reverse) == ((int(num) * 4)):
                    print("Answer: {} and {}".format(num, num_reverse))
