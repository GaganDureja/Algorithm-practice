# Link:  https://www.hackerrank.com/challenges/lonely-integer/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign




def unique(lst):
	return [x for x in lst if lst.count(x)==1][0]








print(unique([0,0,1,2,1]))

print(unique([1,1,2]))

print(unique([1,2,3,4,3,2,1]))
