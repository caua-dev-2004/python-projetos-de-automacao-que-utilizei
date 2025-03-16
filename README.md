# README - Sistema de Gerenciamento de Pastas e Arquivos Acadêmicos

## Introdução

Este projeto consiste em um conjunto de scripts Python desenvolvidos para otimizar o gerenciamento de pastas e arquivos de alunos em uma escola de cursos livres. O sistema foi projetado para facilitar o acesso às pastas dos alunos, garantir a organização dos arquivos e atualizar links de forma automática.

## Funcionalidades

- **Acesso Rápido às Pastas**: Permite que os alunos acessem suas pastas pessoais digitando sua matrícula.
- **Cópia do Caminho da Pasta**: Copia o caminho da pasta do aluno para a área de transferência.
- **Atualização de Links**: Modifica links em arquivos `.url` para garantir que estejam corretos.
- **Renomeação de Pastas**: Remove sufixos indesejados (como `.0`) das pastas dos alunos.
- **Correção de Nomes de Pastas**: Lê uma planilha Excel para corrigir nomes de pastas com base em informações atualizadas.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Tkinter**: Biblioteca para a interface gráfica.
- **Pandas**: Para manipulação de dados e leitura de planilhas Excel.
- **Pillow**: Para manipulação de imagens.

## Como Usar

### Pré-requisitos

1. Instalar Python (versão 3.6 ou superior).
2. Instalar as bibliotecas necessárias:
   ```bash
   pip install pandas pillow pyperclip



# README - Mudar o Apodigi das Apostilas

## Descrição

Este projeto consiste em um script Python que modifica o conteúdo de arquivos `.url` localizados em pastas de alunos. O objetivo é substituir a palavra "apodigi" por "digitalapos" nos links contidos nesses arquivos, garantindo que os links estejam corretos e atualizados.

## Funcionalidades

- **Modificação de Links**: O script percorre recursivamente as pastas dos alunos e altera o conteúdo dos arquivos `.url`, substituindo "apodigi" por "digitalapos".
- **Processamento de Arquivos**: O script lê o conteúdo dos arquivos `.url`, faz a modificação necessária e salva as alterações.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal utilizada para o desenvolvimento do script.
- **OS**: Módulo do Python utilizado para manipulação de diretórios e arquivos.


# README - Renomear Pasta Alunos de Matrícula Antiga para Matrícula Nova

## Descrição

Este script lê uma planilha Excel contendo nomes e matrículas e corrige os nomes das pastas dos alunos com base nas informações mais recentes. Ele remove sufixos indesejados e garante que as pastas estejam corretamente nomeadas.

## Funcionalidades

- Correção de nomes de pastas com base em uma planilha Excel.
- Remoção de sufixos indesejados das pastas.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Pandas**: Para leitura e manipulação de planilhas Excel.

## Como Usar

### Pré-requisitos

1. Instalar Python (versão 3.6 ou superior).
2. Instalar a biblioteca Pandas:
   ```bash
   pip install pandas
