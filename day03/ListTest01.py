a = list('Hello')
print(a)
x = [1,1,1]
x[1] = 2
print(x)

names = ['Alice','Beth','Cecil','Dee-Dee','Earl']
del names[2]
print(names)

name = list('Perl')
name[1:] = list('ython')
print(name)

numbers = [1,5]
numbers[1:4] = []
print(numbers)

lst = [1,2,3]
lst.append(4)
print(lst)

lst2 = [1,2,3]
lst2.clear()
print(lst2)

c = [1,2,3]
b = c
b[1] = 4
print(c)

a1 = [1,2,3]
b1 = a1.copy()
b1[1] = 4
print(a1)




