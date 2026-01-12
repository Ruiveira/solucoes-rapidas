import escoteiro

def executar():
    link_compra = "https://buy.stripe.com/9B6fZ976y7zJ6qn0jl4c80v"
    
    produtos = [
        {"nome": "Score 900 Turbo", "slug": "score", "h1": "SCORE 900 TURBO", "desc": "Aumente seu crédito em tempo recorde.", "img": "https://images.unsplash.com/photo-1563986768609-322da13575f3?q=80&w=600"},
        {"nome": "Renda Extra", "slug": "renda", "h1": "RENDA EXTRA PIX", "desc": "Ganhe via Pix com arbitragem digital.", "img": "https://images.unsplash.com/photo-1512428559087-560fa5ceab42?q=80&w=600"},
        {"nome": "IA Investor Pro", "slug": "ia-pro", "h1": "IA INVESTOR PRO", "desc": "O robô que opera tendências reais.", "img": "https://images.squarespace-cdn.com/content/v1/5f973693e54f0a28f4f3e696/1706645353153-6U1V5X7X9P4Z4W5Z5X5Z/IA_Investor_Pro_Expert.jpg"},
        {"nome": "Drop Express IA", "slug": "drop", "h1": "DROP EXPRESS IA", "desc": "Lojas automáticas com inteligência.", "img": "https://images.unsplash.com/photo-1472851294608-062f824d29cc?q=80&w=600"},
        {"nome": "Vendas no Zap", "slug": "zap", "h1": "VENDAS NO ZAP", "desc": "Converta conversas em dinheiro.", "img": "https://images.unsplash.com/photo-1611746872915-64382b5c76da?q=80&w=600"},
        {"nome": "Hacker do Tráfego", "slug": "trafego", "h1": "HACKER DO TRÁFEGO", "desc": "Públicos ocultos revelados.", "img": "https://images.unsplash.com/photo-1551288049-bbbda5366392?q=80&w=600"}
    ]

    print(">>> ATUALIZANDO ECOSSISTEMA NEXUS ALPHA...")

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(escoteiro.gerar_layout_pagina("Home", "19,90", "ia-pro.html"))

    for p in produtos:
        with open(f"{p['slug']}.html", "w", encoding="utf-8") as f:
            f.write(escoteiro.gerar_layout_pagina(p['nome'], "19,90", link_compra, eh_produto=True, relacionados=produtos, copy_data=p))

    with open("privacidade.html", "w", encoding="utf-8") as f:
        f.write(escoteiro.gerar_layout_pagina("Privacidade", "", "", legal_body="Proteção total de dados Nexus."))
    with open("termos.html", "w", encoding="utf-8") as f:
        f.write(escoteiro.gerar_layout_pagina("Termos", "", "", legal_body="Garantia de 7 dias e suporte total."))

    print(">>> SUCESSO! Verifique o VS Code agora.")

if __name__ == "__main__":
    executar()