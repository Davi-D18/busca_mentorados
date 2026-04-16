# Busca de Mentoreados — Sistema de Gestão de Mentorias

> Desafio 5 | Grupo 4 — Lógica de Programação + Banco de Dados

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey?logo=sqlite)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

---

## Sobre o Projeto

A Labs abriu inscrições para uma nova rodada de mentorias e precisava de uma solução simples para organizar tudo: encontros certinhos, vagas controladas e presença acompanhada sem mistério.

Nossa missão foi criar um sistema que ajuda a Labs a gerenciar inscrições, vagas e presenças, com regras claras e relatórios básicos.

---

## Equipe

| Integrante | Responsabilidade |
|---|---|
| Davi | Banco de dados, configurações, menu interativo |
| Samuel | Controle de vagas, inscrições e slide|
| Tulani | Buscador de mentoreado, documentação (README e docs) e PDF|

---

## Estrutura do Projeto

```
busca_mentorados/
├── configs/
│   ├── __init__.py
│   └── database.py         # Conexão com o banco de dados
├── scripts/
│   ├── __init__.py
│   ├── init_db.py          # Inicialização do banco e seed
├── settings/
│   ├── __init__.py
│   ├── base.py             # Configurações base
│   └── development.py      # Configurações de desenvolvimento
├── docs/                   # Documentação detalhada
├── .env                    # Variáveis de ambiente (não versionado)
├── .gitignore
├── main.py                  # Script de inicialização
└── requirements.txt
```

---

## Como Executar

Veja o guia completo em [docs/como-executar.md](docs/como-executar.md).

```bash
# 1. Clone o repositório
git clone https://github.com/Davi-D18/busca_mentorados.git
cd busca_mentorados

# 2. Crie e ative o ambiente virtual
python -m venv venv
source venv/Scripts/activate  # Windows
source venv/bin/activate       # Mac/Linux

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure o ambiente
echo "ENVIRONMENT=development" > .env

# 5. Inicialize o banco de dados
python main.py

```

---

## Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| Busca de mentoreado | Busca por nome ou parte do nome, mostrando encontros e presenças |
| Controle de vagas | Verifica disponibilidade e bloqueia inscrição quando lotado |
| Confirmação de presença | Atualiza o status de presença no banco |
| Relatório geral | Exibe totais, taxa de presença e top participantes |

---

## Banco de Dados

Duas tabelas principais:

- **`mentoreados`** — cadastro dos participantes
- **`encontros`** — inscrições, datas e confirmações de presença

Veja o schema completo em [docs/banco-de-dados.md](docs/banco-de-dados.md).

---

## Documentação

- [Visão Geral do Projeto](docs/visao-geral.md)
- [Banco de Dados](docs/banco-de-dados.md)
- [Como Executar](docs/como-executar.md)
- [Funcionalidades](docs/funcionalidades.md)
