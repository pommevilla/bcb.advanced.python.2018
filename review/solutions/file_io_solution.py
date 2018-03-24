'''
    Paul Villanueva
    BCBGSO 2018 Advanced Python Workshop
    
'''

# Below is the basic code for reading from a file.  Run this code.



# Note that each of the lines has an extra newline after it.  This is because
# there is a newline character at the end of each line.  Modify the code you just
# to get rid of this newline character.  Hint: look up rstrip().



# Now let's count the lines.  There's a couple different ways to do this.
# Print out the number of lines after the text is finished printing.



# Change it so that you're outputting the line number in front of the line.


# Now, let's print out every line to another file.



# All we did was copy the whole file over to another file.  Not that exciting.
# Let's do change the code so that it only writes every other line.



# How can we modify the above code so that it alternates between printing to the
# console and writing to the output file?

with open("100_percent.txt") as fin, open("output.txt", 'w') as fout:
    for line_num, line in enumerate(fin):
##        line = line.rstrip()
##        print line_num, line
        if line_num % 2 == 0:
            fout.write("{}".format(line))
        else:
            print line
print line_num
