#Link:  https://edabit.com/challenge/iG5vcwd282T4t7h6r



def str_to_dict(lst):
	lst1 = [x.split('=') for x in lst]
	return {x[0]:x[1] for x in lst1}







print(str_to_dict(["1=one", "2=two", "3=three", "4=four"]))