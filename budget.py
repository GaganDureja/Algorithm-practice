# Link:  https://edabit.com/challenge/MSjfXQ4gvMzeezFgB



def fifty_thirty_twenty(ati):
	one_ten = ati//10
	return {'Needs':one_ten*5, 'Wants':one_ten*3, 'Savings':one_ten*2}



print(fifty_thirty_twenty(50000))
print(fifty_thirty_twenty(13450))