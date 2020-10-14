#Link:  https://edabit.com/challenge/AcEnqyHp9q3Dd92Hn



def multiply_nums(nums):	
	res = 1
	for x in nums.split(','):
		res*=int(x)
	return res
	




print(multiply_nums("1, 2, 3, 4"))