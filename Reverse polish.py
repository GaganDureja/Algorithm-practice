#Link:  https://edabit.com/challenge/ofuahH9E4pcRDNChd



def rpn(lst):
    res = []
    for x in lst:
        if isinstance(x,str):
            b = res.pop()
            a = res.pop()
            res.append(eval(str(a)+x+str(b)))
        else:
            res.append(x)        
    return int(res[0])
        

    





print(rpn([9, 9, "*", 6, 6, "*", "-", 9, "/"]))