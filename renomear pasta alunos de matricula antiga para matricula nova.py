import os
import pandas as pd

# Caminho da planilha Excel e da pasta com as subpastas
planilha_path = r'C:\\matriculanova.xls'  # Substitua pelo caminho do seu arquivo Excel
diretorio_pastas = r'\\servidor\\Rede Lab2\\Alunos'  # Substitua pelo caminho onde as pastas estão localizadas

# Ler a planilha do Excel
df = pd.read_excel(planilha_path)

# Cria um dicionário de nome para matrícula
nomes_matriculas = dict(zip(df.iloc[:, 0], df.iloc[:, 1]))  # Coluna 1 = nome, Coluna 2 = matrícula

# Função para corrigir o nome da pasta
def corrigir_nome_pasta(pasta_nome):
    # Separar o nome e matrícula na pasta
    partes = pasta_nome.split(' - ')
    
    # Se houver mais de uma parte (nome e matrícula) e se a matrícula contiver ".0" ou estiver duplicada
    if len(partes) > 1:
        nome = partes[0]
        matriculas = partes[1].split(' ')
        
        # Remover ".0" da matrícula
        matricula = matriculas[0].replace('.0', '')
        
        # Verificar se a matrícula tem mais de uma parte (duplicada), manter apenas a primeira
        if len(matriculas) > 1:
            matricula = matricula  # Deixa apenas a primeira matrícula
        
        # Formatar o nome da pasta corretamente
        novo_nome = f"{nome} - {matricula}"
        return novo_nome
    return pasta_nome  # Retorna o nome original se não for possível corrigir

# Percorrer as pastas do diretório
for pasta in os.listdir(diretorio_pastas):
    pasta_path = os.path.join(diretorio_pastas, pasta)
    
    # Verifica se é um diretório
    if os.path.isdir(pasta_path):
        # Corrigir o nome da pasta com base na regra
        novo_nome = corrigir_nome_pasta(pasta)
        
        # Verificar se o nome da pasta precisa ser alterado
        if novo_nome != pasta:
            novo_caminho = os.path.join(diretorio_pastas, novo_nome)
            os.rename(pasta_path, novo_caminho)
            print(f"Pasta renomeada: {pasta} -> {novo_nome}")
        else:
            print(f"Pasta '{pasta}' já está com o nome correto.")
