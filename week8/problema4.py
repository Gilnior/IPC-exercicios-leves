# -*- coding: utf-8 -*-

def soma(n, m=1):
    if n == m:
        return n
    else:
        return m + soma(n, m+1)


n = int(input("Digite N: "))  # 4

print(soma(n))
