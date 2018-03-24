"""
    Paul Villanueva
    BCBGSO Advanced Python Workshop 2018
"""

# import the calc_wirt package.  Give it an alias.
import calc_wirt as cw



if __name__ == "__main__":
    # Our goal is to write the following to an output file:
    #    
    #   Knot name, Seed Strands, Set Wirtinger Number
    #
    # The gauss_codes.txt file already contains the knot name and the Gauss code.
    # Write a for loop that reads through gauss_codes and writes the name and the Gauss code
    # to a file called "knot_info.txt".
    # Carefully look at the format of the file and pick the appropriate character to split on.
    # See here for a hint: https://tinyurl.com/yaujd8cr

##    with open("gauss_codes.txt") as fin, open("knot_info.txt", 'w') as fout:
##        for line in fin:
##            knot_name, gauss_code = line.split(":")
##            fout.write("{}\t{}".format(knot_name, gauss_code))

    # Verify that knot_info is being printed correctly.
    # Now, use the get_wirtinger_info function from calc_wirt to get the seed_strand set
    # and the Wirtinger number of the knot for each line.
    # Modify the print statement by removing the Gauss code and adding the seed strands
    # and the Wirtinger number.

    with open("gauss_codes.txt") as fin, open("knot_info.txt", 'w') as fout:
        for line in fin:
            knot_name, gauss_code = line.rstrip().split(":")
            seed_strands, wirt_num = cw.get_wirtinger_info(gauss_code)
            fout.write("{}\t{}\t{}\n".format(knot_name, seed_strands, wirt_num))

    pass
