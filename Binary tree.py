#Link:  https://edabit.com/challenge/Cp3JRpooAqfA4kGkv



def node_type(_N, _P, n):
    if n not in _N: return 'Not exist'
    root = _N[_P.index(-1)]
    leaf = [x for x in _N if x not in _P]    
    return 'Root' if n==root else 'Leaf' if n in leaf else 'Inner'






print(node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 5))