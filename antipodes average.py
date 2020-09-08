#Link: https://edabit.com/challenge/oF8T7Apf7jfagC4fD



def antipodes_average(lst):
	l = len(lst)//2
	left = lst[:l]
	right = lst[-l:][::-1]
	return [(a+b)/2 for a,b in zip(left,right)]









print(antipodes_average([1, 2, 3, 4]))