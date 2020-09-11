#Link: https://edabit.com/challenge/xiB2Y4EzEEkXYQchs


def is_magic_square(square):
    total = sum(square[0])    
    square2 = list(map(list,zip(square)))
    diagonals = sum(square[x][x] for x in range(len(square)))== sum(square2[x][0][x] for x in range(len(square)))
    return all(total==sum(x) for x in square) and all(total==sum(x[0]) for x in square2) and diagonals
    




print(is_magic_square([
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]))