from models.pessoa import Pessoa

class EmailNotificacaoMixin:
    def enviar_email(self, mensagem: str):
        print(f"[Email enviado para {self.email}]: {mensagem}")

class Aluno(Pessoa, EmailNotificacaoMixin):
    def __init__(self, nome: str, email: str):
        super().__init__(nome, email)
        self.__notas = {}

    def adicionar_nota(self, disciplina: str, nota: float):
        if disciplina not in self.__notas:
            self.__notas[disciplina] = []
        self.__notas[disciplina].append(nota)

    def calcular_media(self, disciplina: str) -> float:
        notas = self.__notas.get(disciplina, [])
        return sum(notas) / len(notas) if notas else 0.0

    def to_dict(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "notas": self.__notas
        }

    @classmethod
    def from_dict(cls, data):
        aluno = cls(data["nome"], data["email"])
        aluno.__notas = data["notas"]
        return aluno

    def __str__(self):
        return f"Aluno: {self.nome}"