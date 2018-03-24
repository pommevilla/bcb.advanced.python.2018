'''
    Paul Villanueva
    BCBGSO Advanced Python Workshop
    3/23/2018

    Making a function that reads text files and counts the number of lines.
'''

def line_counter(in_file):
    with open(in_file) as fin:
        blank_lines = 0
        for line_num, line in enumerate(fin):
            line = line.rstrip()
            if not line:
                blank_lines += 1
##            print line_num, line
            pass
            

    return line_num - blank_lines

if __name__ == '__main__':
    print line_counter('monday.txt')
