list1 = ["hello", "hi", "mushi", "fdaf", 1, 3, 4, 5]
print(type(list1))
print(list1)

print(list1[0])
print(list1[1])
print(list1[2])

print(list1[3:])
print(list1[:3])
print(list1[1:5])

list1[0] = "mingalarbar"
print(list1)

list1.append(100)
print(list1)

list1.pop()
print(list1)

del list1[0]
print(list1)