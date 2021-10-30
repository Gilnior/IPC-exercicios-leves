# -*- coding: utf-8 -*-

# Escreva um programa que solicita ao usuário um número inteiro de 4 algarismos e imprime na tela a
# soma destes algarismos.

num = input("Digite um inteiro de 4 algarismos: ")

print("Resultado: {}".format(sum([int(n) for n in num])))
