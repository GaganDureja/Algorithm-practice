# Link: https://www.hackerrank.com/challenges/strange-code/problem


def strangeCounter(t):
    t1 = 3
    while(t1 < t):
        t -= t1
        t1 *= 2    
    return t1 - t + 1


print(strangeCounter(17))