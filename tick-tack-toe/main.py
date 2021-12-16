from typing import Match


class Tabuleiro:
    def __init__(self):
        self.mapa = {k: ' ' for k in "abcdefghi"}
        self.game = " {a} | {b} | {c} \n---+---+---\n {d} | {e} | {f} \n---+---+---\n {g} | {h} | {i} "
        self.marcas = {'X', 'O'}
        self._game = self.game.format_map(self.mapa)

    def marcar(self, coordenada, marca):
        self.mapa[coordenada]= marca

    def get_marca(self):
        return self.marcas.pop()


class Player:
    def __init__(self, tabuleiro: Tabuleiro):
        self.tabuleiro = tabuleiro
        self.marca = self.tabuleiro.get_marca()

    def marcar(self, coordenada):
        self.tabuleiro.marcar(coordenada, self.marca)

def main():

    tabuleiro = Tabuleiro()
    
    print(tabuleiro._game)
