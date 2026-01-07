import escoteiro
import sitemap_gen
import notifier  # Novo módulo de aviso
import subprocess
import time

def rodar_sistema():
    print(f"--- NEXUS-ALPHA ATUALIZANDO ({time.strftime('%H:%M')}) ---")
    
    tema_principal = "Score 900 Turbo"
    link_stripe = "https://buy.stripe.com/9B6fZ976y7zJ6qn0jl4c80v"
    
    # 1. Design & SEO
    escoteiro.criar_pagina_vendas(tema_principal, link_stripe)
    sitemap_gen.gerar_sitemap()
    
    # 2. Publicação
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Nexus AI: Full Autonomy Update"], check=True)
        subprocess.run(["git", "push"], check=True)
        
        # 3. Notificação Automática no seu Celular
        msg = f"🚀 Nexus-Alpha Online!\n�� Valor: R$ 19,90\n📈 Tráfego Orgânico: Sitemap Atualizado.\n🤖 Robô: Vigilância Ativa."
        notifier.enviar_notificacao(msg)
        
        print("--- NEXUS STATUS: Notificação Enviada e Sistema Online ---")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    rodar_sistema()
