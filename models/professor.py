from models.pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome: str, email: str, especialidade: str):
        super().__init__(nome, email)
        self.__especialidade = especialidade

    @property
    def especialidade(self):
        return self.__especialidade

    def __str__(self):
        return f"Professor: {self.nome} - {self.especialidade}"
