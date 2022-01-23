# -*- coding: utf-8 -*-

def soma(m, n):
    if m == n:
        return m
    else:
        return m + soma(m+1, n)


m = int(input("Digite m: "))  # 1
n = int(input("Digite n: "))  # 4

print(soma(m, n))