#Link:  https://edabit.com/challenge/BYDZmaM6e4TQrgneb


def fib_fast(num):
	lst = [0,1]
	while len(lst)-1!=num:
		lst.append(lst[-1]+lst[-2])
	return lst[num]








print(fib_fast(10))