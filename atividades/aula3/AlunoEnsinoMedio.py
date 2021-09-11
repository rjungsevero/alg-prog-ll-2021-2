from Aluno import Aluno


class AlunoEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.__ano = ano

    def imprimir(self):
        super().imprimir()
        print("Ano: " + str(self.__ano))

