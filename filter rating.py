#Link:  https://edabit.com/challenge/qM6zWQM7gdfPgE9Hh



def filter_by_rating(d, rating):
	res = {key:value for key,value in d.items() if value==rating}
	return res or "No results found"




print(filter_by_rating({
  "Luxury Chocolates" : "*****",
  "Tasty Chocolates" : "****",
  "Aunty May Chocolates" : "*****",
  "Generic Chocolates" : "***"
}, "*****"))