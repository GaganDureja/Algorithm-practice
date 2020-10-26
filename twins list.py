# https://edabit.com/challenge/9BJzrtpdMP8JFQg74




def twins(lst):
	for x in range(len(lst)):		
		if sum(lst[:x])==sum(lst[x:]):
			return x
		
	







print(twins([1, 2, 3, 4, 5, 5]))

print(twins([3, 3]))

print(twins([10, 20, 30, 5, 40, 50, 40, 15]))