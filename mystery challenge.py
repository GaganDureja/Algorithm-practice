#Link: https://edabit.com/challenge/uCKJi6X3KTH9zuSc3


def mystery_func(n):    
    n=str(n)
    res = [n[0]]
    for x in range(1,len(n)):
        if n[x]==n[x-1]:
            res[-1]+=n[x]
        else:
            res.append(n[x])
    return ''.join([''.join([str(len(x)),x[0]]) for x in res])


    





print(mystery_func(5211255))