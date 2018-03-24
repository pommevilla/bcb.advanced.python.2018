'''
    Paul Villanueva
    BCBGSO 2018 Advanced Python Workshop
    
'''

# We can make a list by directly assigning values to the list.
girls = ["Ashley Burnett", "Rachel Athena", "Jennifer Lam", "Nancy Lam"]

boys = ["Leo Lam", "Calvin Fantone", "Adrian Egan", "Scott Roberts"]

# We can add a single value at a time with list.append().

print girls
girls.append("Vy Tran")
print girls

print boys
boys.append("Paul Villanueva")
print boys

# Add an entry to either one of the lists.

# We can use for loops to iterate over a list like so:

for girl in girls:
    print girl

# We can also use list comprehension to create lists. For instance, to create
# a list containing the numbers 0 to 9, we can do the following.
list_a = [i for i in range(10)]
print list_a

# We can do a lot of things with the expression inside the brackets.
# What do you think this does?
list_b = [i * i for i in range(10)]
print list_b

# How about this?
list_c = [list_a[i] + list_b[i] for i in range(10)]
print list_c

# This?
list_d = [[i + j for j in range(3)] for i in range(10)]
print list_d

# The string.split(x) function splits string into lists delimited by x.
# For example...
something = "That's what a hamburger's all about."
some_list = something.split()
print some_list

something_else = "It's,a,me,Mario!"
something_else = something_else.split(',')
print something_else

# We can use the split function inside of a list comprehension.
print ["Ms. {}".format(name.split()[1]) for name in girls]

# Can you do something similar for the boys' names?

# Challenge
# Uncomment the line below and see what it prints out.
# Read through it and understand it for yourself.
# print ["{} and {}".format(girls[i].split()[0], boys[i].split()[0]) for i in range(len(boys))]

# Another way of doing something close to this output is the following.
# Here, zip combines two lists into a new list of tuples with one element from each list.
# The * on pair unpacks a tuple and puts the values into the placeholder {}.
# Can you modify this code so that it only prints out the first name of each
# person instead of their first AND last name?
# print ["{} and {}".format(*pair) for pair in zip(boys, girls)]


# SOLUTION
# We can use another list comprehension inside of the string format to do what we want.
# This code is just a combination of the code above.
# print ["{} and {}".format(*[name.split()[0] for name in pair]) for pair in zip(boys, girls)]
