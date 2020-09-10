#Link: https://edabit.com/challenge/vfuZia9ufckGzhGZh


def seq_level(lst):
	diff1 = lst[1]-lst[0]
	diff2 = lst[2]-lst[1]
	return 'Linear' if diff2==diff1 else 'Quadratic' if lst[3]-lst[2]== diff2*2-diff1 else 'Cubic'









print(seq_level([4, 9, 16, 25, 36]))