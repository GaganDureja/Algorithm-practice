#Link: https://edabit.com/challenge/46Raiu9C7caNsgjqH








def compare_data(*args):
	return len({type(x) for x in args})==1 if args else True

	







print(compare_data(1, 6, 5, 3, 7, 9))