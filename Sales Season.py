# Link: https://edabit.com/challenge/eznq7gLhLWmKKdsx9




def discount(lst):
	free = sorted(lst)[:len(lst)//3]
	percent = (sum(free)/sum(lst))
	return [round(x-percent*x,2) for x in lst]




print(discount([14.15, 9.45, 3.72, 5.99, 8.13, 8.85]))