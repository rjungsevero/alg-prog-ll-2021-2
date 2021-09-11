from Aluno import Aluno


class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        Aluno.__init__(self, codigo, nome, matricula)
        self.__semestre = semestre

    def imprimir(self):
        super().imprimir()
        print("Semestre: " + str(self.__semestre))
