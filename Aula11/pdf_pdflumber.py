import pdfplumber

with pdfplumber.open('documento.pdf') as pdf:
    # Extrai a primeira página
    primeira_pagina = pdf.pages[0]
    
    # Extrai texto
    texto = primeira_pagina.extract_text()
    print(texto)
    # Extrai tabelas
    tabelas = primeira_pagina.extract_tables()
    
    # Processando a primeira tabela encontrada
    if tabelas:
        tabela = tabelas[0]
        # Converter para DataFrame
        import pandas as pd
        df = pd.DataFrame(tabela[1:], columns=tabela[0])
        print(df)