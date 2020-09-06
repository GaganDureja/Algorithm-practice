#Link: https://www.hackerrank.com/challenges/quicksort1/problem


def quickSort(arr):
	left, right= [],[]
	for num in arr[1:]:
		if num < arr[0]:
			left.append(num)
		else:
			right.append(num)
	return left + [arr[0]] + right
	





print(quickSort([4,5,3,7,2]))