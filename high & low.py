#Link: https://edabit.com/challenge/K9w9hEd9Pn7DtMzjs


def high_low(txt):
	txt = [int(x) for x in txt.split()]
	return '{} {}'.format(max(txt), min(txt))
	





print(high_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))