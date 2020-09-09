#Link: https://edabit.com/challenge/xBPCwB8c4rYrGqY3v



def missing(lst):
	step = min(lst[1]-lst[0], lst[-1]-lst[-2])
	num = lst[0]
	while num in lst:		
		num+= step
	return num







print(missing([1.5,2, 3]))