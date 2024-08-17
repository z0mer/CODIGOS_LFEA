def funcao_transicao(estado, simbolo):
    d = {
        "q1": {"0": "q1", "1": "q2"},
        "q2": {"0": "q3", "1": "q2"},
        "q3": {"0": "q2", "1": "q2"}
    }
    return d[estado][simbolo]

estados = ["q1", "q2", "q3"]
alfabeto = ["0", "1"]
inicial = "q1"
aceitacao = ["q2"]

entrada = input()
palavras = entrada.split()

for palavra in palavras:
    atual = inicial
    for simbolo in palavra:
        if simbolo not in alfabeto:
            atual = None
            print("Caractér inválido")
            break
        atual = funcao_transicao(atual, simbolo)

    if atual in aceitacao:
        print("aceita")
    else:
        print("rejeita")
