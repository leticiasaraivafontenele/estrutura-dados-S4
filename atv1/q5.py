import random

def aniversariosIguais(pessoas):
    aniversarios = [random.randint(1, 365) for _ in range((pessoas))]
    return len(aniversarios) != len(set(aniversarios))

def estimarProbabilidade(n, tests):
    equals = sum(aniversariosIguais(n) for _ in range(tests))
    return equals/tests

def paradoxTest(fromm=5, to=100, jump=5, tests=10000):
    for n in range(fromm, to + 1, jump):
        probabilidade = estimarProbabilidade(n, tests)
        print(f'Para n = {n}, a probabilidade de anivarsários repetidos é aproximadamente {probabilidade:.4f}')