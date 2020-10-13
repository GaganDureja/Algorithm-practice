#Link:  https://edabit.com/challenge/NZH544exC2stzCycu





def unique_fract():
	lst= []
	for x in range(1,10):
		for y in range(1,10):
			num=x/y 
			if 1>num>0 and num not in lst:				
				lst.append(num)
	return sum(lst)







print(unique_fract())