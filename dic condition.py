#Link:  https://edabit.com/challenge/8pDH2SRutPoaQghgc



dic = {
	'Darth Vader':'father',
	'Leia':'sister',
	'Han':'brother in law',
	'R2D2':'droid'
}
def relation_to_luke(name):
	return 'Luke, I am your %s.'%dic[name]





print(relation_to_luke("Darth Vader"))