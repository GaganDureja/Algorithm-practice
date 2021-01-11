# This problem was asked by Yelp.

# Given a mapping of digits to letters (as in a phone number), and a digit string,
# return all possible letters the number could represent. You can assume each valid
# number in the mapping is a single digit.

# For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should
# return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].










phn_map = {'2': 'abc','3': 'def','4': 'ghi','5': 'jkl','6': 'mno','7': 'pqrs','8': 'tuv','9': 'wxyz'}

def word_numbers(n): 
  	res = ['']
  	for char in str(n):
  		letters = phn_map[char]
  		res = [prefix+letter for prefix in res for letter in letters]
  	return res










print(word_numbers(23))
print(word_numbers(523))
