#Link: https://edabit.com/challenge/3ex9eCDEBqdxvfQvD




def are_true(a, b):
	return 'both' if a and b else 'first' if a else 'second' if b else 'neither'





print(are_true(True, True))
print(are_true(True, False))
print(are_true(False, True))
print(are_true(False, False))