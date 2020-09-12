#Link:  https://edabit.com/challenge/a3hPXPfA2o98WBvxD



def fib_seq(*end):
	if not end: return None
	lst = [0,1]
	for x in range(2,end[0]):
		lst.append(lst[-1]+lst[-2])
	return lst[:end[0]]

    





print(fib_seq())
print(fib_seq(0))
print(fib_seq(1))
print(fib_seq(10))