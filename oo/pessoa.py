class Pessoa:
    def __init__(self, *filhos, nome=None, idade=37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    rudy = Pessoa(nome='Rudy')
    rudiney = Pessoa(rudy, nome='Rudiney')
    print(Pessoa.cumprimentar(rudiney))
    print(id(rudiney))
    print(rudiney.cumprimentar())
    print(rudiney.nome)
    print(rudiney.idade)
    for filho in rudiney.filhos:
        print(filho.nome)
    rudiney.sobrenome = 'Assis'
    del rudiney.filhos
    print(rudiney.__dict__)
    print(rudy.__dict__)
