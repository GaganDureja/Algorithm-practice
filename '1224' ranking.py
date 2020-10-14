#Link:  https://edabit.com/challenge/2hk7hFz6haBahtnof




def competition_rank(results, person):	
	return sorted([results[x] for x in results])[::-1].index(results[person])+1
	




print(competition_rank({'Aria': 90, 'Brooke': 90, 'Olivia': 90, 'Eve': 74, 'Ellie': 87}, "Ellie"))