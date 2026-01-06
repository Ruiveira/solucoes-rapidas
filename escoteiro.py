import requests
import json

def buscar_demandas():
    # Buscaremos sementes de busca que indicam "necessidade de ferramenta"
    sementes = ["como calcular ", "gerador de ", "calculadora de ", "modelo de planilha "]
    demandas_encontradas = []

    for semente in sementes:
        # API de sugestão do Google (pública e gratuita)
        url = f"http://suggestqueries.google.com/complete/search?client=firefox&q={semente}"
        try:
            resposta = requests.get(url)
            # O Google retorna uma lista: [termo_original, [sugestoes]]
            sugestoes = resposta.json()[1] 
            demandas_encontradas.extend(sugestoes)
        except Exception as e:
            print(f"Erro ao buscar: {e}")
    
    return demandas_encontradas

if __name__ == "__main__":
    print("--- INICIANDO RASTREIO DE DEMANDAS ---")
    resultados = buscar_demandas()
    for r in resultados:
        print(f"Demanda detectada: {r}")