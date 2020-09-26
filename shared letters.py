#Link: https://edabit.com/challenge/XgJ3L3GF7o2dEaPAW



def shared_letters(a, b):
	return ''.join(sorted(set(a.lower()) & set(b.lower())))


print(shared_letters("House", "home"))