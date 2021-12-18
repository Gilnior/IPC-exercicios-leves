# -*- coding: utf-8 -*-

def tamanho_maior_string(l: list):
    m = max([len(s) for s in l]) if l else 0
    return m
