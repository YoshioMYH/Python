from util import utilidades
from model.Humano import Humano

# Definicao de uma Classe
class PrimeiraClasse:
    'Minha primeira classe em Python'

    def __init__(self, nome, algo):
        self.nome = nome
        self.algo = algo

    def toString(self):
        return "Nome: %s\nLista de Idiomas: %s" % (self.nome, utilidades.list2string(self.algo))
# Fim - Definição de uma classe


firstClass = PrimeiraClasse("Marcelo", ['Inglês', 'Portugues', 'Japonês'])
print(firstClass.toString())

print()

marcelo = Humano("Marcelo", 1995, 1.72, 65.0)
print(marcelo.nome)
print(marcelo.imc())
print(marcelo.idade())