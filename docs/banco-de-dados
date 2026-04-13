# Banco de Dados

## Visão Geral

O sistema utiliza **SQLite** como banco de dados, armazenado localmente no arquivo `labs.db`. A escolha do SQLite se justifica pela simplicidade de configuração e por não exigir um servidor separado.

## Schema

### Tabela: `mentoreados`

Armazena o cadastro de todos os participantes das mentorias.

| Coluna | Tipo | Descrição |
|---|---|---|
| `id` | INTEGER PRIMARY KEY | Identificador único |
| `nome` | TEXT | Nome completo do mentoreado |
| `email` | TEXT | E-mail de contato |

```sql
CREATE TABLE IF NOT EXISTS mentoreados (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    email TEXT
);
```

---

### Tabela: `encontros`

Registra as inscrições dos mentoreados nos encontros, com data e status de presença.

| Coluna | Tipo | Descrição |
|---|---|---|
| `id` | INTEGER PRIMARY KEY | Identificador único |
| `mentoreado_id` | INTEGER | Referência ao mentoreado (FK) |
| `data` | TEXT | Data do encontro (formato YYYY-MM-DD) |
| `confirmou_presenca` | INTEGER | 1 = confirmou, 0 = não confirmou |

```sql
CREATE TABLE IF NOT EXISTS encontros (
    id INTEGER PRIMARY KEY,
    mentoreado_id INTEGER,
    data TEXT,
    confirmou_presenca INTEGER,
    FOREIGN KEY (mentoreado_id) REFERENCES mentoreados(id)
);
```

---

## Relacionamento entre Tabelas

```
mentoreados          encontros
-----------          ---------
id (PK)   ◄──────── mentoreado_id (FK)
nome               id (PK)
email              data
                   confirmou_presenca
```

Um mentoreado pode ter **vários encontros** (relação 1 para N).

---

## Dados de Teste (Seed)

### Mentoreados

| id | nome | email |
|---|---|---|
| 1 | Gertrudes Silva | gertrudes@email.com |
| 2 | José Costa | jose@email.com |
| 3 | Genoveva Souza | genoveva@email.com |
| 4 | Matias Lima | matias@email.com |
| 5 | Maria Martins | maria@email.com |

### Encontros

| id | mentoreado_id | data | confirmou_presenca |
|---|---|---|---|
| 1 | 1 | 2026-04-01 | ✅ Sim |
| 2 | 1 | 2026-04-08 | ✅ Sim |
| 3 | 2 | 2026-04-01 | ❌ Não |
| 4 | 3 | 2026-04-08 | ✅ Sim |
| 5 | 2 | 2026-04-08 | ✅ Sim |

---

## Consultas SQL Utilizadas

### 1. Busca de Mentoreado (Módulo D)

Busca por nome parcial usando `LIKE` e combina as duas tabelas com `LEFT JOIN`:

```sql
SELECT 
    m.nome,
    m.email,
    COUNT(e.id) AS total_encontros,
    SUM(e.confirmou_presenca) AS presencas_confirmadas
FROM mentoreados m
LEFT JOIN encontros e ON m.id = e.mentoreado_id
WHERE m.nome LIKE ?
GROUP BY m.id;
```

### 2. Relatório Geral

Agrega dados de presença de todos os encontros:

```sql
SELECT COUNT(*), SUM(confirmou_presenca)
FROM encontros;
```
