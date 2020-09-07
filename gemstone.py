#Link: https://www.hackerrank.com/challenges/gem-stones/problem


def gemstones(arr):
	return len([x for x in set(arr[0]) if all(x in y for y in arr)])
	







print(gemstones(['abcdde', 'baccd', 'eeabg']))