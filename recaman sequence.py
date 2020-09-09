#Link: https://edabit.com/challenge/fW52x9Gh5iMKNfWMt


def recaman_index(n):
	lst = [0]
	while n not in lst:
		num1 = lst[-1]-len(lst)
		num2 = lst[-1]+len(lst)
		lst.append(num1 if num1>=0 and num1 not in lst else num2)
	return len(lst)-1








print(recaman_index(7))
