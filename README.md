# 📖 Agenda de Contatos em Python (CLI)

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Status](Concluído-success.svg)](https://github.com)

Sistema de gerenciamento de contatos desenvolvido em Python para operar via linha de comando (CLI). O projeto implementa todas as operações fundamentais de um **CRUD** (Create, Read, Update, Delete) utilizando estruturas de dados nativas da linguagem.

---

## Objetivo do Projeto

O objetivo principal deste projeto é consolidar os fundamentos de lógica de programação em Python, aplicando conceitos como:
* Manipulação de estruturas de dados (**Listas** e **Dicionários**).
* Criação de funções modulares e reutilizáveis.
* Controle de fluxo (`while`, `for`, condicionais).
* Tratamento de erros e exceções (`try/except`) para garantir a robustez da entrada de dados do usuário.

---

## Funcionalidades

O sistema oferece um menu interativo com as seguintes opções:

1. **Adicionar Contato (Create):** Cadastra um novo contato informando nome, telefone e e-mail, com validação para evitar campos de nome vazios.
2. **Listar Contatos (Read):** Exibe todos os contatos cadastrados de forma enumerada e organizada.
3. **Buscar Contato (Read):** Permite pesquisar contatos por nome (busca parcial ou completa, ignorando maiúsculas/minúsculas).
4. **Atualizar Contato (Update):** Modifica os dados de um contato existente. Caso o usuário queira manter algum dado atual, basta pressionar *Enter*.
5. **Excluir Contato (Delete):** Remove um contato selecionado da agenda com base no seu número na listagem.
6. **Sair:** Encerra a execução do programa de forma segura.

---

## Tecnologias Utilizadas

* **Python 3.x** (Linguagem de programação principal)
* **Visual Studio Code** (Editor de Código-Fonte)
* Estruturas nativas: `list`, `dict`, `str`
* Tratamento de exceções: `ValueError`

---

## ⚙️ Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o **Python** instalado em sua máquina. Você pode verificar executando o seguinte comando no seu terminal:
```bash
python --version
