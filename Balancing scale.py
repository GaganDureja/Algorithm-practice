#Link: https://edabit.com/challenge/xPmfKHShmuKL5Qf9u


def scale_tip(lst):
	left = sum(lst[:lst.index('I')])
	right = sum(lst[lst.index('I')+1:])
	return 'balanced' if left==right else 'left' if left>right else 'right'
	





print(scale_tip([0, 0, "I", 1, 1]))