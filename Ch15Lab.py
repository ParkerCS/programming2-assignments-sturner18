# SIMONE TURNER

import re
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

dictionary = open('search_files/dictionary.txt')

dictionary_list = []
for line in dictionary:
    words = split_line(line)
    for word in words:
        dictionary_list.append(word)
print(dictionary_list)

print(" --- Linear Search --- ")


alice_in_wonderland = open('search_files/AliceInWonderland200.txt')


def linear_search(key, dictionary_list, line_count):
    i = 0
    while i < len(dictionary_list) and dictionary_list[i] != key:
        i += 1

    if i < len(dictionary_list) - 1:
        pass

    else:
        print(key, "on line", line_count, "is not in the dictionary.")

line_count = 0
for line in alice_in_wonderland:
    words = split_line(line)
    line_count += 1
    for word in words:
        linear_search(word.upper(), dictionary_list, line_count)


alice_in_wonderland.close()


print(" --- Binary Search ---" )

alice_in_wonderland = open('search_files/AliceInWonderland200.txt')

def binary_search(key, dictionary_list):

    lower_bound = 0
    upper_bound = len(dictionary_list) - 1
    found = False

    while lower_bound <= upper_bound and not found:
        middle_pos = (upper_bound + lower_bound) // 2
        if dictionary_list[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif dictionary_list[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True

    if not found:
        print(key, "on line", middle_pos, "is not in the dictionary.")

for line in alice_in_wonderland:
    words = split_line(line)
    for word in words:
        binary_search(word.upper(), dictionary_list)