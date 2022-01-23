# -*- coding: utf-8 -*-

def imprime_naturais_impares(n, m=0):
    if m == 1:
        printa_se_impar(m)
    else:
        m = n if m == 0 else m
        printa_se_impar(m)
        imprime_naturais_impares(n, m-1)

def printa_se_impar(n):
    if not n % 2 == 0: print(n)

n = int(input("Digite N:  ")) # 4

imprime_naturais_impares(n)