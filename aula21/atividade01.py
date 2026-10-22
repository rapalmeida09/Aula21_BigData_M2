import subprocess
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


subprocess.run('cls', shell=True)
# Obtendo os dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    df_cvli = df_ocorrencias[['aisp', 'cvli']]
    
    df_cvli = df_cvli.groupby('aisp', as_index=False)['cvli'].sum()
    
    print(f'''\n-------------------------------------------
Crimes Violentos Letais Intencionais (CVLI)
-------------------------------------------
''')
    print(df_cvli)

except Exception as e:
    print(f'Erro ao obter os dados - {e}')

try:
    array_cvli = np.array(df_cvli['cvli'])

    media_cvli = np.mean(array_cvli)
    mediana_cvli = np.median(array_cvli)
    distancia_media_mediana = abs(
        (media_cvli - mediana_cvli) / mediana_cvli * 100
    )
    print(f'''\n---------------------------
Medias de tendência Central
---------------------------
Media: {media_cvli:.2f}
Mediana: {mediana_cvli}
Distancia: {distancia_media_mediana:.2f}
''')


except Exception as e:
    print(f'Obtendo Medidas - {e}')

try:
    q1 = np.quantile(array_cvli, .25) 
    q2 = np.quantile(array_cvli, .50)
    q3 = np.quantile(array_cvli, .75)

    print(f'''\n------------------
Medidas de Posição
------------------
Q1: {q1}
Q2: {q2}
Q3: {q3}
''')
    
    df_cvli_menores = df_cvli[
        df_cvli['cvli'] < q1
    ]

    df_cvli_maiores = df_cvli[
        df_cvli['cvli'] > q3
    ]

    print(f'''\n
-----------------------------------------
Batalhoes com Menos Ocorrencias de "CVLI"
-----------------------------------------
''')
    print(df_cvli_menores.sort_values(by='cvli', ascending=True))

    print(f'''\n
-----------------------------------------
Batalhoes com Mais Ocorrencias de "CVLI"
-----------------------------------------
''')
    print(df_cvli_maiores.sort_values(by='cvli', ascending=False))



except Exception as e:
    print(f'Erro ao Analizar a distribuição - {e}')