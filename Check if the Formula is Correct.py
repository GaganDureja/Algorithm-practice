# Link: https://edabit.com/challenge/abEZ5AEPaDBHFjfJG


# Create a function that takes a string and returns True or False depending on whether or not the 
# given formula is correct.



def formula(txt):
	txt=txt.replace('=','==').replace('a','4')
	return eval(txt)



print(formula("6 * 4 = 24"))
print(formula('(1+2+3+4+5+6+7+8)/a=9'))
