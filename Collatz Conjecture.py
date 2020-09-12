#Link: https://edabit.com/challenge/X8fNb5EouWxrMMjZL



def collatz(num):
	count = 0
	while num!=1:
		if num%2:num= num*3 +1
		else:num/=2
		count+=1
	return count


    





print(collatz(10))