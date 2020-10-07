#Link: https://edabit.com/challenge/c4WKPr4upiKx8GwJK



def duplicate_nums(nums):
	res = [x for x in nums if nums.count(x)>1]
	return sorted(list(set(res))) if res else None
	







print(duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54]))