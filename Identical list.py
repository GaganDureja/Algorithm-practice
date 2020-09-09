#Link: https://edabit.com/challenge/QugwmQ8WH6x4oqMD9


def count_identical_lists(*lst):
	res = max(lst.count(x) for x in lst)
	return res if res>1 else 0











print(count_identical_lists([0, 0, 0], [0, 1, 2], [0, 0, 0], [2, 1, 0]))
