# -*- coding: utf-8 -*-

# Escreva um programa que solicita ao usuário um montante inicial de investimento (v p), uma taxa de
# juros anual (i ) e o número de anos (n) que durará esse investimento. O programa deverá imprimir na
# tela o valor futuro (v f ) do investimento. Considere a seguinte fórmula:

# • v f =v p ×(1+(i ×0.01))n

vp = float(input("Digite o valor do investimento inicial: "))
i = float(input("Digite a taxa de juros anual: "))
n = float(input("Digite o período do investimento em anos: "))

print(f"Valor futuro: {round((vp*(1+(i*0.01))**n), 2)}")
