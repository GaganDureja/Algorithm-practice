# Compute the running median of a sequence of numbers. That is, given a stream
# of numbers, print out the median of the list so far on each new element.

# Recall that the median of an even-numbered list is the average of the two
# middle numbers.






def median(lst):
	half_len = 	len(lst)//2	
	med = sorted(lst)[half_len]
	return med if len(lst)%2 else ((med+ sorted(lst)[half_len-1])/2)





lst = [2,1,5,7,2,0,5]

for x in range(1,len(lst)+1):
	print(median(lst[:x]))