#Link: https://edabit.com/challenge/oq2FxAx5bJZgPLk9r



def sock_merchant(lst):
	return sum([lst.count(x)//2 for x in set(lst)])

	







print(sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))