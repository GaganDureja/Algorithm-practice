#Link: https://edabit.com/challenge/dKeLAqAxpddbkvNhh


def group_seats(lst, n):
	count = 0
	for r in lst:
		if r.count(0)>=n:
			for x in range(n,len(r)+1):
				if r[x-n:x].count(0)==n:
					count+=1
	return count






print(group_seats([
	[1, 0, 1, 0, 1, 0, 1], 
	[0, 1, 0, 1, 0, 1, 0], 
	[0, 0, 0, 0, 0, 0, 0], 
	[1, 0, 1, 1, 0, 0, 1], 
	[1, 1, 1, 0, 0, 0, 1], 
	[0, 1, 1, 1, 1, 0, 0]
], 7))