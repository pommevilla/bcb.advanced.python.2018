"""
    Paul Villanueva
    BCBGSO Advanced Python Workshop 2018

    A list of modified bioinformatics utility functions.
"""


class DNAString:
	"""
            Represents a DNA sequence with a header.  
	"""

	def __init__(self, header, seq):
		self.header = header
		self.seq = seq
	   
	@property
	def length(self):
		"""
                    >>> string1 = bcbutils.read_fasta_file("A.short.txt")
                    >>> A = DNAString(*string1)
                    >>> A.length
                    26
		"""
		return len(self.seq)
		
	def __len__(self):
		return len(self.seq)

	def __iter__(self):
		self.current = 0
		return self
		
	def __next__(self):
		if self.current == self.length - 1:
			raise StopIteration
		else:
			self.current = self.current + 1
			return self.seq[self.current]
			
	def __getitem__(self, i):
		"""
                    >>> string1 = bcbutils.read_fasta_file("A.short.txt")
                    >>> A = DNAString(*string1)
                    >>> print(A[0])
                    G
		"""
		return self.seq[i]
	
	def __str__(self):
		"""
                    >>> string1 = bcbutils.read_fasta_file("A.short.txt")
                    >>> A = DNAString(*string1)
                    >>> print(A)
                    Ashort
                    GATCGTAGAGTGAGACCTAGTGTTTG
		"""
		return "{}\n{}".format(self.header, self.seq)

class LocalAlignment:
	"""
            Represents an optimal local alignment between two DNA strings.
	"""
	
	def __init__(self, dnastring1, dnastring2, match_score = 15, mismatch_score = -20,
                     gap_open_penalty = 40, gap_extend_penalty = 2):
            
		self.dnastring1 = dnastring1 
		self.dnastring2 = dnastring2
		
		self.match_score = match_score 
		self.mismatch_score = mismatch_score 
		self.gap_open_penalty = gap_open_penalty
		self.gap_extend_penalty = gap_extend_penalty
		
		
		S_matrix, D_matrix, I_matrix, self.max_score_row, self.max_score_column = calculate_matrices(self.dnastring1, self.dnastring2, self.match_score, mismatch_score, gap_open_penalty, gap_extend_penalty)
		
		self.max_alignment_score = S_matrix[self.max_score_row][self.max_score_column]
		
		self.optimal_alignment = traceback(S_matrix, D_matrix, I_matrix, self.dnastring1, self.dnastring2, self.gap_open_penalty + self.gap_extend_penalty, self.max_score_row, self.max_score_column)
		
		del S_matrix, D_matrix, I_matrix
		
		
	@property
	def length(self):
		"""
		>>> string1 = bcbutils.read_fasta_file("A.short.txt")
		>>> A = DNAString(*string1)
		>>> string2 = bcbutils.read_fasta_file("B.short.txt")
		>>> B = DNAString(*string2)
		>>> AB_local_alignment = LocalAlignment(A, B, 10, -20, 40, 2)
		>>> AB_local_alignment.length
		22
		"""
		return len(self.optimal_alignment)
		
	def process_alignment(self):
		"""
		Partitions self.optimal_alignment into subsequences of size 70 and saves the chunks into a list of strings.
		Returns formatted sections of the alignment ready for printing to the console and counts of deletions, insertions, matches
		mismatches, and the position in each string where the alignments end.
		
		This one is really ugly and got away from me because I was working on this one last.  
		"""
		insertion_count = 0
		deletion_count = 0
		match_count = 0
		mismatch_count = 0
		
		# Breaks the optimal alignment into subsequences 70 pairs long per assignment instructions.
		optimal_alignment_sections_raw = [section for section in sectioner(self.optimal_alignment)]
		
		optimal_alignment_sections_processed = []
		
		
		align_position_A = self.max_score_row + 1
		align_position_B = self.max_score_column + 1
		
		# n counts our spot in the alignment and puts a '.' or ':' every 5 spots, alternating, to ease reading.
		n = 0
			
		for section in optimal_alignment_sections_raw:
			spacer_string = '{:5} '.format(' ')
			aligned_string_A = '{:>5} '.format(n + align_position_A)
			aligned_string_mid = '{:5} '.format(' ')
			aligned_string_B = '{:>5} '.format(n + align_position_B)
			for i in section:
				if ((n + 1) % 10)  == 5:
					spacer_string += '.'
				elif ((n + 1) % 10) == 0:
					spacer_string += ':'
				else:
					spacer_string += ' ' 
				aligned_string_A += i[0]
				aligned_string_B += i[1]
				if i[0] == ' ':
					aligned_string_mid += "-"
					insertion_count += 1
					align_position_A -= 1
				elif i[1] == ' ':
					aligned_string_mid += "-"
					deletion_count += 1
					align_position_B -= 1
				elif i[0] != i[1]:
					aligned_string_mid += 'x'
					mismatch_count += 1
				else:
					aligned_string_mid += "|"
					match_count += 1
					
				n += 1
			optimal_alignment_sections_processed.append("{:>7}\n{:>7}\n{:>7}\n{:>7}".format(spacer_string, aligned_string_A, aligned_string_mid, aligned_string_B))
			
			A_end = n + align_position_A - 1
			B_end = n + align_position_B - 1
		
			
		return optimal_alignment_sections_processed, A_end, B_end, insertion_count, deletion_count, mismatch_count, match_count

        # Not working as intended since this was backported from Python 3.
	def __str__(self):
		sectioned_string_alignment, A_end, B_end, insertion_count, deletion_count, mismatch_count, match_count = self.process_alignment()	
		
		
		# Extra blank character at the end of the argument to make the spacing nice.
		score_info_header = "{:^15}{:^20}{:^20}{:^28}".format(
			"Match Score", "Mismatch Score", "Gap Open Penalty", "Gap Extension Penalty"
			)
		score_info_values = "{:^15}{:^20}{:^20}{:^28}".format(
			self.match_score, self.mismatch_score, self.gap_open_penalty, self.gap_extend_penalty
			)
		
		score_info = "\n".join([score_info_header, score_info_values, ''])
		
		seq_info = "{:>20}: {}\n{:>20}: {}\n{:>20}: {}\n{:>20}: {}\n".format(
			"Sequence A", self.dnastring1.header, 
			"Length", self.dnastring1.length, 
			"Sequence B", self.dnastring2.header, 
			"Length", self.dnastring2.length
			)
			
		align_info = "{:>20}: {}\n{:>20}: {}\n{:>20}: {}\n{:>20}: {}\n{:>20}: {}\n{:>20}: {}\n".format(
			"Alignment Score", self.max_alignment_score, 
			"Length", self.length, 
			"Start in A", str(self.max_score_row + 1), 
			"Start in B", str(self.max_score_column + 1), 
			"End in A", A_end, 
			"End in B", B_end
			)
			
		match_info = "{:>20}: {}\n{:>20}: {}\n{:>20}: {:.6f}\n\n{:>20}: {}\n{:>20}: {}\n{:>20}: {}\n".format(
			"Number of matches", match_count, 
			"Number of mismatches", mismatch_count, 
			"Match percentage", match_count / self.length, 
			"Number of deletions", deletion_count, 
			"Number of insertions", insertion_count, 
			"Total length of gaps", deletion_count +insertion_count
			)
		
		
		
		return "\n".join([score_info, seq_info, align_info, match_info, "\n".join(sectioned_string_alignment)])

