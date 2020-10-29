# Watson gives Sherlock an array of integers. His challenge is to find an element 
# of the array such that the sum of all elements to the left is equal to the sum 
# of all elements to the right. For instance, given the array arr= [5,6,8,11], 8
# is between two subarrays that sum to 11. If your starting array is [1], that
# element satisfies the rule as left and right sum to 0.

# You will be given arrays of integers and must determine whether there is an element
# that meets the criterion.


# It should return a string, either YES if there is an element meeting the criterion 
# or NO otherwise.



def balancedSums(arr):
	for x in range(len(arr)):
		if sum(arr[:x])==sum(arr[x+1:]):
			return 'YES'
	return 'NO'




print(balancedSums([1,2,3]))

print(balancedSums([1,2,3,3]))

print(balancedSums([1,1,4,1,1]))

print(balancedSums([2,0,0,0]))

print(balancedSums([0,0,2,0]))