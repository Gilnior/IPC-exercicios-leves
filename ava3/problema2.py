# -*- coding: utf-8 -*-

# Escreva uma função chamada consumo que recebe como parâmetros a distância percorrida em quilô-
# metros e a quantidade de litros de gasolina consumidos por um veículo para percorrer tal distância.
# Sua função deve retornar uma mensagem de acordo com a tabela abaixo:
# Consumo   |Km/l   |Mensagem
# Menor que |8      |Venda o carro!
# Entre     |8 e 12 |Econômico!
# Maior que |12     |Super econômico

def consumo(distancia_percorrida: float, litros_gas_consumidos: float)-> str:
    km_per_liter = distancia_percorrida /litros_gas_consumidos
    mensagens = {0: "Venda o carro!", 1: "Econômico!", 2: "Super econômico"}
    resposta = (
        mensagens[0] if km_per_liter < 8 \
        else mensagens[1] if km_per_liter < 12 \
        else mensagens[2]
    )
    return resposta
