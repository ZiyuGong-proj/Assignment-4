# '#' is for comment
a = 1
b = 1.0
c1 = True
c2 = False
d1 = 'Good Morning'
d2 = "Good Morning"

# Math is what you would expect
1 + 1   # => 2
8 - 1   # => 7
10 * 2  # => 20
35 / 5  # => 7.0
# Enforce precedence with parentheses
1 + 3 * 2    # => 7
(1 + 3) * 2  # => 8
# The result of division is always a float
10.0 / 3  # => 3.3333333333333335
# Exponentiation (x**y, x to the yth power)
2**3  # => 8

# Integer division rounds down 
# for both positive and negative numbers.
5 // 3       # => 1
-5 // 3      # => -2
# Modulo operation
7 % 3   # => 1
# i % j have the same sign as j, unlike C
-7 % 3  # => 2


# Boolean Operators
# negate with not
not True   # => False
not False  # => True
# Note "and" and "or" are case-sensitive
True and False  # => False
False or True   # => True
# True and False are actually 1 and 0
# but with different keywords
True + True # => 2
True * 8    # => 8
False - 5   # => -5

# Equality is ==
1 == 1  # => True
2 == 1  # => False

# Inequality is !=
1 != 1  # => False
2 != 1  # => True

# More comparisons
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# Seeing whether a value is in a range
1 < 2 and 2 < 3  # => True
2 < 3 and 3 < 2  # => False


# Strings are created with " or '
"This is a string."
'This is also a string.'

# Strings can be added too
"Hello " + "world!"  # => "Hello world!"

# A string can be treated like a list of characters
"Hello world!"[0]  # => 'H'

# You can find the length of a string
len("This is a string")  # => 16



# There are no declarations, only assignments.
# Convention is to use lower_case_with_underscores
some_var = 5
some_var  # => 5

# Accessing a previously unassigned 
# variable is an exception.
#some_unknown_var  # Raises a NameError

# Python has a print function
print("Nice to meet you!")  # => Nice to meet you!
print(some_var) # => 5

# Lists store sequences
li = []
# You can start with a prefilled list
other_li = [4, 5, 6]

# Add stuff to the end of a list with append
li.append(1)    # li is now [1]
li.append(2)    # li is now [1, 2]
li.append(4)    # li is now [1, 2, 4]
li.append(3)    # li is now [1, 2, 4, 3]
# Remove from the end with pop
li.pop()        # => 3 and li is now [1, 2, 4]
# Let's put it back
li.append(3)    # li is now [1, 2, 4, 3] again.

li = [1, 2, 4, 3]
# Access a list like you would any array
li[0]   # => 1
# Look at the last element
li[-1]  # => 3

# Looking out of bounds is an IndexError
#li[4]  # Raises an IndexError

# You can look at ranges with slice syntax.
# The start index is included, the end index is not
# (It's a closed/open range for you mathy types.)
li[1:3]   # Return list from index 1 to 3 => [2, 4]
li[2:]    # Return list starting from index 2 => [4, 3]
li[:3]    # Return list from beginning until index 3  => [1, 2, 4]
li[::2]   # Return list selecting every second entry => [1, 4]
li[::-1]  # Return list in reverse order => [3, 4, 2, 1]
# Use any combination of these to make advanced slices
# li[start:end:step]


li = [1, 2, 4, 3]
# Make a one layer deep copy using slices
li2 = li[:]  # => li2 = [1, 2, 4, 3], 
# the address of li and li2 is also different

# Remove arbitrary elements from a list with "del"
del li[2]  # li is now [1, 2, 3]

# Remove first occurrence of a value
li.remove(2)  # li is now [1, 3]
#li.remove(2)  # Raises a ValueError as 2 is not in the list

# Insert an element at a specific index
li.insert(1, 2)  # li is now [1, 2, 3] again

# Get the index of the first item found matching the argument
li.index(2)  # => 1
#li.index(4)  # Raises a ValueError as 4 is not in the list

# You can add lists
li = [1, 2, 4, 3]
other_li = [4, 5, 6]
li + other_li  # => [1, 2, 4, 3, 4, 5, 6]

# Concatenate lists with "extend()"
li.extend(other_li)  # Now li is [1, 2, 4, 3, 4, 5, 6]

# Check for existence in a list with "in"
1 in li  # => True

# Examine the length with "len()"
len(li)  # => 7

# Tuples are like lists but are immutable.
tup = (1, 2, 3)
tup[0]      # => 1
#tup[0] = 3  # Raises a TypeError

# You can do most of the list operations on tuples too
len(tup)         # => 3
tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
tup[:2]          # => (1, 2)
2 in tup         # => True

