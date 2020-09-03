#Link: https://edabit.com/challenge/uojwbCn2yyqqk9Wpf

def is_untouchable(number):
	if number<2:
		return 'Invalid Input'
	mul = number**2 +1
	lst = [1]*mul
	for x in range(2,mul):
		for y in range(x*2,mul,x):
			lst[y]+=x
	if number not in lst:
		return True
	return [x for x in range(len(lst)) if lst[x]==number]






print(is_untouchable(6))