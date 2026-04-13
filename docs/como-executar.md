# Como Executar

## Pré-requisitos

- Python 3.10 ou superior instalado
- Git instalado

## Passo a Passo

### 1. Clone o repositório

```bash
git clone https://github.com/Davi-D18/busca_mentorados.git
cd busca_mentorados
```

### 2. Crie o ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

> O ambiente virtual está ativo quando aparecer `(venv)` no início do terminal.

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```
ENVIRONMENT=development
```

> Este arquivo não é versionado por segurança. Precisa ser criado manualmente.

### 5. Execute o programa

```bash
python main.py
```

Saída esperada:
```
=============================================
SISTEMA DE MENTORIA
=============================================
1. Buscar mentoreado
2. Ver relatório geral
3. Sair
Escolha uma opção:
```

---

## Possíveis Erros

| Erro | Causa | Solução |
|---|---|---|
| `ModuleNotFoundError: No module named 'decouple'` | Dependência não instalada | Rodar `pip install -r requirements.txt` |
| `KeyError: 'ENVIRONMENT'` | Arquivo `.env` não criado | Criar o arquivo `.env` conforme o passo 4 |
| `python não encontrado` | Python não está no PATH | Reinstalar o Python marcando "Add to PATH" |

---

## Estrutura de Arquivos Gerados

Após executar `main.py`, será criado o arquivo `labs.db` na raiz do projeto com as tabelas e dados de teste já populados.
