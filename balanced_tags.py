# Given a string of round, curly, and square open and closing brackets, return
# whether the brackets are balanced (well-formed).

# For example, given the string "([])[]({})", you should return true.

# Given the string "([)]" or "((()", you should return false.












def balnced(txt):
	lst = []
	for x in txt:
		if x in ['(','[','{']:
			lst.append(x)
		else:
			if not lst:
				return False
			last_char = lst.pop()
			if last_char == '(' and x!=')':
				return False
			if last_char == '{' and x!='}':
				return False
			if last_char == '[' and x!=']':
				return False
	if lst:
		return False
	return True
	return [txt.count(x)%2==0 for x in txt]




print(balnced('[]'))
print(balnced('([])[]({})'))