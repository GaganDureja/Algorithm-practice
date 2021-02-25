# This problem was asked by Microsoft.

# Let's represent an integer in a linked list format by having each node represent a digit in the number.
# The nodes make up the number in reversed order.

# For example, the following linked list:

# 1 -> 2 -> 3 -> 4 -> 5
# is the number 54321.

# Given two linked lists in this format, return their sum in the same linked list format.

# For example, given

# 9 -> 9
# 5 -> 2
# return 124 (99 + 25) as:

# 4 -> 2 -> 1
















def int_lst(*lst):
	res = []
	for x in lst:		
		res.append(int(''.join(str(y) for y in x[::-1])))		
	return [int(x) for x in str(res[0])] if len(res)==1 else [int(x) for x in str(sum(res))[::-1]]
	



print(int_lst([1,2,3,4,5]))
print(int_lst([9,9],[5,2]))

