# -*- coding: utf-8 -*-
nums = []
n = 1
while n >= 0:
    n = input("Digite um número: ")
    n = int(n) if n.isnumeric else 0
    if n >= 0: nums.append(n)

nums.sort()

print(f"Maior: {nums[-1]}\nMenor: {nums[0]}")
