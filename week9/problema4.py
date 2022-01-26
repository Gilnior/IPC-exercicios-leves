# -*- coding: utf-8 -*-

from statistics import mode


inputed_value = None

inputed_values = []

while inputed_value != -1:
    if inputed_value is not None and inputed_value != -1:
        inputed_values.append(inputed_value)

    inputed_value = int(input(""))

print(mode(inputed_values))