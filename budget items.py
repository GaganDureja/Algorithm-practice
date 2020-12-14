Link:  https://edabit.com/challenge/9ZAk3EEoQ9YPGGYhA


def items_purchase(store, wallet):
	lst = []
	for x in store:
		price = int((store[x][1:]).replace(',',''))
		if price<= int(wallet[1:]):
			lst.append(x)
	return lst if lst else 'Nothing'

	
print(items_purchase({"Water": "$1", "Bread": "$3", "TV": "$1,000","Fertilizer": "$20"}, "$300"))

