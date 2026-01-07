import escoteiro
import sitemap_gen
import subprocess
import time

def rodar_sistema():
    print(f"--- NEXUS-ALPHA ATUALIZANDO ({time.strftime('%H:%M')}) ---")
    
    # 1. Gera as páginas com o design de Alta Performance
    tema_principal = "Score 900 Turbo"
    link_stripe = "https://buy.stripe.com/9B6fZ976y7zJ6qn0jl4c80v"
    escoteiro.criar_pagina_vendas(tema_principal, link_stripe)
    
    # 2. Gera o Sitemap para Tráfego Orgânico Grátis
    sitemap_gen.gerar_sitemap()
    
    # 3. Publica tudo automaticamente no GitHub
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Nexus AI: SEO & Design Update"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("--- NEXUS STATUS: Tudo Online e Indexado ---")
    except Exception as e:
        print(f"Erro na publicação: {e}")

if __name__ == "__main__":
    rodar_sistema()
