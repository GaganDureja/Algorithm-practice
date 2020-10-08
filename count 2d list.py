#Link: https://edabit.com/challenge/dWeA6vWdrPYtwhxoS




def count_number(lst):
	return sum([type(x)!=str if type(x)!=list else count_number(x) for x in lst])







print(count_number([["", 17.2, 5, "edabit"],22]))