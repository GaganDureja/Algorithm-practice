# Implement an autocomplete system. That is, given a query string s 
# and a set of all possible query strings, return all strings in the
# set that have s as a prefix.












def autocomplete(lst,txt):
	return [x for x in lst if x.startswith(txt)]




print(autocomplete(['dog', 'deer', 'deal'], 'de'))