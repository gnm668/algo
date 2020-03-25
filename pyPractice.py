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
# print(g.count('l'))

# find is only for strings, count works on both

# h = ['car', 'skate', 'boat', 'plane']

# for idx, el in enumerate(h):
#     print(el, idx)

# for idx in range(len(h)):
#     print(h[idx], idx)

# ways = [0 for x in range(10)]
# print(ways)

# i = g[:]
# print(i)

# print([float('inf') for value in range(10)])


def check_sudoku(grid):
    results = []
    
    results.append(check_col(grid))
    results.append(check_row(grid))
    
    if False in results: 
        return False
    else:
        return True
    
def check_col(grid):
    for i in range(len(grid[0])):
        counter = {}
        for j in range(len(grid)):
            value = grid[j][i]

            if value not in range(1,len(grid) + 1): return False

            if value in counter:
                counter[value] += 1
            else:
                counter[value] = 1
    
        print(counter)
        for value in list(counter.values()):
            if value > 1:
                return False
    return True
            
def check_row(grid):
    for i in range(len(grid)):
        counter = {}
        for j in range(len(grid[0])):
            value = grid[i][j]
            
            if value not in range(1,len(grid) + 1): return False

            if value in counter:
                counter[value] += 1
            else:
                counter[value] = 1

        # print(counter)
        for value in list(counter.values()):
            if value > 1:
                return False
    return True


correct = [[1,2,3],
            [2,3,1],
            [3,1,2]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

    
print(check_sudoku(incorrect2))
