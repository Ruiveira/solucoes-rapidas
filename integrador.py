import escoteiro
import sitemap_gen
import notifier
import subprocess
import time

def rodar_sistema():
    print(f"--- NEXUS-ALPHA ATUALIZANDO ({time.strftime('%H:%M')}) ---")
    
    tema_principal = "Score 900 Turbo"
    link_stripe = "https://buy.stripe.com/9B6fZ976y7zJ6qn0jl4c80v"
    
    # 1. Design & SEO
    escoteiro.criar_pagina_vendas(tema_principal, link_stripe)
    sitemap_gen.gerar_sitemap()
    
    # 2. Publicação Inteligente
    try:
        subprocess.run(["git", "add", "."], check=True)
        # Tenta o commit; se não houver mudanças, o 'and' impede o erro de travar o fluxo
        result = subprocess.run(["git", "commit", "-m", "Nexus AI: Full Autonomy Update"], capture_output=True, text=True)
        
        if "nothing to commit" in result.stdout or result.returncode == 0:
            subprocess.run(["git", "push"], check=True)
            
            # 3. Notificação de Sucesso
            msg = "🚀 Nexus-Alpha: Sistema Online e Sincronizado!"
            notifier.enviar_notificacao(msg)
            print("--- NEXUS STATUS: Notificação Enviada e Sistema Online ---")
        else:
            print(f"Aviso Git: {result.stderr}")
            
    except Exception as e:
        print(f"Status: Arquivos já estão atualizados no servidor.")

if __name__ == "__main__":
    rodar_sistema()
