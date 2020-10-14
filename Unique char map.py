#Link:  https://edabit.com/challenge/yPsS82tug9a8CoLaP




def character_mapping(txt):
	lst = ''
	for x in txt:
		if x not in lst:
			lst+=x
	return [lst.index(x) for x in txt]




print(character_mapping("babbcb"))