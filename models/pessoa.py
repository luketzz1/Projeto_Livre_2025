class Pessoa:
    def __init__(self, nome: str, email: str):
        self.__nome = nome
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    def __str__(self):
        return f"{self.nome} ({self.email})"