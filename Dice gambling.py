#Link: https://edabit.com/challenge/Yfm3h3nT3apARd4gC



def rolls(lst):
	return lst[0]+sum(lst[x]*2 if lst[x-1]==6 else lst[x]*0 if lst[x-1]==1 else lst[x] for x in range(1,len(lst)))










print(rolls([1, 2, 3]))