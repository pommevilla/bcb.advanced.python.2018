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


