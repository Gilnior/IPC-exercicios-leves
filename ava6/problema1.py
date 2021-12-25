# -*- coding: utf-8 -*-

# a = set()
# b = set()

# for i in range(10):
#     if i <5:
#         a.add(input())
#     else:
#         b.add(input())

# print(sorted([int(n) for n in a.intersection(b)]))

a = [int(input()) for i in range(5)] 
b = [int(input()) for i in range(5)]

c = [x for x in a if x in b]

print('Interseção:', c)
