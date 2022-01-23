# -*- coding: utf-8 -*-

def imprime_naturais(n, m=0):
    if n == m:
        print(n)
    else:
        print(m)
        imprime_naturais(n, m+1)

n = int(input("Digite N:  ")) # 4

imprime_naturais(n)