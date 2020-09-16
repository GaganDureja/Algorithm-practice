#Link: https://edabit.com/challenge/kSmkcYLcWRnEEwXwX




def calculate_losses(items):
	res = sum(value for key,value in items.items())
	return res if res else 'Lucky you!'





print(calculate_losses({
  "tv": 30,
  "skate": 20,
  "stereo": 50,
}))