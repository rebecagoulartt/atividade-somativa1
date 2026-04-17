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