def calculate_matrices(A, B, MATCH_SCORE, mismatch_score, gap_open, gap_extend):
	"""
	A, B - two DNA sequences 
	mismatch - a negative integer indicating mismatch scare
	gap_open - a non-negative integer indicating gap_open penalty
	gap_extend - a positive integer indicating gap extension penalty
	
	returns:
			matrices of integers S, D, and I, where:
				-S[i][j] is the maximum score of all local alignments starting at A[i + 1] and B[j + 1]
				-D[i][j] is the maximum score of those local alignments that begin with a deletion gap
				-I[i][j] is the maximum score of those local alignments that begin with an insertion gap
			integers max_score, max_score_row, max_score_column, where:
				-max_score is the highest alignment score in the S matrix
				-max_score_row and max_score_column are max_score's row and column position in the S matrix, respectively
		
	"""
	m = len(A)
	n = len(B)
	S, D, I = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(3)]
	
	max_score_row = m
	max_score_column = n
	
	gap_init_penalty = gap_open + gap_extend
	
	max_score = 0
	
	D[m][n] = -gap_init_penalty
	I[m][n] = -gap_init_penalty
	
	for i in reversed(range(n)):
		D[m][i] = -gap_init_penalty
		I[m][i] = -gap_init_penalty

		
	for i in reversed(range(m)):
		D[i][n] = -gap_init_penalty
		I[i][n] = -gap_init_penalty
		
		for j in reversed(range(n)):
			D[i][j] = max(D[i + 1][j] - gap_extend,
							S[i + 1][j] - gap_init_penalty)
			I[i][j] = max(I[i][j + 1] - gap_extend, 
							S[i][j + 1] - gap_init_penalty)
			S[i][j] = max(0, S[i + 1][j + 1] + delta(A[i], B[j], MATCH_SCORE, mismatch_score),
							D[i][j], I[i][j])
			if max_score < S[i][j]:
				max_score = S[i][j]
				max_score_row = i
				max_score_column = j 
	
	return S, D, I, max_score_row, max_score_column
	
