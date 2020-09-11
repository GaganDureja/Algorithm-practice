#Link: https://edabit.com/challenge/4hFDo2uytDJmvKMfG




def happy_algorithm(num):
    if num==1: return 'HAPPY 1'
    lst = [num]
    while 1 not in lst:        
        num = sum(int(x)**2 for x in str(num))
        if num not in lst:
            lst.append(num)
        else:
            break
    return ('HAPPY' + ' %s'%(len(lst)-1)) if num==1 else 'SAD' + ' %s'%len(lst)
    



print(happy_algorithm(1))
print(happy_algorithm(139))
print(happy_algorithm(67))
print(happy_algorithm(89))