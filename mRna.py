#Link: https://edabit.com/challenge/McZF4JRhPus5DtRA4


def dna_to_rna(dna):
	mRNA= dna.replace('A','U').replace('T','A')
	return ''.join(['C' if x=='G' else 'G' if x=='C' else x for x in mRNA])

			







print(dna_to_rna("ATTAGCGCGATATACGCGTAC"))