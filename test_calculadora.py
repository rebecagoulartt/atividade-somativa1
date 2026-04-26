import unittest
from calculadora import soma, subtracao, multiplicacao, divisao, potencia, media

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)

    def test_subtracao(self):
        self.assertEqual(subtracao(10, 4), 6)

    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(3, 5), 15)

    def test_divisao(self):
        self.assertEqual(divisao(10, 2), 5.0)

    def test_divisao_por_zero(self):
        self.assertEqual(divisao(10, 0), "Erro: divisão por zero!")

    def test_media(self):
        self.assertEqual(media(6, 8), 7.0)

if __name__ == '__main__':
    unittest.main()
# testes unitários da calculadora
