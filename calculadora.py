def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

print("=== Calculadora ===")
print("Soma 2+3 =", soma(2, 3))
print("Subtração 10-4 =", subtracao(10, 4))
print("Multiplicação 3x5 =", multiplicacao(3, 5))
print("Divisão 10/2 =", divisao(10, 2))

def potencia(base, expoente):
    return base ** expoente

print("Potência 2^10 =", potencia(2, 10))

def resto_divisao(a, b):
    return a % b

print("Resto de 10/3 =", resto_divisao(10, 3))

def valor_absoluto(a):
    return abs(a)

print("Valor absoluto de -15 =", valor_absoluto(-15))

import math

def raiz_quadrada(a):
    if a < 0:
        return "Erro: número negativo!"
    return math.sqrt(a)

print("Raiz quadrada de 25 =", raiz_quadrada(25))

def media(a, b):
    return (a + b) / 2

print("Média de 6 e 8 =", media(6, 8))