# This problem was asked by LinkedIn.

# Given a string, return whether it represents a number. Here are the different kinds of numbers:

# "10", a positive integer
# "-10", a negative integer
# "10.1", a positive real number
# "-10.1", a negative real number
# "1e5", a number in scientific notation
# And here are examples of non-numbers:

# "a"
# "x 1"
# "a -2"
# "-"
















def validate_number(n):
	lst = []
	try:
		lst.append(int(n))
	except ValueError:
		pass

	try:
		lst.append(float(n))
	except ValueError:
		pass
	
	return len(lst)>0



print(validate_number("10"))
print(validate_number("-10"))
print(validate_number("10.1"))
print(validate_number("-10.1"))
print(validate_number("1e5"))


print(validate_number("a"))
print(validate_number("x 1"))
print(validate_number("a -2"))
print(validate_number("-"))