# You can unpack tuples (or lists) into variables
a, b, c = (1, 2, 3)  # a is now 1, b is now 2 and c is now 3
# You can also do extended unpacking
a, *b, c = (1, 2, 3, 4)  # a is now 1, b is now [2, 3] and c is now 4
# Tuples are created by default if you leave out the parentheses
d, e, f = 4, 5, 6  # tuple 4, 5, 6 is unpacked into variables d, e and f
# respectively such that d = 4, e = 5 and f = 6
# Now look how easy it is to swap two values
e, d = d, e  # d is now 5 and e is now 4


# Dictionaries store mappings from keys to values
empty_dict = {}
# Here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}

# Look up values with []
filled_dict["one"]  # => 1

# Get all keys as an iterable with "keys()". We need to wrap
# the call in list() to turn it into a list.
list(filled_dict.keys())  # => ["one", "two", "three"]

# Get all values as an iterable with "values()". Once again 
# we need to wrap it in list() to get it out of the iterable. 
list(filled_dict.values())  # => [1, 2, 3] 

# Check for existence of keys in a dictionary with "in"
"one" in filled_dict  # => True
1 in filled_dict      # => False

filled_dict = {"one": 1, "two": 2, "three": 3}
#Looking up a key
filled_dict["one"]  # => 1

# Adding to a dictionary
filled_dict.update({"four":4})  # => {"one": 1, "two": 2, "three": 3, "four": 4}
filled_dict["four"] = 4         # another way to add to dict

# Remove keys from a dictionary with del
del filled_dict["one"]  # Removes the key "one" from filled dict

li = [1, 1, 2, 2, 3, 4]
filled_set = set(li) # filled_set is now {1, 2, 3, 4}

# Directly initialize a set with a bunch of values. 
# Yeah, it looks a bit like a dict. Sorry
filled_set = {1,1,2,2,3,4} # filled_set is {1, 2, 3, 4}
 
# Add one more item to the set
filled_set.add(5)  # filled_set is now {1, 2, 3, 4, 5}
# Sets do not have duplicate elements
filled_set.add(5)  # it remains as before {1, 2, 3, 4, 5}

# Do set intersection with &
other_set = {3, 4, 5, 6}
filled_set & other_set  # => {3, 4, 5}

# Do set union with |
filled_set | other_set  # => {1, 2, 3, 4, 5, 6}

# Do set difference with -
{1, 2, 3, 4} - {2, 3, 5}  # => {1, 4}

# Check if set on the left is a superset of set on the right
{1, 2} >= {1, 2, 3} # => False

# Check if set on the left is a subset of set on the right
{1, 2} <= {1, 2, 3} # => True

filled_set = {1, 2, 3, 4}
# Check for existence in a set with in
2 in filled_set   # => True
10 in filled_set  # => False

# Here is an if statement. Indentation is significant in Python!
# Convention is to use four spaces, not tabs.
# This prints "some_var is smaller than 10"
if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10:    # This elif clause is optional.
    print("some_var is smaller than 10.")
else:                  # This is optional too.
    print("some_var is indeed 10.")


"""
For loops iterate over lists
prints:
    dog 
    cat 
    mouse
"""
for animal in ["dog", "cat", "mouse"]:
    print(animal)


"""
For loops iterate over range
prints:
    0
    1
    2
    3
"""
for i in range(4):
    print(i)

'''
"range(lower, upper)" returns an iterable of numbers
from the lower number to the upper number
prints:
    4
    5
    6
    7
'''
for i in range(4, 8):
    print(i)
    
"""
"range(lower, upper, step)" returns an iterable of numbers
from the lower number to the upper number, while incrementing
by step. If step is not indicated, the default value is 1.
prints:
    4
    6
"""
for i in range(4, 8, 2):
    print(i)
    

"""
While loops go until a condition is no longer met.
prints:
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print(x)
    x += 1  # Shorthand for x = x + 1


# Use "def" to create new functions
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y  # Return values with a return statement

# Calling functions with parameters
add(5, 6)  # => prints out "x is 5 and y is 6" and returns 11

# Another way to call functions is with keyword arguments
add(y=6, x=5)  # Keyword arguments can arrive in any order.

# Returning multiple values (with tuple assignments)
def swap(x, y):
    return y, x  # Return multiple values as a tuple without the parenthesis.
                 # (Note: parenthesis have been excluded but can be included)

x = 1
y = 2
x, y = swap(x, y)     # => x = 2, y = 1
# (x, y) = swap(x,y)  # Again parenthesis have been excluded but can be included.


# You can import Library
import math
print(math.sqrt(16))  # => 4.0

# You can get specific functions from a Library
from math import sqrt
print(sqrt(16))    # => 4.0

# You can import all functions from a Library.
# Warning: this is not recommended
from math import *

# You can shorten Library names
import math as m
math.sqrt(16) == m.sqrt(16)  # => True

