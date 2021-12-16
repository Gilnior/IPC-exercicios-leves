class Tabuleiro:
    def __init__(self):
        self.mapa = {k: ' ' for k in "abcdefghi"}
        self.game = " {a} | {b} | {c} \n---+---+---\n {d} | {e} | {f} \n---+---+---\n {g} | {h} | {i} "
        self.marcas = {'X', 'O'}
        self._game = self.game.format_map(self.mapa)
        self.posicoes_ocupadas = set()
        self.len_posicoes_ocupadas = 0

    def marcar(self, coordenada, marca):
        self.mapa[coordenada]= marca
        self.posicoes_ocupadas.add(coordenada)
        self.len_posicoes_ocupadas = self.get_posicoes_jogadas()

    def get_marca(self):
        return self.marcas.pop()

    def get_posicoes_jogadas(self):
        return len(self.posicoes_ocupadas)
        

class Player:
    def __init__(self, tabuleiro: Tabuleiro):
        self.tabuleiro = tabuleiro
        self.marca = self.tabuleiro.get_marca()

    def marcar(self, coordenada):
        self.tabuleiro.marcar(coordenada, self.marca)


class Game:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.jogador_x = Player(self.tabuleiro)
        self.jogador_o = Player(self.tabuleiro)
        self.turno = self.jogador_x
        self.winner = ""

    def start(self):
        while self.tabuleiro.len_posicoes_ocupadas != 9 and not self.winner:
            print(self.tabuleiro._game)
            print("Vez do jogador", self.turno.marca)

            valido = False
            while not valido:
                coordenada = input("Digite onde quer jogar: ").strip()
                valido = coordenada not in self.tabuleiro.posicoes_ocupadas \
                    and coordenada in self.tabuleiro.mapa.keys()

            self.turno.marcar(coordenada)
            self.turno = self.jogador_x if self.turno.marca==self.jogador_o.marca else self.jogador_o

    # TODO method to check if someone won the game
    def has_winner(self):
        pass

if __name__=="__main__":
    Game.start()