#Link: https://edabit.com/challenge/C3z6t5DxzZQLk3mRf




def tune(lst):
    frequencies = (329.63, 246.94, 196, 146.83, 110, 82.41)
    
    res = []
    for a, b in zip(frequencies, lst):
        if b == 0:
            res.append(' - ')
        else:
            diff = round((a-b)/b*100)
            if diff == 0:
                res.append('OK')
            elif diff < -2:
                res.append('+<<')
            elif diff in (-1, -2):
                res.append('+<')
            elif diff > 2:
                res.append('>>+')
            elif diff in (1, 2):
                res.append('>+')
    return res

    



print(tune([329, 246, 195, 146, 111, 82,0]))