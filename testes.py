class Pessoa:
    def __init__(self, nome, score):
        self.nome = nome
        self.score = score

pessoas = [
    Pessoa("Maria", 20),
    Pessoa("João", 10),
    Pessoa("José", 30),
]

# Ordenar pessoas por score
pessoas.sort(key=lambda p: p.score)

print([pessoa.nome for pessoa in pessoas])

