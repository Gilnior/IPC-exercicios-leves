# -*- coding: utf-8 -*-

frase = input("Frase embaralhada: ") # I ENIL SIHTHSIREBBIG S

fra = frase[:len(frase)//2-1:-1]

se = frase[len(frase)//2-1::-1]

correta = se+fra

print("Frase correta:", correta) # THIS LINE IS GIBBERISH
