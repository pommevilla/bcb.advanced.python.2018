'''
    Paul Villanueva
    BCBGSO 2018 Advanced Python Workshop
    March 24, 2018
'''

# We're going to follow much the same process as we did when we did Exercise 1.

# Define a function get_rating_info that takes as input a file name
# and (for now) outputs the highest rated item in the file.
# The general outline of this function will is:
# Open the file
#   Initiate highest_rating = 0, highest_item = ''
#   For every line in the file
#       split the line on the the "-" and save them to current rating and current item
#       if the current rating is higher than the highest rating
#           ...
# Return highest_rating, highest_item

def get_rating_info(in_file):
    '''
        in - a file of ratings in the format "ITEM - RATING" separated by newlines.
        out - returns the name and rating for the highest rated item.
    '''
    pass

# Once you have implemented the get_rating_info function, try it out on the files.
# Compare the answer with the values in the file - are you getting what you expected?
# What could be the problem?

# Once you get the code working correctly, we'll flesh out the main function.


if __name__ == "__main__":
    # Create a list of the file names.  Call this list ratings_list.

    # For each of the items in this list, print out the highest rated item and its rating on
    # separate lines.  Make the print out nice.

# Challenges
# If there are multiple items with the same highest rating, get_rating_info skips over them.  How can you change the code
# so that the LAST item with the highest rating is returned?

# Edit get_rating_info so that it also returns the average rating for the file.
