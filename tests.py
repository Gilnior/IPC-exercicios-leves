import unittest
from tic_tac_toe import main

class TestGame(unittest.TestCase):

    def setUp(self) -> None:
        self.table = main.Table()
        return super().setUp()  

    def test_table_initial_state(self):
        self.assertListEqual(list(self.table.mapa.values()), [" " for i in range(9)])
        self.assertEqual(self.table.get_posicoes_jogadas(), 0)
        self.assertEqual(self.table.marcas, {"O", "X"})

        self.table.marcar("q", "X")

        self.assertEqual(self.table.get_posicoes_jogadas(), 1)
        self.assertNotEqual(list(self.table.mapa.values()), [" " for i in range(9)])
        self.assertEqual(self.table.mapa['q'], "X")

    def test_players(self):
        player_1 = main.Player(self.table)
        player_2 = main.Player(self.table)
        
        self.assertEquals(player_1.tabuleiro, player_2.tabuleiro, self.table)
        self.assertNotIn({'X', 'O'}, self.table.marcas)
        self.assertEqual({player_2.marca, player_1.marca}, {'X', 'O'})

        player_1.marcar("q")

        self.assertEqual(player_1.marca, self.table.mapa["q"])

        player_2.marcar("c")

        self.assertEqual(player_2.marca, self.table.mapa["c"])


if __name__=="__main__":
    unittest.main()