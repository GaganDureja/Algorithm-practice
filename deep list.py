#Link:  https://edabit.com/challenge/nn7Na6zHLEHS9R8j2



def deep_count(lst):
    counter = 0
    for element in lst:
        if isinstance(element, list):
            counter += 1
            counter += deep_count(element)
        else:
            counter +=1
    return counter






print(deep_count([[1], [2], [3]]))