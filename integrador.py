import random
import arquiteto
import escoteiro
import os
import datetime

# Lista massiva para o modo 24 horas (Alta Conversão)
temas_venda_rapida = [
    "Como calcular decimo terceiro", "Guia: Sair das Dividas em 30 dias",
    "Planilha Financeira Automática", "Como aumentar seu Score de Crédito",
    "Ganhar dinheiro com Milhas", "Manual do Reembolso de Impostos",
    "Aposentadoria Antecipada", "Direitos Trabalhistas Urgentes",
    "Como baixar parcelas do financiamento", "Segredo do Score 900",
    "Guia Prático: Limpar Nome sem Pagar", "Como declarar Cripto no IR",
    "Aumento de Limite de Cartão", "Como ganhar Cashback em tudo",
    "Renda Extra com ChatGPT", "Modelo de Petição para Pequenas Causas",
    "Como contestar multas de trânsito", "Guia do Auxílio Doença",
    "Planilha de Gastos 2026", "Como investir com 100 reais"
]

def gerar_sitemap():
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d")
    conteudo = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://ruiveira.github.io/solucoes-rapidas/</loc>
        <lastmod>{data_atual}</lastmod>
        <changefreq>hourly</changefreq>
        <priority>1.0</priority>
    </url>
</urlset>"""
    with open("sitemap.xml", "w") as f:
        f.write(conteudo)

def rodar_sistema():
    agora = datetime.datetime.now().strftime("%H:%M")
    print(f"--- NEXUS-ALPHA ATIVO ({agora}) ---")
    tema = random.choice(temas_venda_rapida)
    link = arquiteto.criar_produto_e_link(tema)
    escoteiro.criar_pagina_vendas(tema, link)
    gerar_sitemap()
    
    # Envia para o GitHub para manter o site vivo
    os.system("git add . && git commit -m 'Atualização Automática Nexus-Alpha' && git push origin main")
    print(f"--- SUCESSO: Produto '{tema}' no ar 24h ---")

if __name__ == "__main__":
    rodar_sistema()
