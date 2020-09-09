#Link: https://edabit.com/challenge/DGK42TmQiocZqifxi



def reverse_complement(input_sequence):
	return input_sequence.translate(str.maketrans('AUGC','UACG'))[::-1]








print(reverse_complement("UCUCG"))