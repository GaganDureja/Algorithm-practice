# Given an array of integers, return a new array such that each element at index i
# of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

#Follow-up: what if you can't use division?




def product(lst):
	num = 1
	for x in lst:
		num*=x
	return num


def exceptional_product(lst):
	return [product(lst[:x]+lst[x+1:]) for x in range(len(lst))]


	




print(exceptional_product([1, 2, 3, 4, 5]))

print(exceptional_product([3, 2, 1]))