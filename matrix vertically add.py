#Link: https://edabit.com/challenge/kPKNb4c3QjCf5tHRM




table1 = [
 ['A', 'B', 'C'],
 [ 2 ,  7 ,  1 ],
 [ 3 ,  6 ,  6 ],
 [ 4 ,  5 ,  5 ]]
 
table2 = [
 ['W', 'X', 'Y', 'Z'],
 [ 3 ,  5 ,  7 ,  1 ],
 [ 4 ,  5 ,  2 ,  3 ]]
 
table3 = [
 ['R', 'T', 'V', 'W', 'C'],
 [ 2 ,  3 ,  7 ,  7 ,  4 ],
 [ 8 ,  5 ,  2 ,  9 ,  0 ],
 [ 2 ,  5 ,  8 ,  7 ,  4 ],
 [ 5 ,  3 ,  7 ,  2 ,  3 ]]

def total_sales(sales_table, product):
	return 'Product not found' if product not in sales_table[0] else sum(sales_table[x][sales_table[0].index(product)] for x in range(1,len(sales_table)))







print(total_sales(table1,'A'))
