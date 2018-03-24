'''
    File name: calc_wirt.py
    Author: Paul Villanueva
    Date created: 1/3/2018
    Date last modified: 3/24/2018
    Python Version: 2.7
'''

from itertools import combinations
    
def process_gauss_code(raw_gauss_code):
    '''
    Formats input Gauss code for use in other functions.
    input:
        a sequence of characters or strings (which may contain commas) representing a Gauss code.
        
    output:
        a list of signed integers representing the Gauss code of a knot diagram.
    '''

    return [int(s) for s in raw_gauss_code.replace(",", "").split()]
    
def create_knot_dictionary(gauss_code):   
    '''
    Creates a knot dictionary from a Gauss code.
    
    input:
        gauss_code - a list of ints representing the Gauss code of the knot. 
            
    output:
        a dictionary representing the diagram of the Gauss code.
        
    The output knot dictionary is of the form
    
            d_k = {
                s_i: [(gauss_subseq), [c_1, c_2, . . ., c_n]]
                .
                .
                .
            },
            
    where s_i is the name of the strand, gauss_subseq is a tuple representing the subsequence of the Gauss code
    corresponding to the the strand, and the c_i represent the crossings that s_n are over.  The c_i are tuples 
    (s_i_1, s_i_2), where s_i_1 and s_i_2 are the names of the strands that s_i is over. 
    
    Warnings:
        This code will only run on standard Gauss code.
        This code does NOT check if the Gauss code is 'correct.'
        See readme.md for more details.        
            
    '''
 
    strands_dict = find_strands(gauss_code)
    knot_dict = find_crossings(strands_dict, gauss_code)
    
    return knot_dict
    
def find_strands(gauss_code):
    '''
    Processes a Gauss code to find the strands of the knot diagram.  
    
    inputs:
        gauss_code: a Gauss code (a list of signed integers) representing some knot diagram D.
        
    
    output:
        a dictionary whose keys are the strands of the knot diagram D.  
        
    The output knot dictionary is of the form
                d_k = {
                    s_i: [(gauss_subseq), [c_1, c_2, . . ., c_n]]
                    .
                    .
                    .
                },
                
    where s_i is the name of the strand and gauss_subseq is a tuple representing the subsequence of the
    Gauss code corresponding to the the strand.  The empty list will be populated with crossing
    information in the find_crossings function.       
    '''
    
    strand_set = set()

    i = 0
    while True:
        if gauss_code[i] < 0:
            beginning = i
            i = (i + 1) % len(gauss_code)
            while gauss_code[i] > 0:
                i = (i + 1) % len(gauss_code)
            if beginning > i:
                new_strand = gauss_code[beginning:]
                for k in range(i + 1):
                    new_strand.append(gauss_code[k])
                new_strand = tuple(new_strand)
            else:
                new_strand = tuple(gauss_code[beginning:i+1])
            if new_strand not in strand_set:
                strand_set.add(new_strand)
            else:
                break
        else:
            i = (i + 1) % len(gauss_code)
                
    letter_list = list(map(chr, range(65, 91)))
    strands_dict = dict()
    for i, strand in enumerate(strand_set):    
        strands_dict[letter_list[i]] = [strand, []]
    return strands_dict
    
def find_crossings(knot_dict, gauss_code):
    '''
    Takes a knot dictionary as output from the find_strands function and the corresponding Gauss code
    and populates the empty list in each key entry with the crossings that the strand is over.
    
    inputs:
        gauss_code: a Gauss code (a list of signed integers) representing some knot diagram D.
        knot_dict: a dictionary as output from find_strands.
        
    
    output:
        a dictionary whose keys are the strands of the knot diagram D.  
    The output knot dictionary is of the form
                d_k = {
                    s_i: [(gauss_subseq), []]
                    .
                    .
                    .
                },
    where s_i is the name of the strand, gauss_subseq is a tuple representing the subsequence of the Gauss code
    corresponding to the the strand, and the c_i represent the crossings that s_n are over.  The c_i are tuples 
    (s_i_1, s_i_2), where s_i_1 and s_i_2 are the names of the strands that s_i is over.      
    '''    
    
    for key_outer in knot_dict:
        for under in knot_dict[key_outer][0]:
            if under > 0:
                found1, found2 = False, False
                for key_inner in knot_dict:
                    if found1 and found2:
                        break
                    else:
                        if knot_dict[key_inner][0][0] == -under:
                            under1 = key_inner
                            found1 = True
                        if knot_dict[key_inner][0][-1] == -under:
                            under2 = key_inner
                            found2 = True
                knot_dict[key_outer][1].append((under1, under2))

    return knot_dict

