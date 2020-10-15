a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)

print("=========")
a1 = [1,2,3]
b1 = [4,5,6]
c1 = a1 + b1
print(c1)
print(a1)

print("=========")

a2 = [1,2,3]
b2 = [4,5,6]
a2[len(a2):] = b2
print(a2)
print("=========")
