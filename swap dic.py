#Link:  https://edabit.com/challenge/cEzT2e8tLpwYnrstP




def swap_d(k, v, swapped):
	return {x[swapped]:x[not swapped] for x in zip(k,v)}






print(swap_d([1, 2, 3], ["one", "two", "three"], True))