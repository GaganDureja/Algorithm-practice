#Link: https://edabit.com/challenge/DJa7PoKDhTTmwnxJg



def adjacent_product(lst):
	return max(lst[x]*lst[x-1] for x in range(1,len(lst)))






print(adjacent_product([3, 6, -2, -5, 7, 3]))
