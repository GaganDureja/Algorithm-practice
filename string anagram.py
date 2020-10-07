#Link:  https://edabit.com/challenge/KYGpco9NFmJRyMQqj






def min_removals(txt1, txt2):	
	return sum([abs(txt1.count(x)-txt2.count(x)) for x in txt1] + [abs(txt1.count(x)-txt2.count(x)) for x in txt2])

	







print(min_removals("acb", "ghi"))