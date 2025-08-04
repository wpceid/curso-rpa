import PyPDF2

# Abrir arquivo PDF
with open('documento.pdf', 'rb') as arquivo:
    leitor = PyPDF2.PdfReader(arquivo)
    
    # Número de páginas
    num_paginas = len(leitor.pages)
    print(f"O documento tem {num_paginas} páginas.")
    
    # Extrair texto da primeira página
    pagina = leitor.pages[0]
    texto = pagina.extract_text()
    print(texto)