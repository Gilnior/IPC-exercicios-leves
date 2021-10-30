# -*- coding: utf-8 -*-

# Pedro, João e Marcela jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcio-
# nalmente ao valor que cada um deu para a realização da aposta. Escreva um programa que solicita
# ao usuário quanto cada apostador investiu e o valor do prêmio, e então o programa deve imprimir na
# tela quanto cada um ganharia do prêmio com base no valor investido.

aposta_pedro = float(input("Digite o valor que o Pedro apostou: ")) # 1.5
aposta_john = float(input("Digite o valor que o João apostou: ")) # 4.0
aposta_marcela = float(input("Digite o valor que a Marcela apostou: ")) # 5.0
total_apostado = sum([aposta_john, aposta_marcela, aposta_pedro])

premio = float(input("Digite o valor do prêmio: ")) # 500000

print(f"Prêmio do Pedro: {((aposta_pedro/total_apostado)*premio):.2f}") # 71428.57
print(f"Prêmio do João: {((aposta_john/total_apostado)*premio):.2f}") # 190476.19
print(f"Prêmio da Marcela: {((aposta_marcela/total_apostado)*premio):.2f}") # 238095.24
