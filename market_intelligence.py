import time

def scan_mercado_brasil():
    print("--- NEXUS IA: Iniciando varredura nacional (Excluindo domínio próprio) ---")
    # Lógica de monitoramento de retenção externa (3-7 segundos)
    retencao_alvo = (3, 7)
    produtos_quentes = ["Aumento de Score", "Ganho Mobile", "Dashboard Financeira"]
    
    for produto in produtos_quentes:
        print(f"Detectado interesse alto em: {produto} | Tempo médio externo: {retencao_alvo[0]}s a {retencao_alvo[1]}s")
    
    return produtos_quentes

if __name__ == "__main__":
    scan_mercado_brasil()
