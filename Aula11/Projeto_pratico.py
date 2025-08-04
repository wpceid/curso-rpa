import PyPDF2, re, pandas as pd

# Lista para armazenar dados extraídos
dados = []

# Processando múltiplos PDFs
for arquivo in ['nf1.pdf', 'nf2.pdf', 'nf3.pdf']:
    with open(arquivo, 'rb') as pdf:
        texto = PyPDF2.PdfReader(pdf).pages[0].extract_text()
        
        # Extrair número da NF
        nf_match = re.search(r'NF-e: (\d+)', texto)
        numero_nf = nf_match.group(1) if nf_match else 'N/A'
        
        # Extrair valor total
        valor_match = re.search(r'VALOR TOTAL R\$ ([\d.,]+)', texto)
        valor = valor_match.group(1) if valor_match else '0'
        
        # Adicionar à lista
        dados.append({'NF': numero_nf, 'Valor': valor})

# Criar DataFrame e exportar para Excel
df = pd.DataFrame(dados)
df.to_excel('relatorio_notas.xlsx', index=False)