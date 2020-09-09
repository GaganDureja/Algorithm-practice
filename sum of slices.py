#Link: https://edabit.com/challenge/qKBfL9pQBaqXvKTfW


def sum_of_slices(lst):
	res = [0]
	for x in lst:
		if res[-1]+x<=100:
			res[-1]+=x
		else:
			res.append(x)
	return res








print(sum_of_slices([10, 29, 13, 14, 15, 16, 17, 31, 20, 10, 29, 13, 14, 15, 16, 17, 31, 20, 100]))