# This problem was asked by Google.

# Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.











def sort_merge(lst):
    return sorted(sum(lst,[]))
lst = [[1,5,8],[0,2,6]]

print(sort_merge(lst))


