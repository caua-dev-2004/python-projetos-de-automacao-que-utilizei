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