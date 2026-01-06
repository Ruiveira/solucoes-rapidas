import random
import arquiteto
import escoteiro
import os

temas_venda_rapida = [
    "Como calcular decimo terceiro", "Guia: Sair das Dividas em 30 dias",
    "Planilha Financeira Automática", "Como aumentar seu Score de Crédito",
    "Ganhar dinheiro com Milhas", "Manual do Reembolso de Impostos",
    "Aposentadoria Antecipada: O Guia", "Direitos Trabalhistas: Guia Urgente"
]

def gerar_sitemap():
    # Este código cria o mapa que o Google usa para te achar sozinho
    conteudo = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://ruiveira.github.io/solucoes-rapidas/</loc>
        <lastmod>2026-01-06</lastmod>
        <changefreq>daily</changefreq>
        <priority>1.0</priority>
    </url>
</urlset>"""
    with open("sitemap.xml", "w") as f:
        f.write(conteudo)
    print("--- SITEMAP GERADO PARA O GOOGLE ---")

def rodar_sistema():
    print("--- SISTEMA NEXUS-ALPHA: MODO ALTA CONVERSÃO ---")
    tema = random.choice(temas_venda_rapida)
    print(f"Produto de Alta Probabilidade: {tema}")
    link = arquiteto.criar_produto_e_link(tema)
    escoteiro.criar_pagina_vendas(tema, link)
    gerar_sitemap()
    print(f"--- SUCESSO! Robô escolheu e publicou: {tema} ---")

if __name__ == "__main__":
    rodar_sistema()
