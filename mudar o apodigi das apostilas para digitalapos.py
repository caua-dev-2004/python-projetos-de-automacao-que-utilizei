import os
print('Iniciando o código')

# Caminho da pasta principal onde estão as pastas dos alunos
caminho_base = r'\\servidor\\Rede Lab2\\Alunos'  # Usar r para caminho com barra invertida

# Função para modificar o conteúdo dos arquivos .url
def modificar_link_arquivo(url_file):
    print(f"Processando o arquivo {url_file}...")
    try:
        # Abrir o arquivo .url e ler seu conteúdo
        with open(url_file, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        print(f"Conteúdo original do arquivo: {conteudo}")  # Verifica o conteúdo do arquivo

        # Substituir "digitalaposapos" por "digitalapos" no link do arquivo .url
        conteudo_modificado = conteudo.replace('apodigi', 'digitalapos')

        print(f"Conteúdo antes da modificação: {conteudo}")
        print(f"Conteúdo depois da modificação: {conteudo_modificado}")
        
        # Verificar se houve alguma modificação no conteúdo
        if conteudo != conteudo_modificado:
            # Se houve modificação, salvar o arquivo de volta
            with open(url_file, 'w', encoding='utf-8') as f:
                f.write(conteudo_modificado)
            print(f"Arquivo {url_file} atualizado com sucesso.")
        else:
            print(f"Nenhuma modificação necessária no arquivo {url_file}.")
    
    except Exception as e:
        print(f"Erro ao modificar o arquivo {url_file}: {e}")

# Função para percorrer recursivamente todas as pastas e arquivos dentro de 'arquivos_cursos'
def atualizar_links_pastas(caminho_base):
    # Percorre todas as pastas e subpastas de forma recursiva
    for root, dirs, files in os.walk(caminho_base):
        print(f"Verificando pasta: {root}")  # Verifica a pasta atual
        print(f"Arquivos encontrados: {files}")  # Verifica os arquivos encontrados
        for file in files:
            if file.endswith('.url'):  # Verifica se o arquivo termina com .url
                caminho_arquivo = os.path.join(root, file)  # Caminho completo do arquivo .url
                modificar_link_arquivo(caminho_arquivo)  # Modificar o conteúdo do arquivo .url

# Chama a função para iniciar o processo de atualização
atualizar_links_pastas(caminho_base)

print('Código finalizado')
