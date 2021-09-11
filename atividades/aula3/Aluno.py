class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.__codigo = codigo
        self.__nome = nome
        self.__matricula = matricula

    def imprimir(self):
        print("\nCódigo: " + str(self.__codigo) + \
              "\nNome: " + self.__nome + \
              "\nMatrícula: " + self.__matricula)
