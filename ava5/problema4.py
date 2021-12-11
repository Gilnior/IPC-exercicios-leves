# -*- coding: utf-8 -*-

palavra = input("Digite uma palavra: ") # cheer
nc = int(input("Digite o valor da chave: ")) # 7

just_apha = lambda x: x - 26 if x > 122 else x

resposta = ''.join([chr(just_apha(ord(s)+nc)) for s in palavra])

print("Resultado:", resposta) # jolly
