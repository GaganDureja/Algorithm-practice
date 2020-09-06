#Link: https://edabit.com/challenge/GaXXfmpM72yCHag9T


def unique(lst):
  return [x for x in lst if lst.count(x)==1][0]



print(unique([3, 3, 3, 7, 3, 3]))