'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''
import re

# This function takes in a line of text and returns a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

#1.  (7pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.  (read the file line by line to accomplish this task)
file = open('search_files/dictionary.txt')
all_words = []

for line in file:
    words = split_line(line)
    for word in words:
        all_words.append(word)

print(all_words)

lengths = [len(x) for x in all_words]
print(lengths)

print(max(lengths))

print(lengths.index(28))

print(all_words[2285])

#2.  (7pts)  Write code which finds
#  The total word count AND average word length of "AliceInWonderLand.txt"
file = open('search_files/AliceInWonderLand.txt')
all_words = []

for line in file:
    words = split_line(line)
    for word in words:
        all_words.append(word)

print("There are", len(all_words), "words.")

lengths = [len(x) for x in all_words]
print(lengths)



print(sum(lengths) / len(lengths))

# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (13pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?
file = open('search_files/dictionary.txt')
key = "CAT"
count = 0
count_2 = 0
key_2 = "CHESHIRE"

for i in range(len(all_words)):
    if all_words[i].upper() == key:
        count += 1
        if all_words[i - 1].upper() == key_2:
            count_2 += 1

print("The word 'cat' shows up", count, "times.")

print("The words 'cheshire' and 'cat' show up", count_2, "times.")

#### OR #####

#3  (13pts)Find the most frequently occurring 
#  seven letter word in "AliceInWonderLand.txt"

# CHALLNENGE PROBLEM  (for fun, not for credit).  
#  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.




