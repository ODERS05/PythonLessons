import copy
def chop(numbers):
    numbers.pop(0)
    numbers.pop()
    return None
def middle(numbers):
    new_list = copy.copy(numbers)
    return new_list[1:3]
numbers1 = [1, 2, 3, 4]
print("My list before call chop function => ", numbers1)
chop(numbers1)
print("My list after call chop function => ",numbers1)
numbers2 = [1,2,3,4]
print("My list before call middle function =>", numbers2)
new_list = middle(numbers2)
print("My list after call middle function =>", numbers2)
print("new list after call middle function =>", new_list)
