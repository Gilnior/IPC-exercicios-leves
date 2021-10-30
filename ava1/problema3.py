# -*- coding: utf-8 -*-

# Escreva um programa que solicita ao usuário um número inteiro e então o programa imprime na tela
# a soma do sucessor de seu triplo com o antecessor de seu dobro

num = int(input("Digite um número: "))

print(f"Resultado: {sum([num*3+1, num*2-1])}")
