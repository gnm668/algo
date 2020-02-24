# print('pick a number')
# num1 = input()
# print('pick another number')
# num2 = input()

# print(num1 + num2)

# print(type(4))
# print(type([4]))
# print(type('4'))
# print(type(4.4))
# print(type({4: 4}))

#  list.index(ELEMENT)
#  list.insert(INDEX, ELEMENT)
#  del list[INDEX]
#  list.pop(INDEX -- DEFAULT -1)
#  list.remove(ELEMENT)
a = ['car', 'boat', 'airplane']
# print(a.index('boat'))
# a.insert(1, 'skate')
# print(a)
# del a[2]
# print(a)
# print(a.pop())
# print(a)


b = [1,2,3,4]
b[0:2] = 'b'
# print(b)
# interesting slice assignment...

c = [6,4,2,31,10,2]
# sorted(LIST) will not mutate original list
# c.sort() will mutate original list
# print(sorted(c))
# print(c)
# c.sort()
# print(c)

d = [5,4,3,2,1]
# d = d[::-1]
# d.reverse()
# print(d)


e = ['apple', 'Apple', 'boo', 'Baack', 'BLip']
# e.sort()
# print(sorted(e))
# print(e)

# weird sort behavior with caps in strings

f = 'hello'
# print(d.find('o'))
# print(d.count('l'))

g = ['h', 'e', 'l', 'l', 'o']
# print(g.find('e'))
print(g.count('l'))

# find is only for strings, count works on both