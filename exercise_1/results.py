#!/usr/bin/python

import re

l = [["name", "dinner"], ["Abraham", "Avi"], ["Hello", "Tree", "Door"], ["Name", "Glass", "Two", "am"]]

# 1. Unify all the sublist to a one bigger list.
biggerList = [value for sublist in l for value in sublist]
print(biggerList)

# 2. Remove all the duplicates from the bigger list.

noDuplicateList = list(set(biggerList))
print(noDuplicateList)

# 3. Print all the strings that have more than two letters in the middle of them.

print([value for value in noDuplicateList if re.search('^.+([a-zA-Z]{3,}).+$', value)])