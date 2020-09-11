#Link:  https://edabit.com/challenge/vcxcY5cKC7Cfkt7fi



from math import ceil
def roundabout(siz, dgr):
    return 'Exit %s'%(ceil((dgr+30)%360 /(360/siz))%siz)

    





print(roundabout(4, 320))