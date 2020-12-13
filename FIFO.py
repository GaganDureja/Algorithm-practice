lst = [1,2,3,4,5,6]

def enqueue(x):
	return lst.append(x)

def dequeue():
	return lst.pop(0)

enqueue(15)
dequeue()
enqueue(200)



print(lst)