def traceback(S, D, I, A, B, gap_init_penalty, max_score_row, max_score_column):
	"""
            A, B - two DNA sequences
            S, D, I - the three matrices returned by calculate_matrices(A, B)
            gap_init_penalty - a positive integer indicating a penalty for opening a gap.
                This quantity is equal to the sum gap_open_penalty + gap_extend_penalty that is subtracted in the traceback algorithm.
            max_score_row, max_score_column - integers indicating the location of the max_score in the S matrix
	
	"""

	m = len(S)
	n = len(S[0])

	opt_align = []
	i = max_score_row
	j = max_score_column
	current_mat = 'S'

	while i <= m and j <= n:
		if current_mat == 'S':
			if i == m - 1 or j == n - 1 or S[i][j] == 0:
				break
			if S[i][j] == D[i][j]:
				current_mat = 'D'
				continue
			if S[i][j] == I[i][j]:
				current_mat = 'I'
				continue
			opt_align.append((A[i], B[j]))
			i += 1
			j += 1
			
		if current_mat == 'D':
			opt_align.append((A[i], ' '))
			if i == m - 1 or D[i][j] == S[i + 1][j] - gap_init_penalty:
				current_mat = 'S'
			i += 1
			continue
			
		if current_mat == 'I':
			opt_align.append((' ', B[j]))
			if j == n - 1 or I[i][j] == S[i][j + 1] - gap_init_penalty:
				current_mat = 'S'
			j += 1
			continue
			

	row_last = i
	col_last = j
	
	aligned_string_A = ''
	aligned_string_mid = ''
	aligned_string_B = ''
	
	for pair in opt_align:
		aligned_string_A += pair[0]
		aligned_string_B += pair[1]
		if pair[0] == ' ' or pair[1] == ' ':
			aligned_string_mid += '-'
		else:
			aligned_string_mid += "|"
			
	return opt_align

def get_alignment_score(stringA, stringB, output = False):
    """
        in - stringA, stringB, two tuples of (header, DNA sequence)

        out - best local alignment score as calculated with the following scoring parameters:
            match score = 15, mismatch score = -20,
            gap initiation penalty = 40, gap extension penalty = 2
    """
    A = DNAString(*stringA)
    B = DNAString(*stringB)
    AB_optimal_alignment = LocalAlignment(A, B)
    if output:
            print AB_optimal_alignment
    return AB_optimal_alignment.max_alignment_score

def calc_word_code(dnastring):
    """
        in - a string of nucleotides
         
        out - the word score of the DNA string.  
    """
    value_map = {   
                    'A': 0,
                    'C': 1,
                    'G': 2,
                    'T': 3
                }
    
    values = []
    for char in dnastring:
        if char not in value_map:
            return -1
        else:
            values.append(value_map[char])
            
    word_code = 0
    for n, value in enumerate(values):
        word_code += value * (4 ** (len(values) - n - 1))

    return word_code

##def get_alignment_score(stringA, stringB):
##    """
##        
##    """
##    A = DNAString(*stringA)
##    B = DNAString(*stringB)
##    AB_optimal_alignment = LocalAlignment(A, B)
##    return AB_optimal_alignment.max_alignment_score

def sectioner(seq, n = 70):
	"""
            seq - any sequence- or list-like object
            n - desired size of chunks.  Defaulted to 70 per assignment directions.
            
            returns a list of subsequences of seq, each of size n.  
	"""
	return (seq[i:i + n] for i in range(0, len(seq), n))

def delta(a, b, match, mismatch):
	"""
            in:
                a, b - two characters 
                match - a positive integer score for a character match
                mismatch - a negative integer score for a character mismatch

            out- the match score if a and b match, and the mismatch score otherwise.
            
            >>> delta("C", "C", 10, -20)
            10
            
            >>> delta("C", "T", 10, -30)
            -30
            
	"""
	return match if a is b else mismatch

def read_fasta_file(fasta_file):
    """
        in - a .txt file in FASTA format
    
        out - a list containing tuples of (header, dnastring)
    """
    
    with open(fasta_file) as fin:
    
        dnastring_list = []
        header, seq = None, ""
        
        for line in fin:
            line = line.rstrip()
            if line.startswith(">"):
                if header:
                    dnastring_list.append((header, seq))
                header, seq = line[1:], ""
            else:
                seq += line.rstrip()
        dnastring_list.append((header, seq))

        return dnastring_list
    


if __name__ == '__main__':
    genes = read_fasta_file('inti1.97.fasta')
    goi = genes[0]
    best_score = 0
    best_gene = ''
    for gene in genes[1:10]:
        current_score = get_alignment_score(goi, gene)
        print "Alignment score between {} and {}: {}".format(goi[0], gene[0], current_score)
        if current_score > best_score:
            best_score = current_score
            best_gene = gene
    print "Gene best aligned with {} was {} with alignment score of {}.\n".format(goi[0], best_gene[0], best_score)
    get_alignment_score(goi, best_gene, output = True)
    
