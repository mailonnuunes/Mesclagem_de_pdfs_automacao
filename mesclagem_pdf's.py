import os
import fitz  # PyMuPDF
from datetime import datetime

# Pasta onde os PDFs estão localizados
pasta_origem = 'C:/Users/Mailon/Downloads/17.04.2023'

# Verifica se a pasta de origem existe
if os.path.exists(pasta_origem):
    pdfs_validos = []  # Lista para armazenar os PDFs válidos
    pdfs_problema = []  # Lista para armazenar os PDFs com problemas
    
    # Loop pelos arquivos na pasta
    for arquivo in os.listdir(pasta_origem):
        # Verifica se o arquivo é um PDF
        if arquivo.endswith('.pdf'):
            # Caminho completo para o arquivo PDF
            pdf_path = os.path.join(pasta_origem, arquivo)
            
            try:
                # Tenta abrir o arquivo PDF
                doc = fitz.open(pdf_path)
                
                # Se a abertura do PDF for bem-sucedida, consideramos o PDF "OK" e o adicionamos à lista
                pdfs_validos.append(doc)
                
            except Exception as e:
                # Se houver um erro ao abrir o PDF, adicionamos o arquivo à lista de PDFs com problemas
                print(f"Erro ao processar o arquivo {arquivo}: {str(e)}")
                pdfs_problema.append(pdf_path)
    
    # Verifica se há PDFs válidos para mesclar
    if pdfs_validos:
        # Cria um novo documento PDF de saída
        pdf_output = fitz.open()
        
        # Adiciona todas as páginas dos PDFs válidos ao PDF de saída
        for doc in pdfs_validos:
            pdf_output.insert_pdf(doc)
            doc.close()  # Fecha cada PDF de entrada
        
        # Caminho completo para o arquivo PDF de saída na pasta "pdfs mesclados" dentro da pasta de origem
        pasta_saida = os.path.join(pasta_origem, 'pdfs mesclados')
        os.makedirs(pasta_saida, exist_ok=True)  # Cria a pasta de saída se ela não existir
        
        pdf_saida = os.path.join(pasta_saida, 'pdf_mesclado.pdf')
        
        # Salva o PDF mesclado na pasta "pdfs mesclados"
        pdf_output.save(pdf_saida)
        pdf_output.close()  # Fecha o PDF de saída após salvar
        print(f"PDFs válidos mesclados com sucesso em '{pdf_saida}'")
    else:
        print("Nenhum PDF válido encontrado para mesclar.")
    
    # Mescla o arquivo "pdf_mesclado_com_problema.pdf" com o "pdf_mesclado.pdf"
    pdf_mesclado_final = fitz.open(pdf_saida)
    
    for pdf_path in pdfs_problema:
        pdf_com_problema = fitz.open(pdf_path)
        pdf_mesclado_final.insert_pdf(pdf_com_problema)
        pdf_com_problema.close()
    
    # Caminho completo para o arquivo PDF final
    pdf_saida_final = os.path.join(pasta_saida, 'pdf_mesclado_versao_final.pdf')
    
    # Salva o PDF final
    pdf_mesclado_final.save(pdf_saida_final)
    pdf_mesclado_final.close()  # Fecha o PDF final após salvar
    print(f"PDFs mesclados com sucesso em '{pdf_saida_final}'")
     # Exclui o arquivo intermediário "pdf_mesclado.pdf"
    pdf_saida_intermediario = os.path.join(pasta_saida, 'pdf_mesclado.pdf')
    if os.path.exists(pdf_saida_intermediario):
        os.remove(pdf_saida_intermediario)
else:
    print(f"A pasta {pasta_origem} não existe.")
