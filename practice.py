# commonly used list methods with return type

list1=[2,3,4,1,32,4]
list1.append(19)
print(list1)

print(list1.count(4))

list2=[99,54]
list1.extend(list2)
print(list1)

print(list1.index(4))

list1.insert(1,25)
print(list1)

print(list1.pop(2))

list1.remove(32)
print(list1)

list1.reverse()
print(list1)

list1.sort()
print(list1)



# list comprehension

list1 = [x for x in range(10)]
print(list1)

list1 = [x+1 for x in range(10)]
print(list1)

list1 = [x for x in range(10) if x%2 == 0]
print(list1)

# + and * operations in list

list1 = [11,33]
list2 = [1,9]
list3 = list1+list2
print(list3)

list4 = [1,2,3,4]
list5 = list4*3
print(list5)

# liat common operations
list1 = [2,3,4,1,30]
print(2 in list1)
print(2 not in list1)
print(len(list1))
print(min(list1))
print(max(list1))
print(sum(list1))

# list slicing
list = [11,22,33,44,66]
print(list[0:3])
print(list[:2])
print(list[:])
print(list[1:])