#Link:  https://edabit.com/challenge/HJNhLoS4W8jdEYprh


def list_between(num1, num2, lst):
	return [x for x in lst if num2>x>num1]





print(list_between(3, 8, [1, 5, 95, 0, 4, 7]))