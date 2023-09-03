import os
import fitz  # PyMuPDF

# Pasta onde os PDFs estão localizados
pasta_origem = 'C:/Users/Mailon/Downloads/17.04.2023'

# Inicializa a variável para armazenar o número total de páginas
numero_total_de_paginas = 0

# Verifica se a pasta de origem existe
if os.path.exists(pasta_origem):
    # Loop pelos arquivos na pasta
    for arquivo in os.listdir(pasta_origem):
        # Verifica se o arquivo é um PDF
        if arquivo.endswith('.pdf'):
            # Caminho completo para o arquivo PDF
            pdf_path = os.path.join(pasta_origem, arquivo)

            try:
                # Abre o arquivo PDF
                doc = fitz.open(pdf_path)

                # Obtém o número de páginas do PDF
                numero_de_paginas = doc.page_count

                # Adiciona o número de páginas do PDF ao total
                numero_total_de_paginas += numero_de_paginas

                # Fecha o arquivo PDF
                doc.close()
            except Exception as e:
                # Em caso de erro ao abrir o PDF, imprime a mensagem de erro
                print(f"Erro ao processar o arquivo {arquivo}: {str(e)}")

    # Imprime o número total de páginas
    print(f"Número total de páginas em todos os PDFs: {numero_total_de_paginas}")
else:
    print(f"A pasta {pasta_origem} não existe.")
