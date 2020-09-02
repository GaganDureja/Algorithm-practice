# Link: https://edabit.com/challenge/C45TKLcGxh8dnbgqM

# Julius Caesar protected his confidential information by encrypting it using a cipher.
# Caesar's cipher (check Resources tab for more info) shifts each letter by a number of letters.
# If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet.
# In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

# Create a function that takes a string s (text to be encrypted) and an integer k (the rotation factor).
# It should return an encrypted string.


def caesar_cipher(s, k):
	txt = 'abcdefghijklmnopqrstuvwxyz'
	res = ''
	for x in s:
		if x.lower() in txt:
			new = txt[(txt.index(x.lower())+k)%26]
			res+= new if x.islower() else new.upper()
		else:
			res+=x
	return res




print(caesar_cipher("middle-Outz", 2))