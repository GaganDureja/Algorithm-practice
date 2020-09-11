#Link: https://edabit.com/challenge/u9nd9D3HYcLxNZr7x


def group_monotonic(a):
    if len(a): return []
    res = []
    increase = 1 if a[1]>a[0] else 0
    for x in range(1,len(a)):
        if increase and a[x]<a[x-1]:            
            res.append(x-1)
            increase=0
        elif not increase and a[x]>a[x-1]:            
            res.append(x-1)
            increase=1
    return res

    

print(group_monotonic([0,1,1,0]))
print(group_monotonic([]))


print(group_monotonic([2,1,0]))
print(group_monotonic([0, 6, 10, 9, 3, -3, -9, -10, -6, 0]))