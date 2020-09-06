#Link: https://edabit.com/challenge/YGhrwfg6k6zHnmeDh



def get_discounts(nums, d):
	return [x*(int(d[:-1])/100) for x in nums]






print(get_discounts([2, 4, 6, 11], "50%"))