from AlunoGraduacao import AlunoGraduacao
from AlunoEnsinoMedio import AlunoEnsinoMedio

if __name__ == '__main__':
    alunoGraduacao = AlunoGraduacao(1, "Raul Jung Severo", "181610166", 3)
    alunoEnsinoMedio = AlunoEnsinoMedio(2, "Juan Juan Severo", "202108967", 2021)

    alunoGraduacao.imprimir()
    alunoEnsinoMedio.imprimir()
