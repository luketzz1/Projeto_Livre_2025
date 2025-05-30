import os
from models.professor import Professor
from models.aluno import Aluno
from models.disciplina import Disciplina
from models.turma import Turma
from utils.persistencia import salvar_turma_em_json, carregar_turma_de_json

TURMAS = {}

def criar_ou_pegar_turma(nome: str) -> Turma:
    if nome in TURMAS:
        return TURMAS[nome]
    if os.path.exists(f"{nome}.json"):
        turma = carregar_turma_de_json(f"{nome}.json")
        TURMAS[nome] = turma
        return turma
    turma = Turma(nome)
    TURMAS[nome] = turma
    return turma

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Cadastrar aluno")
        print("2. Cadastrar professor e disciplina")
        print("3. Adicionar nota para aluno")
        print("4. Listar alunos da turma")
        print("5. Salvar e sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_aluno = input("Nome do aluno: ")
            email_aluno = input("Email do aluno: ")
            turma_nome = input("Turma (ex: 2º B): ")
            turma = criar_ou_pegar_turma(turma_nome)

            aluno = Aluno(nome_aluno, email_aluno)
            aluno.enviar_email("Bem-vindo à turma!")
            turma.adicionar_aluno(aluno)

            print(f"Aluno {nome_aluno} adicionado à turma {turma_nome}.")

        elif opcao == "2":
            nome_prof = input("Nome do professor: ")
            email_prof = input("Email do professor: ")
            esp = input("Especialidade: ")
            nome_disc = input("Nome da disciplina: ")
            turma_nome = input("Turma: ")
            turma = criar_ou_pegar_turma(turma_nome)

            professor = Professor(nome_prof, email_prof, esp)
            disciplina = Disciplina(nome_disc, professor)
            turma.adicionar_disciplina(disciplina)

            print(f"Disciplina {nome_disc} adicionada à turma {turma_nome}.")

        elif opcao == "3":
            turma_nome = input("Turma: ")
            turma = criar_ou_pegar_turma(turma_nome)
            print("\nAlunos:")
            for i, aluno in enumerate(turma._Turma__alunos):
                print(f"{i + 1}. {aluno.nome}")

            aluno_index = int(input("Escolha o número do aluno: ")) - 1
            aluno = turma._Turma__alunos[aluno_index]

            print("\nDisciplinas:")
            for i, disc in enumerate(turma._Turma__disciplinas):
                print(f"{i + 1}. {disc.nome}")

            disc_index = int(input("Escolha o número da disciplina: ")) - 1
            disciplina = turma._Turma__disciplinas[disc_index]
            nota = float(input(f"Nota para {disciplina.nome}: "))

            aluno.adicionar_nota(disciplina.nome, nota)
            aluno.enviar_email(f"Sua nota em {disciplina.nome} foi registrada: {nota}")

        elif opcao == "4":
            turma_nome = input("Turma: ")
            turma = criar_ou_pegar_turma(turma_nome)
            print(f"\nTurma {turma.nome} - Alunos:")
            for aluno in turma._Turma__alunos:
                print(f"- {aluno.nome}")

        elif opcao == "5":
            for nome, turma in TURMAS.items():
                salvar_turma_em_json(turma, f"{nome}.json")
                print(f"Turma {nome} salva em {nome}.json.")
            print("Encerrando programa.")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
