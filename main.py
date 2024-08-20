import pandas as pd
from google_play_scraper import Sort, reviews

# Coleta das avaliações
result, continuation_token = reviews(
    'com.google.android.apps.googleassistant',    # ID do aplicativo - modifique para o link de página quedeseja avaliar
    lang='pt_BR',                                 # Linguagem
    sort=Sort.MOST_RELEVANT,                      # Mais relevantes
    count=50,                                     # Quantidade a ser coletada
    filter_score_with=None                        # Coleta todas as avaliações
)

# Cria um DataFrame com as avaliações
planilha = pd.DataFrame(result)

# Salva o DataFrame como um arquivo Excel (.xlsx)
planilha.to_excel("planilha googleplay.xlsx", index=False)

print("Arquivo Excel salvo como 'planilha_google_assistant_reviews.xlsx'.")
