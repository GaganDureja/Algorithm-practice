# Leetcode: https://leetcode.com/explore/featured/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/

# Given an array of integers arr, return true if and only if 
# it is a valid mountain array.








def valid_mountain(lst):
	res = [[lst[0]]]
	for x in range(1,len(lst)):
		if lst[x]>res[-1][-1]:
			res[-1].append(lst[x])
		elif lst[x]<res[-1][-1]:
			res.append(lst[x:])
			break
		else:
			return False
	if len(res)!=2 or len(res[0])<2:
		return False
	return (len(res[0])==len(set(res[0])), len(res[1])==len(set(res[1])),res[0]==sorted(res[0]), res[1][::-1]==sorted(res[1])).count(True)==4
		
	













print(valid_mountain([0,3,2,1]))
print(valid_mountain([3,5,5]))
print(valid_mountain([9,8,7,6,5,4,3,2,1]))



