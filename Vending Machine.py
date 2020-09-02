# Link: https://edabit.com/challenge/dKLJ4uvssAJwRDtCo


# Your task is to create a function that simulates a vending machine.

# Given an amount of money (in cents ¢ to make it simpler) and a product_number, 
#the vending machine should output the correct product name and give back the correct amount of change.

# The coins used for the change are the following: [500, 200, 100, 50, 20, 10]

# The return value is a dictionary with 2 properties:

# product: the product name that the user selected.
# change: an array of coins (can be empty, must be sorted in descending order).







def vending_machine(products, money, product_number):
	if product_number not in range(1,10):
		return 'Enter a valid product number'
	if money < products[product_number-1]['price']:
		return 'Not enough money for this product'

	lst = [500,200,100,50,20,10]
	count = 0
	money-= products[product_number-1]['price']
	change = []
	while money!=0:
		if money-lst[count]>=0:
			money-=lst[count]
			change.append(lst[count])
		else:
			count+=1
	return {'product':products[product_number-1]['name'], 'change': change}
	


# Products available
products = [
  	{ 'number': 1, 'price': 100, 'name': 'Orange juice' },
  	{ 'number': 2, 'price': 200, 'name': 'Soda' },
  	{ 'number': 3, 'price': 150, 'name': 'Chocolate snack' },
  	{ 'number': 4, 'price': 250, 'name': 'Cookies' },
  	{ 'number': 5, 'price': 180, 'name': 'Gummy bears' },
  	{ 'number': 6, 'price': 500, 'name': 'Condoms' },
  	{ 'number': 7, 'price': 120, 'name': 'Crackers' },
  	{ 'number': 8, 'price': 220, 'name': 'Potato chips' },
  	{ 'number': 9, 'price': 80,  'name': 'Small snack' }
]



print(vending_machine(products, 500, 8))