# -*- coding: utf-8 -*-

# Escreva uma função chamada estacionamento que recebe como parâmetros a hora e minuto de
# entrada e hora e minuto de saída de um estacionamento e retorna o valor total devido de acordo com
# as seguintes regras:
# Quantidade de Horas Tarifa
# Até duas horas R$ 1.00 para cada hora
# Entre três e quatro horas R$ 1.40 para cada hora
# Acima de quatro horas R$ 2.00 para cada hora
# O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo, quem estacionar
# durante 61 minutos pagará por 2 horas. Os momentos de chegada e partida do estacionamento são
# apresentados na forma de pares de inteiros, representando horas e minutos. Por exemplo, o par 12
# 50 representará "dez para a uma da tarde". Admite-se que a chegada e a partida se dão com intervalo
# não superior a 24 horas.

import datetime


def estacionamento(hora_entrada: int, minuto_entrada: int, hora_partida: int, minuto_partida: int):
    tempo_entrada = datetime.datetime(year=2021, month=6, day=17, hour=hora_entrada, minute=minuto_entrada)
    tempo_partida = datetime.datetime(year=2021, month=6, day=18 if hora_partida<hora_entrada else 17, hour=hora_partida, minute=minuto_partida)

    tempo_total = (tempo_partida - tempo_entrada).seconds/3600
    tempo_total = tempo_total if tempo_total.is_integer() else int(tempo_total) + 1

    a_pagar_por_hora = (
        1 if tempo_total <= 2 \
        else 1.4 if  tempo_total <=4 \
        else 2
    )

    preco = tempo_total * a_pagar_por_hora

    return preco
