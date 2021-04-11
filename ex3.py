class Aluno:

    def __init__(self, n1, n2, n3, n4):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4

    def n1Get(self):
        return self.n1

    def n2Get(self):
        return self.n2

    def n3Get(self):
        return self.n3

    def n4Get(self):
        return self.n4

    def calculaMediaDoAluno(aluno):
        media = (aluno.n1Get() + aluno.n2Get() + aluno.n3Get() + aluno.n4Get()) / 4
        return round(media, 2)


a1 = Aluno(0.0, 0.0, 1.0, 9.1)
a2 = Aluno(6.0, 7.0, 8.0, 9.2)
a3 = Aluno(6.0, 7.0, 8.0, 9.3)
a4 = Aluno(6.0, 7.0, 8.0, 9.4)
a5 = Aluno(6.0, 7.0, 8.0, 9.5)
a6 = Aluno(6.0, 7.0, 8.0, 9.6)
a7 = Aluno(6.0, 7.0, 8.0, 9.7)
a8 = Aluno(6.0, 7.0, 8.0, 9.8)
a9 = Aluno(6.0, 7.0, 8.0, 9.9)
a10 = Aluno(1.0, 2.0, 3.0, 5.2)

alunos = []


def calculaMediaGeral():
    alunos.append(Aluno.calculaMediaDoAluno(a1))
    alunos.append(Aluno.calculaMediaDoAluno(a2))
    alunos.append(Aluno.calculaMediaDoAluno(a3))
    alunos.append(Aluno.calculaMediaDoAluno(a4))
    alunos.append(Aluno.calculaMediaDoAluno(a5))
    alunos.append(Aluno.calculaMediaDoAluno(a6))
    alunos.append(Aluno.calculaMediaDoAluno(a7))
    alunos.append(Aluno.calculaMediaDoAluno(a8))
    alunos.append(Aluno.calculaMediaDoAluno(a9))
    alunos.append(Aluno.calculaMediaDoAluno(a10))

    print("ESTES SÃO OS DISCENTES COM MÉDIA MAIOR QUE 7.0:")
    for i in range(alunos.__len__()):
        if alunos[i] >= 7.0:
            print("MEDIA DO ALUNO INDICE ", i, "é:", alunos[i])


calculaMediaGeral()
