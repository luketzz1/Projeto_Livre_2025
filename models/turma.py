from models.aluno import Aluno
from models.disciplina import Disciplina

class Turma:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__alunos = []
        self.__disciplinas = []

    @property
    def nome(self):
        return self.__nome

    def adicionar_aluno(self, aluno: Aluno):
        self.__alunos.append(aluno)

    def adicionar_disciplina(self, disciplina: Disciplina):
        self.__disciplinas.append(disciplina)

    def listar_alunos(self):
        return [str(a) for a in self.__alunos]

    def listar_disciplinas(self):
        return [str(d) for d in self.__disciplinas]

    def to_dict(self):
        return {
            "nome": self.__nome,
            "alunos": [a.to_dict() for a in self.__alunos],
            "disciplinas": [
                {"nome": d.nome, "professor": d.professor.nome} for d in self.__disciplinas
            ]
        }

    @classmethod
    def from_dict(cls, data):
        from models.aluno import Aluno
        turma = cls(data["nome"])
        turma.__alunos = [Aluno.from_dict(a) for a in data["alunos"]]
        return turma

    def __str__(self):
        return f"Turma {self.nome} - {len(self.__alunos)} alunos"