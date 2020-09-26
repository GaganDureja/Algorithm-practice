#Link:https://edabit.com/challenge/9gmNpQ3m9BTYm3FKr



from itertools import combinations as cb
def lucky_seven(lst):
	return any(sum(x)==7 for x in cb(lst,3))


print(lucky_seven([2, 4, 3, 8, 9, 1]))