#Link: https://edabit.com/challenge/LL9RJMMqKD9fCB2HN



class Stack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def push(self, element):
        self.data.append(element)

    def peek_top(self):
        if self.size() == 0:
            return "Stack Is Empty"
        return self.data[-1]

    def pop(self):
        if self.size() == 0:
            return "Stack Is Empty"
        return self.data.pop()



def is_palindrome(word):
 	stack = Stack()
 	for x in word:
 		stack.push(x)
 	res = ''
 	while stack.size()!=0:
 		res +=stack.pop()
 	return res==word








print(is_palindrome('radar'))