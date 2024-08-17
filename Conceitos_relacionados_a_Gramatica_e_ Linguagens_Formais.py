class AFD:
    def __init__(self, estados, alfabeto, transicoes, inicial, finais):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.inicial = inicial
        self.finais = finais

    def reconhece(self, palavra):
        estado_atual = self.inicial
        for simbolo in palavra:
            if (estado_atual, simbolo) not in self.transicoes:
                return False
            estado_atual = self.transicoes[(estado_atual, simbolo)]
        return estado_atual in self.finais

# L1 = {w ∈ {0, 1}∗ : w termina em 01}
afd1 = AFD(
    estados={'q0', 'q1', 'q2'},
    alfabeto={'0', '1'},
    transicoes={
        ('q0', '0'): 'q0',
        ('q0', '1'): 'q1',
        ('q1', '0'): 'q2',
        ('q1', '1'): 'q1',
        ('q2', '0'): 'q0',
        ('q2', '1'): 'q1'
    },
    inicial='q0',
    finais={'q2'}
)

# ... (implementar os outros AFDs de forma similar)

# Exemplo de uso
print(afd1.reconhece("0101"))  # True
print(afd1.reconhece("111"))  # False