def is_valid_coloring(seed_strands, knot_dict):
    '''
    Determines if a seed strand set leads to a valid coloring for a knot diagram represented 
    by the given knot dictionary.
    
    inputs:
        seed_strands: a set of characters representing strands in the knot diagram D
        knot_dict: a dictionary representing the knot
    
    See readme.md for explanation of algorithm.
    
    output:
        returns True if the seed_strands lead to a valid coloring of the knot, False otherwise
    '''
    
    seed_strands = set(seed_strands)
    colored_set = seed_strands.copy()
    new_coloring = True
    while new_coloring:
        new_coloring = False
        for strand in colored_set.copy():
            for crossing in knot_dict[strand][1]:
                if crossing[0] not in colored_set or crossing[1] not in colored_set:
                    if crossing[0] in colored_set or crossing[1] in colored_set:
                        colored_set.update(crossing)
                        new_coloring = True
                        
    if colored_set == set(knot_dict.keys()):
        return True
    
    return False
    
def calc_wirt_info(knot_dict):
    '''
    Calculates the Wirtinger number of a knot diagram D.
    
    input:
        knot_dict: a dictionary representing a knot diagram D.
    
    output:
        a tuple of (strands, n) where strands is a subset of the keys of knot_dict and n
        is the Wirtinger number of the knot diagram D.    
    '''
   
    n = 2
    while n < len(knot_dict):
        for seed_strands in combinations(knot_dict, n):
            if is_valid_coloring(seed_strands, knot_dict):
                return (seed_strands, n)
        n += 1

    
    # If control passes the above while loop, then a valid coloring with less than n - 1 strands
    # was not found.  In that case, return n - 1 colorability and an arbitrary subset
    # of n - 1 strands.
    return (set(knot_dict.keys()).pop, n)
    

def print_knot_dictionary(knot_dict):
    '''
    Nicely prints out a knot dictionary.
    
    input:
        knot_dict: a knot dictionary as put out by create_knot_dictionary.
        
    output:
        Prints out the strands of the knot dictionary, their corresponding subsequences in the
        Gauss code, and the crossings that the strand is over.
    '''
    
    print("\nKnot dictionary:\n")
    print("{:^15}{:30}{}".format("STRAND", "SUBSEQUENCE", "CROSSINGS OVER"))
    for strand in knot_dict:
        subsequence = knot_dict[strand][0]
        undercrossings = ' '.join([str(x) for x in knot_dict[strand][1]])
        print("{:^15}{:30}{}".format(strand, str(subsequence), undercrossings))
        
def display_wirtinger_info(raw_gauss_code):
    '''
        in - the Gauss code of a diagram of a knot
        out - a print out of information related to the wirtinger number
            of the knot diagram.
    '''

    gauss_code = process_gauss_code(raw_gauss_code)
    knot_dict = create_knot_dictionary(gauss_code)

    seed_strand_set, wirt_num = calc_wirt_info(knot_dict)

    print_knot_dictionary(knot_dict)
    print '\nSeed strand set: {}'.format(seed_strand_set)
    print "Wirtinger number: {}".format(wirt_num)

def get_wirtinger_info(raw_gauss_code):
    '''
        in - the Gauss code of a diagram of a knot
        out - the Wirtinger number of the knot diagram.
    '''
    gauss_code = process_gauss_code(raw_gauss_code)
    knot_dict = create_knot_dictionary(gauss_code)

    return calc_wirt_info(knot_dict)

if __name__ == "__main__":
    trefoil = "1, -2, 3, -1, 2, -3"
    display_wirtinger_info(trefoil)
