# Visão Geral do Projeto

## O Contexto

A Labs abriu inscrições para uma nova rodada de mentorias. O desafio era organizar:

- Encontros com datas e vagas limitadas
- Inscrições dos mentoreados
- Acompanhamento de presença
- Relatórios básicos de participação

## A Solução

Desenvolvemos um sistema de linha de comando em **Python + SQLite** com menu interativo, permitindo que qualquer pessoa da equipe consulte, inscreva e acompanhe mentoreados em tempo real.

## Desafio do Grupo

**Módulo D — Busca de Mentoreado**

> Um buscador que recebe o nome (ou parte do nome) de um mentoreado e mostra: em quais encontros está inscrito, se confirmou presença e quantos encontros já participou no total.

## Requisitos Atendidos

### 1. Lógica de Programação
- Variáveis e tipos de dados
- Condicionais (`if/else`) para verificação de vagas e presença
- Funções com parâmetros para busca e relatórios
- Repetição (`while`) no menu interativo

### 2. Banco de Dados com SQL
- 2 tabelas: `mentoreados` e `encontros`
- Seed com 5 registros por tabela
- 2 consultas úteis com filtros e junções (JOIN)

### 3. Saídas Claras
- Resultados exibidos no terminal de forma organizada
- Mensagens de feedback para cada ação do usuário

## Tecnologias Utilizadas

| Tecnologia | Versão | Uso |
|---|---|---|
| Python | 3.10+ | Linguagem principal |
| SQLite | 3 | Banco de dados |
| python-decouple | 3.8 | Variáveis de ambiente |

## Ferramenta de Desenvolvimento

**VS Code + Terminal** — escolhido pela praticidade, controle total do ambiente e facilidade de demonstração ao vivo durante a apresentação.
