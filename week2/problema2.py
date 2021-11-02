# -*- coding: utf-8 -*-

vel_max = float(input("Digite o valor da velocidade máxima: "))  # 60
vel_reg = float(input("Digite o valor da velocidade registrada: "))  # 60

fracao = vel_reg / vel_max

nivel_infracao = {0: "Sem Infração", 1: "Infração Média", 2: "Infração Grave", 3: "Infração Gravíssima"}

if not fracao > 1:
	print(nivel_infracao[0])
elif not fracao  > 1.2:
	print(nivel_infracao[1])
elif not fracao > 1.5:
	print(nivel_infracao[2])
else:
	print(nivel_infracao[3])

