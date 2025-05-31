# Projeto_Livre_2025

## Descrição

O **Projeto_Livre_2025** é um sistema de gerenciamento escolar desenvolvido em Python, com interface gráfica utilizando `customtkinter`. O objetivo é facilitar o cadastro de alunos, professores, disciplinas, lançamento de notas e visualização de informações das turmas, tanto via terminal quanto por interface gráfica.

## Casos de Uso

- **Cadastro de Alunos:** Permite adicionar alunos a uma turma, registrando nome e e-mail.
- **Cadastro de Professores e Disciplinas:** Permite cadastrar professores e associá-los a disciplinas em turmas.
- **Lançamento de Notas:** Permite lançar notas para alunos em disciplinas específicas.
- **Visualização de Notas:** Permite visualizar todas as notas e médias dos alunos por disciplina.
- **Listagem de Alunos:** Permite listar todos os alunos de uma turma.
- **Persistência:** Salva e carrega os dados das turmas em arquivos `.json`.

## Estrutura de Pastas

```
Projeto_Livre_2025/
│
├── gui.py                  # Interface gráfica (CustomTkinter)
├── main.py                 # Interface de linha de comando (CLI)
├── README.md               # Este arquivo
├── turma3A.json            # Exemplo de arquivo de turma (pode estar vazio)
│
├── Gerenciador/
│   └── .gitattributes      # Configuração de git
│
├── models/                 # Modelos de domínio
│   ├── __init__.py
│   ├── aluno.py            # Classe Aluno
│   ├── disciplina.py       # Classe Disciplina
│   ├── pessoa.py           # Classe base Pessoa
│   ├── professor.py        # Classe Professor
│   └── turma.py            # Classe Turma
│
├── turmas_salvas/          # Turmas salvas em JSON
│   ├── 3 A.json
│   ├── 3 B.json
│   └── 3 C.json
│
└── utils/
    ├── __init__.py
    └── persistencia.py     # Funções de salvar/carregar turmas
```

## Funcionalidades

- **Interface Gráfica:** Cadastro, consulta e lançamento de notas de forma intuitiva.
- **Interface CLI:** Menu interativo para operações básicas.
- **Persistência automática:** Dados das turmas são salvos em arquivos JSON.
- **Notificações simuladas:** Envio de mensagens simuladas para e-mail dos alunos ao cadastrar ou lançar notas.

## Como Executar

### Pré-requisitos

- Python 3.10 ou superior
- Instalar dependências:
    - `customtkinter` (para interface gráfica)

```sh
pip install customtkinter
```

### Executando a Interface Gráfica

No terminal, execute:

```sh
python gui.py
```

### Executando a Interface de Linha de Comando

No terminal, execute:

```sh
python main.py
```

Os dados das turmas serão salvos automaticamente na pasta [`turmas_salvas`](turmas_salvas/).

---

**Observação:**  
Os arquivos de modelos estão na pasta [`models`](models/), e as funções de persistência em [`utils/persistencia.py`](utils/persistencia.py).