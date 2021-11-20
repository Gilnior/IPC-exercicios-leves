# -*- coding: utf-8 -*-

# Escreva um função chamada fizz_buzz que recebe como parâmetro um número inteiro e retorna
# um número inteiro ou uma string de acordo com as regras abaixo:
# 1. Se o número é divisível por 3, a função deve retornar a string "Fizz".
# 2. Se o número é divisível por 5, a função deve retornar a string "Buzz".
# 3. Se o número é divisível por 3 e por 5, a função deve retornar a string "FizzBuzz".
# 4. Senão, a função deve retornar o mesmo número inteiro que recebeu como parâmetro.

def fizz_buzz(num: int):
    resposta = "FizzBuzz" if (num % 15 == 0) else "Fizz" if num % 3 == 0 \
        else "Buzz" if num % 5 == 0 else num
    
    return resposta
