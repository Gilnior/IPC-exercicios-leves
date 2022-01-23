# -*- coding: utf-8 -*-

def imprime_naturais_pares(n, m=0):
    if n == m:
        print(n)
    else:
        if m % 2 == 0: print(m)
        imprime_naturais_pares(n, m+1)

n = int(input("Digite N:  ")) # 4

imprime_naturais_pares(n)