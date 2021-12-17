class Tabuleiro:
    def __init__(self):
        self.mapa = {k: ' ' for k in "qweasdzxc"}
        self.game = "\n {q} | {w} | {e} \n---+---+---\n {a} | {s} | {d} \n---+---+---\n {z} | {x} | {c} \n"
        self.marcas = {'X', 'O'}
        self.posicoes_ocupadas = set()
        self.len_posicoes_ocupadas = 0
        self.rows = [{'q','w', 'e'}, {'a', 's', 'd'}, {'z', 'x', 'c'}]
        self.columns = [{'q', 'a', 'z'}, {'w', 's', 'x'}, {'e', 'd', 'c'}]
        self.diagonals = [{'q', 's', 'c'}, {'z', 's', 'e'}]

    def marcar(self, coordenada, marca):
        self.mapa[coordenada]= marca
        self.posicoes_ocupadas.add(coordenada)
        self.len_posicoes_ocupadas = self.get_posicoes_jogadas()

    def get_marca(self):
        return self.marcas.pop()

    def get_posicoes_jogadas(self):
        return len(self.posicoes_ocupadas)
    
    def show(self):
        print(self.game.format_map(self.mapa))


class Player:
    def __init__(self, tabuleiro: Tabuleiro):
        self.tabuleiro = tabuleiro
        self.marca = self.tabuleiro.get_marca()

    def marcar(self, coordenada):
        self.tabuleiro.marcar(coordenada, self.marca)


class Game:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.jogador_1 = Player(self.tabuleiro)
        self.jogador_2 = Player(self.tabuleiro)
        self.turno = self.jogador_1
        self.winner = ""

    def start(self):
        print(self.tabuleiro.game)
        while self.tabuleiro.len_posicoes_ocupadas != 9 and not self.winner:
            self.tabuleiro.show()
            print("Vez do jogador", self.turno.marca)

            valido = False
            while not valido:
                coordenada = input("Digite onde quer jogar: ").strip()
                valido = coordenada not in self.tabuleiro.posicoes_ocupadas \
                    and coordenada in self.tabuleiro.mapa.keys()

            self.turno.marcar(coordenada)
            self.has_winner()
            self.turno = self.jogador_1 if self.turno.marca==self.jogador_2.marca else self.jogador_2

        self.tabuleiro.show()

        if self.winner:
            print(f"Jogador {self.winner} vence!")
        else:
            print("Empate...")

    # TODO method to check if someone won the game
    def has_winner(self):
        """
        Basicamente checa se as condições de vitória foram alcançadas pelo jogador que acabou de jogar
        """
        for row in self.tabuleiro.rows:
            if self.check_victory(row):
                self.winner = self.turno.marca

        for column in self.tabuleiro.columns:
            if self.check_victory(column):
                self.winner = self.turno.marca

        for diagonal in  self.tabuleiro.diagonals:
            if self.check_victory(diagonal):
                self.winner = self.turno.marca

    def check_victory(self, line):
        return len([i[1] for i in [(p, v) for (p, v) in self.tabuleiro.mapa.items() if p in line] if i[1]==self.turno.marca])==3


if __name__=="__main__":
    Game().start()
