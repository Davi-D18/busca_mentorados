#  Funcionalidades

## Menu Interativo

O sistema é operado por um menu de linha de comando com opções numeradas. O usuário digita o número da opção desejada e interage com o sistema em tempo real.

```
=============================================
SISTEMA DE MENTORIA
=============================================
1. Buscar mentorado e encontros inscritos
2. Verificar vaga em um encontro
3. Inscrever alguém novo
4. Confirmar presença em um encontro
5. Inscrever-se em um encontro
6. Sair
Escolha uma opção:
```

---

## 1. Busca de Mentoreado (Módulo D)

**O que faz:** Recebe o nome ou parte do nome de um mentoreado e retorna todas as informações de participação.

**Como usar:**
```
Escolha uma opção: 1
Digite o nome (ou parte): Maria
```

**Saída esperada:**
```
 Nome: Maria Martins
 Email: maria@email.com
 Encontros inscritos: 2
 Confirmou presença: Sim
 Total de participações: 2
```

**Lógica aplicada:**
- Função com parâmetro de busca
- SQL com `LIKE` para busca parcial
- `LEFT JOIN` entre `mentoreados` e `encontros`
- Condicional para exibir "Sim" ou "Não" na presença

---

## 2. Controle de Vagas

**O que faz:** Verifica se ainda há vagas disponíveis em um encontro antes de permitir a inscrição. O limite é de **3 vagas por encontro**.

**Lógica aplicada:**
```python
if vagas_restantes > 0:
    # permite inscrição
else:
    # bloqueia e avisa que está lotado
```

---

## 3. Confirmação de Presença

**O que faz:** Atualiza o status `confirmou_presenca` de 0 para 1 no banco de dados para um mentoreado em uma data específica.

**SQL utilizado:**
```sql
UPDATE encontros 
SET confirmou_presenca = 1
WHERE mentoreado_id = ? AND data = ?
```

---

## 4. Relatório Geral

**O que faz:** Exibe um resumo consolidado de todas as mentorias.

**Saída esperada:**
```
========================================
RELATÓRIO GERAL
========================================
 Total de mentoreados: 5
 Total de inscrições: 5
 Presenças confirmadas: 4
 Taxa de presença: 80.0%

 Top participantes:
  • Gertrudes Silva: 2 presenças
  • José Costa: 1 presença
  • Genoveva Souza: 1 presença
```

---

## Arquitetura do Código

O projeto segue uma separação de responsabilidades clara:

| Módulo | Responsabilidade |
|---|---|
| `configs/database.py` | Conexão com o banco |
| `settings/` | Configurações por ambiente |
| `scripts/init_db.py` | Criação das tabelas e seed |
| `scripts/buscar_mentoreado.py` | Lógica de busca (Módulo D) |
| `scripts/relatorio.py` | Geração de relatórios |
| `menu.py` | Interface do usuário |
| `run.py` | Ponto de entrada para inicialização |
