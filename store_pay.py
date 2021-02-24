#Link:  https://edabit.com/challenge/phMpXM9nu52bCjguS












def change_enough(change, amount_due):
	lst = [25, 10, 5, 1]
	return sum([(change[x]*lst[x])/100 for x in range(4)])>=amount_due






print(change_enough([25, 20, 5, 0], 4.25))
print(change_enough([2, 100, 0, 0], 14.11))
print(change_enough([30, 40, 20, 5], 12.55))
print(change_enough([1, 0, 2555, 219], 127.75))

