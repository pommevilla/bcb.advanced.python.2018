"""
    Paul Villanueva
    BCBGSO Advanced Python Workshop 2018

    
"""

# Import the bioinformatics_utilities package.  Use the "as" keyword to give
# it a shorter name.

import bioinformatics_utilities as bio_utils

if __name__ == '__main__':
    # We're going to adapt the code in the main section of bioinformatics_utilities
    # so that it performs the same kind of analysis on the ENTIRE short.inti1.97.fasta file.
    # Copy over that code and change it so that:
    #   The gene of interest is the last gene in the gene list
    #   Alignments are calculated against ALL the genes in short.inti1.97.fasta EXCEPT the last one.

##    genes = bio_utils.read_fasta_file('short.inti1.97.fasta')
##    goi = genes[-1]
##    best_score = 0
##    best_gene = ''
##    for gene in genes[:-1]:
##        current_score = bio_utils.get_alignment_score(goi, gene)
##        print "Alignment score between {} and {}: {}".format(goi[0], gene[0], current_score)
##        if current_score > best_score:
##            best_score = current_score
##            best_gene = gene
##    print "Gene best aligned with {} was {} with alignment score of {}.\n".format(goi[0], best_gene[0], best_score)
##    bio_utils.get_alignment_score(goi, best_gene, output = True)


    # Modify the above code to print out the average alignment score after the alignment information.

##    genes = bio_utils.read_fasta_file('short.inti1.97.fasta')
##    goi = genes[-1]
##    best_score = 0
##    best_gene = ''
##    alignment_score_sums = 0
##    for gene in genes[:-1]:
##        current_score = bio_utils.get_alignment_score(goi, gene)
##        alignment_score_sums += current_score
##        print "Alignment score between {} and {}: {}".format(goi[0], gene[0], current_score)
##        if current_score > best_score:
##            best_score = current_score
##            best_gene = gene
##    print "Gene best aligned with {} was {} with alignment score of {}.\n".format(goi[0], best_gene[0], best_score)
##    bio_utils.get_alignment_score(goi, best_gene, output = True)
##
##    average_alignment_score = alignment_score_sums / float(len(genes))
##
##    print "The average alignment score against {} was {}.".format(goi[0], average_alignment_score)

    # Let's modify the above code so that it writes all the alignment information to another file.
##    genes = bio_utils.read_fasta_file('short.inti1.97.fasta')
##    goi = genes[-1]
##    best_score = 0
##    best_gene = ''
##    alignment_score_sums = 0
##    with open("short_alignment_info.txt", 'w') as fout:
##        for gene in genes[:-1]:
##            current_score = bio_utils.get_alignment_score(goi, gene)
##            alignment_score_sums += current_score
##            fout.write("Alignment score between {} and {}: {}\n".format(goi[0], gene[0], current_score))
##            print "Alignment score between {} and {}: {}".format(goi[0], gene[0], current_score)
##            if current_score > best_score:
##                best_score = current_score
##                best_gene = gene
##        print "Gene best aligned with {} was {} with alignment score of {}.\n".format(goi[0], best_gene[0], best_score)
##        fout.write("Gene best aligned with {} was {} with alignment score of {}.\n".format(goi[0], best_gene[0], best_score))
##        
##    bio_utils.get_alignment_score(goi, best_gene, output = True)
##
##    average_alignment_score = alignment_score_sums / float(len(genes))
##
##    print "The average alignment score against {} was {}.".format(goi[0], average_alignment_score)

    # Now, make the following two changes:
    #   'short.inti1.97.fasta' -> 'inti1.97.fasta'
    #   'short_alignment_info.txt" -> 'alignment_info.txt'

    genes = bio_utils.read_fasta_file('inti1.97.fasta')
    goi = genes[-1]
    best_score = 0
    best_gene = ''
    alignment_score_sums = 0
    with open("alignment_info.txt", 'w') as fout:
        for gene in genes[:-1]:
            current_score = bio_utils.get_alignment_score(goi, gene)
            alignment_score_sums += current_score
            fout.write("Alignment score between {} and {}: {}\n".format(goi[0], gene[0], current_score))
            print "Alignment score between {} and {}: {}".format(goi[0], gene[0], current_score)
            if current_score > best_score:
                best_score = current_score
                best_gene = gene
        print "Gene best aligned with {} was {} with alignment score of {}.\n".format(goi[0], best_gene[0], best_score)
        fout.write("Gene best aligned with {} was {} with alignment score of {}.\n".format(goi[0], best_gene[0], best_score))
        
    bio_utils.get_alignment_score(goi, best_gene, output = True)

    average_alignment_score = alignment_score_sums / float(len(genes))

    print "The average alignment score against {} was {}.".format(goi[0], average_alignment_score)
    
