# crid-verifier-ufrj

# Sistema de Verificação de Autenticidade para o CRID da UFRJ em Blockchain

[![CI Status](https://github.com/DaviSilvaC/crid-verifier-ufrj/actions/workflows/main.yml/badge.svg)](https://github.com/DaviSilvaC/crid-verifier-ufrj/actions)
![Solidity](https://img.shields.io/badge/Solidity-^0.8.19-lightgrey)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Este projeto é um protótipo de um sistema descentralizado para a verificação de autenticidade do Documento de Confirmação de Inscrição em Disciplinas (CRID) da UFRJ, utilizando um Smart Contract na blockchain Ethereum.

---

## 📋 Tabela de Conteúdos

1.  [Sobre o Projeto](#-sobre-o-projeto)
2.  [Arquitetura e Tecnologias](#-arquitetura-e-tecnologias)
3.  [Funcionalidades](#-funcionalidades)
4.  [Começando](#-começando)
5.  [Uso](#-uso)
6.  [Estrutura do Projeto](#-estrutura-do-projeto)
7.  [Pipeline de CI/CD](#-pipeline-de-cicd)
8.  [Autor](#-autor)

---

## 🚀 Sobre o Projeto

O Documento de Confirmação de Inscrição em Disciplinas (CRID) é um registro acadêmico essencial na UFRJ. No entanto, seu formato digital o torna vulnerável a adulterações. Este projeto resolve essa questão ao criar um "cartório digital" na blockchain.

A solução permite que a administração da universidade registre uma "assinatura" digital (hash) de cada CRID emitido. Uma vez registrado, esse dado se torna imutável. Qualquer pessoa ou empresa pode, então, verificar de forma rápida e segura se um documento CRID é autêntico, comparando seu hash com o registro na blockchain, prevenindo fraudes de forma eficaz.

---

## 🛠️ Arquitetura e Tecnologias

Este projeto foi construído utilizando as seguintes tecnologias:

* **Solidity:** Linguagem de programação para escrever o Smart Contract.
* **Python 3.11:** Linguagem principal para os scripts de teste e deploy.
* **Brownie:** Framework de desenvolvimento e testes para projetos de smart contracts em Python.
* **Hardhat:** Utilizado como ambiente de blockchain local para execução dos testes.
* **Pytest:** Framework para a escrita e execução da suíte de testes.
* **GitHub Actions:** Plataforma de automação para o pipeline de Integração Contínua (CI).

---

## ✨ Funcionalidades

* **Registro Seguro:** Apenas o endereço "dono" do contrato (representando a UFRJ) pode registrar novos hashes de CRID.
* **Verificação Pública:** Qualquer pessoa pode chamar a função de verificação para validar a autenticidade de um documento sem custo de gás.
* **Imutabilidade:** Uma vez que um hash é registrado, ele não pode ser alterado ou removido, garantindo a integridade do registro.

---

## 🏁 Começando

Para executar este projeto localmente, siga os passos abaixo.

### Pré-requisitos

Você precisa ter o seguinte software instalado:
* [Python 3.11+](https://www.python.org/downloads/)
* [Node.js (LTS)](https://nodejs.org/en/) (para o ambiente de teste Hardhat)

### Instalação

1.  Clone o repositório:
    ```sh
    git clone [https://github.com/](https://github.com/)DaviSilvaC/crid-verifier-ufrj.git
    ```
2.  Navegue até a pasta do projeto:
    ```sh
    cd [NOME_DO_REPOSITORIO]
    ```
3.  Crie e ative um ambiente virtual:
    ```sh
    # No Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```
4.  Instale as dependências Python:
    ```sh
    pip install eth-brownie
    ```
5.  Instale as dependências Node.js:
    ```sh
    npm install
    ```

---

## ▶️ Uso

Após a instalação, você pode usar os seguintes comandos do Brownie:

* **Compilar os contratos:**
    ```sh
    brownie compile
    ```

* **Executar a suíte de testes:**
    ```sh
    brownie test
    ```

* **Fazer o deploy em uma rede local (ex: Hardhat):**
    Primeiro, inicie um nó Hardhat em um terminal separado:
    ```sh
    npx hardhat node
    ```
    Depois, em outro terminal, execute o script de deploy:
    ```sh
    brownie run scripts/deploy.py --network hardhat
    ```

---

## 🔄 Pipeline de CI/CD

Este projeto utiliza um pipeline de Integração Contínua (CI) configurado em `.github/workflows/main.yml`. A cada `push` para o repositório, o GitHub Actions automaticamente:
1.  Configura um ambiente com Python e Node.js.
2.  Instala todas as dependências do projeto.
3.  Executa a suíte de testes completa para garantir que nenhuma alteração quebrou o código.

O status da última execução do pipeline é mostrado no badge no topo deste README.

---

## 👨‍💻 Autor

* Davi da Costa Silva - [davicostasilva@poli.ufrj.br]

---
