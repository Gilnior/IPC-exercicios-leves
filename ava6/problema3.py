# -*- coding: utf-8 -*-

n = int(input("Digite a dimensão: "))

a = [int(input()) for i in range(n)]
b = [int(input()) for i in range(n)]

r = 0

for i in range(n):
    r += a[i]*b[i]

print("Produto Escalar:", r)
