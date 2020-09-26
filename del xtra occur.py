#Link: https://edabit.com/challenge/iA5aeTFGLcxx94Wjh



def delete_occurrences(lst, num):
	res = []
	for x in lst:
		if res.count(x)<num:
			res.append(x)
	return res







print(delete_occurrences([1, 1, 1, 1], 2))