#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#Bonus: Can you do this in one pass?






from itertools import combinations as cb
def sum_of_two(lst,k):
	return any(sum(x)==k for x in cb(lst,2))



	




print(sum_of_two([10, 15, 3, 7],17))

print(sum_of_two([10, 15, 3, 2],17))

print(sum_of_two([9, 10, 3, 7],18))

print(sum_of_two([9, 9, 3, 7],18))