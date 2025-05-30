import customtkinter as ctk
from models.aluno import Aluno
from models.professor import Professor
from models.disciplina import Disciplina
from models.turma import Turma
from utils.persistencia import salvar_turma_em_json, carregar_turma_de_json
import os
import json

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

TURMAS = {}

TURMA_DIR = "turmas_salvas"
if not os.path.exists(TURMA_DIR):
    os.makedirs(TURMA_DIR)

def criar_ou_pegar_turma(nome):
    if nome in TURMAS:
        return TURMAS[nome]
    caminho = os.path.join(TURMA_DIR, f"{nome}.json")
    if os.path.exists(caminho):
        turma = carregar_turma_de_json(caminho)
        TURMAS[nome] = turma
        return turma
    turma = Turma(nome)
    TURMAS[nome] = turma
    return turma

def salvar_todas_turmas():
    for nome, turma in TURMAS.items():
        caminho = os.path.join(TURMA_DIR, f"{nome}.json")
        salvar_turma_em_json(turma, caminho)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gerenciamento Escolar")
        self.geometry("600x500")

        self.tabs = ctk.CTkTabview(self)
        self.tabs.pack(padx=20, pady=20, fill="both", expand=True)

        self.tab_aluno = self.tabs.add("Cadastrar Aluno")
        self.tab_professor = self.tabs.add("Cadastrar Professor")
        self.tab_nota = self.tabs.add("Adicionar Nota")
        self.tab_visualizar = self.tabs.add("Visualizar Notas")
        self.tab_listar_alunos = self.tabs.add("Listar Alunos")

        self.build_cadastro_aluno()
        self.build_cadastro_professor()
        self.build_adicionar_nota()
        self.build_visualizar_notas()
        self.build_listar_alunos()

        self.protocol("WM_DELETE_WINDOW", self.sair_com_salvamento)

    def build_cadastro_aluno(self):
        self.nome_aluno = ctk.CTkEntry(self.tab_aluno, placeholder_text="Nome do aluno")
        self.nome_aluno.pack(pady=10)
        self.email_aluno = ctk.CTkEntry(self.tab_aluno, placeholder_text="Email do aluno")
        self.email_aluno.pack(pady=10)
        self.turma_aluno = ctk.CTkEntry(self.tab_aluno, placeholder_text="Turma")
        self.turma_aluno.pack(pady=10)
        btn = ctk.CTkButton(self.tab_aluno, text="Cadastrar", command=self.cadastrar_aluno)
        btn.pack(pady=10)

    def build_cadastro_professor(self):
        self.nome_prof = ctk.CTkEntry(self.tab_professor, placeholder_text="Nome do professor")
        self.nome_prof.pack(pady=10)
        self.email_prof = ctk.CTkEntry(self.tab_professor, placeholder_text="Email do professor")
        self.email_prof.pack(pady=10)
        self.especialidade = ctk.CTkEntry(self.tab_professor, placeholder_text="Especialidade")
        self.especialidade.pack(pady=10)
        self.nome_disc = ctk.CTkEntry(self.tab_professor, placeholder_text="Disciplina")
        self.nome_disc.pack(pady=10)
        btn = ctk.CTkButton(self.tab_professor, text="Cadastrar em Todas as Turmas", command=self.cadastrar_disciplina_todas_turmas)
        btn.pack(pady=10)

    def build_adicionar_nota(self):
        self.turma_nota = ctk.CTkEntry(self.tab_nota, placeholder_text="Turma")
        self.turma_nota.pack(pady=10)
        self.aluno_opcao = ctk.CTkOptionMenu(self.tab_nota, values=[""], command=self.selecionar_aluno)
        self.aluno_opcao.pack(pady=10)
        self.disciplina_opcao = ctk.CTkOptionMenu(self.tab_nota, values=[""], command=self.selecionar_disciplina)
        self.disciplina_opcao.pack(pady=10)
        self.nota_input = ctk.CTkEntry(self.tab_nota, placeholder_text="Nota")
        self.nota_input.pack(pady=10)
        btn_atualizar = ctk.CTkButton(self.tab_nota, text="Carregar Dados da Turma", command=self.atualizar_dados_turma)
        btn_atualizar.pack(pady=5)
        btn = ctk.CTkButton(self.tab_nota, text="Adicionar Nota", command=self.adicionar_nota)
        btn.pack(pady=10)
        self.aluno_selecionado = ""
        self.disciplina_selecionada = ""

    def build_visualizar_notas(self):
        self.turma_visualizar = ctk.CTkEntry(self.tab_visualizar, placeholder_text="Turma")
        self.turma_visualizar.pack(pady=10)
        self.output = ctk.CTkTextbox(self.tab_visualizar, width=500, height=300)
        self.output.pack(pady=10)
        btn = ctk.CTkButton(self.tab_visualizar, text="Mostrar Notas", command=self.mostrar_notas)
        btn.pack(pady=10)

    def build_listar_alunos(self):
        self.turma_listar = ctk.CTkEntry(self.tab_listar_alunos, placeholder_text="Turma")
        self.turma_listar.pack(pady=10)
        self.output_listar = ctk.CTkTextbox(self.tab_listar_alunos, width=500, height=300)
        self.output_listar.pack(pady=10)
        btn = ctk.CTkButton(self.tab_listar_alunos, text="Listar Alunos", command=self.listar_alunos)
        btn.pack(pady=10)

    def cadastrar_aluno(self):
        nome = self.nome_aluno.get()
        email = self.email_aluno.get()
        turma_nome = self.turma_aluno.get()
        turma = criar_ou_pegar_turma(turma_nome)
        aluno = Aluno(nome, email)
        turma.adicionar_aluno(aluno)
        aluno.enviar_email("Bem-vindo à turma!")
        label = ctk.CTkLabel(self.tab_aluno, text="Aluno cadastrado com sucesso!", text_color="green")
        label.pack(pady=5)
        self.after(3000, label.destroy)

    def cadastrar_disciplina_todas_turmas(self):
        nome = self.nome_prof.get()
        email = self.email_prof.get()
        esp = self.especialidade.get()
        disc = self.nome_disc.get()
        professor = Professor(nome, email, esp)
        disciplina = Disciplina(disc, professor)
        salvar_todas_turmas()  # Salva estado antes de alteração
        for turma in TURMAS.values():
            turma.adicionar_disciplina(disciplina)
        label = ctk.CTkLabel(self.tab_professor, text="Professor e disciplina cadastrados com sucesso!", text_color="green")
        label.pack(pady=5)
        self.after(3000, label.destroy)

    def atualizar_dados_turma(self):
        turma_nome = self.turma_nota.get()
        turma = criar_ou_pegar_turma(turma_nome)
        nomes = [aluno.nome for aluno in turma._Turma__alunos]
        disciplinas = [disc.nome for disc in turma._Turma__disciplinas]
        self.aluno_opcao.configure(values=nomes)
        self.disciplina_opcao.configure(values=disciplinas)
        if nomes:
            self.aluno_opcao.set(nomes[0])
            self.aluno_selecionado = nomes[0]
        if disciplinas:
            self.disciplina_opcao.set(disciplinas[0])
            self.disciplina_selecionada = disciplinas[0]

    def selecionar_aluno(self, value):
        self.aluno_selecionado = value

    def selecionar_disciplina(self, value):
        self.disciplina_selecionada = value

    def adicionar_nota(self):
        turma_nome = self.turma_nota.get()
        aluno_nome = self.aluno_selecionado
        disciplina_nome = self.disciplina_selecionada
        nota = float(self.nota_input.get())
        turma = criar_ou_pegar_turma(turma_nome)
        for aluno in turma._Turma__alunos:
            if aluno.nome == aluno_nome:
                aluno.adicionar_nota(disciplina_nome, nota)
                aluno.enviar_email(f"Nota registrada em {disciplina_nome}: {nota}")
                label = ctk.CTkLabel(self.tab_nota, text="Nota adicionada com sucesso!", text_color="green")
        label.pack(pady=5)
        self.after(3000, label.destroy)

    def mostrar_notas(self):
        turma_nome = self.turma_visualizar.get()
        turma = criar_ou_pegar_turma(turma_nome)
        self.output.delete("0.0", "end")
        for aluno in turma._Turma__alunos:
            self.output.insert("end", f"{aluno.nome}:\n")
            for disc, notas in aluno._Aluno__notas.items():
                media = aluno.calcular_media(disc)
                self.output.insert("end", f"  {disc}: Notas {notas}, Média: {media:.2f}\n")

    def listar_alunos(self):
        turma_nome = self.turma_listar.get()
        turma = criar_ou_pegar_turma(turma_nome)
        self.output_listar.delete("0.0", "end")
        self.output_listar.insert("end", f"Alunos da turma {turma_nome}:\n")
        for aluno in turma._Turma__alunos:
            self.output_listar.insert("end", f"- {aluno.nome} ({aluno.email})\n")

    def sair_com_salvamento(self):
        salvar_todas_turmas()
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
