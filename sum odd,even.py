#Link: https://edabit.com/challenge/5XXXppAdfcGaootD9



def sum_odd_and_even(lst):	
	return [sum(x for x in lst if x%2==0) ,sum(x for x in lst if x%2)]
	







print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))