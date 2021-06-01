 # This problem was asked by Zillow.

 # Let's define a "sevenish" number to be one which is either a power of 7,
 # or the sum of unique powers of 7. The first few sevenish numbers are 1, 
 # 7, 8, 49, and so on. Create an algorithm to find the nth sevenish number.








def sevenish(n):
	return n%7==1 or n%7==0
	



print(sevenish(1))
print(sevenish(7))
print(sevenish(8))
print(sevenish(9))
print(sevenish(49))
print(sevenish(52))
print(sevenish(364))
print(sevenish(371))
