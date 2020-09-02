# Link: https://edabit.com/challenge/yuPWwSbCGPm2KzSzx

# Create a class Smoothie and do the following:

# • Create an instance attribute called ingredients.
# • Create a get_cost method which calculates the total cost of the ingredients used to make the smoothie.
# • Create a get_price method which returns the number from get_cost plus the number from get_cost
#   multiplied by 1.5. Round to two decimal places.
# • Create a get_name method which gets the ingredients and puts them in alphabetical order into a
#   nice descriptive sentence. If there are multiple ingredients, add the word 'Fusion' to the end 
#   but otherwise, add 'Smoothie'. Remember to change '-berries to '-berry'.



class Smoothie:
	# Write code here!
	def __init__(self,ingredients):
		self.ingredients = ingredients
		self.cost = sum([float(prices[x] [1:]) for x in self.ingredients])
		self.price = self.cost*2.5	
	def get_cost(self):		
		return '$'+ '{:0.2f}'.format(self.cost)
	def get_price(self):		
		return '$'+ '{:0.2f}'.format(self.price)
	def get_name(self):
		fruits = sorted([x.replace('ies','y') for x in self.ingredients])
		return ' '.join(fruits) + (' Smoothie' if len(fruits)==1 else ' Fusion')


s1 = Smoothie(["Banana"])
s2 = Smoothie(["Raspberries", "Strawberries", "Blueberries"])
s3 = Smoothie(["Mango", "Apple", "Pineapple"])
s4 = Smoothie(["Pineapple", "Strawberries", "Blueberries", "Mango"])
s5 = Smoothie(["Blueberries"])

print(s2.get_cost())
print(s2.get_name())