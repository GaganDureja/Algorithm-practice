#Link: https://edabit.com/challenge/F4iemEeFfsaFoMpAF






# Not working on site showing Hi!\x00 but working fine on terminal
def cpp_txt(lst):
	return ''.join(lst)



# working successfully
# def cpp_txt(lst):
# 	return ''.join(lst)[:len(lst)-1]



print(cpp_txt(["P","y","T","h", "O", "n","\0"]))
print(cpp_txt(["H", "i", "!", "\0"]))