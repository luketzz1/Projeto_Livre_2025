class Disciplina:
    def __init__(self, nome: str, professor):
        self.__nome = nome
        self.__professor = professor

    @property
    def nome(self):
        return self.__nome

    @property
    def professor(self):
        return self.__professor

    def __str__(self):
        return f"{self.nome} - {self.professor.nome}"