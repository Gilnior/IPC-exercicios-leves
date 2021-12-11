# -*- coding: utf-8 -*-

s1 = input("Digite a primeira palavra: ") # Tpo
s2 = input("Digite a segunda palavra: ") # oCder

S = ''

for a, b in zip(s1, s2):
    S += a+b

if len(S) != len(s1+s2):
    S += s1[len(s2):] if len(s1) > len(s2) else s2[len(s1):]

print(f"Combinação: {S}") # TopCoder
