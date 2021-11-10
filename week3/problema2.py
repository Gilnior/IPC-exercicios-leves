# -*- coding: utf-8 -*-

def pagamento(valor_hora: float, horas: int) -> float:
    """
    Função que recebe o valor hora e as horas trabalhadas como
    parâmetros e retorna o valor do salário com o IRPF já descontado
    """
    bruto = valor_hora * horas
    irpf = 0 if bruto <= 900 else 0.05 if bruto <= 1500 else 0.1 if bruto <= 2500 else 0.2

    return bruto - bruto * irpf 
