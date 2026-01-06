import random, arquiteto, escoteiro, os, datetime

# Temas com gatilhos de "Desejo de Alívio"
temas_magneticos = [
    "Recuperação de Impostos Retidos", "O Segredo do Score 900",
    "Protocolo: Sair das Dívidas", "Manual da Renda Extra Online",
    "Estratégia: Juros Abusivos Nunca Mais", "Investimento Blindado",
    "Como Baixar Parcelas do Carro", "Auxílio Doença sem Erros"
]

def rodar_sistema():
    print(f"--- NEXUS-ALPHA ATUALIZANDO ({datetime.datetime.now().strftime('%H:%M')}) ---")
    tema = random.choice(temas_magneticos)
    link = arquiteto.criar_produto_e_link(tema)
    escoteiro.criar_pagina_vendas(tema, link)
    
    # Atualiza Sitemap para SEO Orgânico
    with open("sitemap.xml", "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://ruiveira.github.io/solucoes-rapidas/</loc><changefreq>hourly</changefreq></url></urlset>')

    os.system("git add . && git commit -m 'Nexus-Alpha: Psicologia de Vendas Aplicada' && git push origin main")
    print(f"--- SUCESSO: '{tema}' está vendendo agora ---")

if __name__ == "__main__":
    rodar_sistema()
