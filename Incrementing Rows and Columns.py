# Link: https://edabit.com/challenge/8BQKa98d3s9Kis4vv


# Write a function that takes in three parameters: r, c, i, where:

# • r and c are the number of rows and columns to initialize a zero matrix.
# • i represents the list of incrementing operations (+1).
# And returns the resulting matrix after applying all the increment operations.
# Each increment operation will add 1 to the rows or columns specified in the incrementing list.



def final(r, c, i):
	matrix = []
	for x in range(r):
		matrix.append([])
		for y in range(c):
			matrix[-1].append(0)

	for x in i:
		if x[1]=='r':			
			new_row= []
			for y in matrix[int(x[0])]:
				new_row.append(y+1)
			matrix[int(x[0])] = new_row			
		else:
			for a in range(len(matrix)):
				matrix[a][int(x[0])]+=1


	return matrix





print(final(3,3, ["2r", "2c", "1r", "0c"]))