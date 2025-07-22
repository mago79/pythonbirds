class Pessoa:
    def __init__(self, nome = None, idade = 46):
        self.idade = idade
        self.nome = None

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__' :
    p = Pessoa('Elizel')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Elizel'
    print(p.nome)
    print(p.idade)
