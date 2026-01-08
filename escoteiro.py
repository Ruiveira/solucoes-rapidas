import os

def criar_estilo():
    foto_unificada = "https://images.unsplash.com/photo-1551836022-d5d88e9218df?q=80&w=1600&auto=format&fit=crop"
    return f"""
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,800;1,800&family=Inter:wght@300;400;700&display=swap');
        body {{ font-family: 'Inter', sans-serif; background: #020617; color: #fff; margin: 0; scroll-behavior: smooth; overflow-x: hidden; }}
        .bg-hero {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, rgba(2, 6, 23, 0.9) 0%, rgba(2, 6, 23, 1) 100%), url('{foto_unificada}'); background-size: cover; background-position: center; z-index: -1; }}
        .titulo-master {{ font-family: 'Montserrat', sans-serif; font-weight: 800; letter-spacing: -0.05em; color: #39FF14; text-transform: uppercase; font-style: italic; }}
        .glass {{ background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(25px); border-radius: 2rem; }}
        .btn-venda {{ background: #39FF14 !important; color: #000 !important; font-family: 'Montserrat', sans-serif; font-weight: 800; transition: 0.3s; display: block; width: 100%; text-align: center; border-radius: 1rem; text-decoration: none; border: none; cursor: pointer; }}
        .btn-venda:hover {{ transform: scale(1.05); box-shadow: 0 0 50px rgba(57, 255, 20, 0.9); }}
        .valor-branco {{ color: #FFFFFF !important; font-family: 'Montserrat', sans-serif; font-weight: 800; }}
        .img-premium {{ width: 100%; border-radius: 1.5rem; border: 1px solid rgba(57, 255, 20, 0.3); }}
    </style>
    """

def obter_textos_legais(tipo):
    if tipo == "privacidade":
        return """<h2>Política de Privacidade</h2><p>Nexus Alpha System segue a LGPD. Coletamos nome e e-mail para processamento. Cookies analisam o mercado brasileiro (3-7s) para melhoria de UX.</p>"""
    return """<h2>Termos de Uso</h2><p>Contrato de uso Nexus Alpha. Garantia de 7 dias conforme CDC. Entrega imediata de produtos digitais.</p>"""

def obter_copy_vendas(tema):
    banco = {
        "Score 900 Turbo": {
            "headline": "ELEVE SEU SCORE PARA 900 PONTOS E DESTRAVE CRÉDITO BLACK IMEDIATAMENTE",
            "descricao": "O treinamento definitivo para limpar seu histórico e ativar os gatilhos de aprovação bancária.",
            "beneficios": "Consiga os melhores cartões do Brasil e financiamentos com taxas reduzidas.",
            "faq": "É seguro? Sim. Em quanto tempo? Resultados em até 15 dias.",
            "img": "https://images.unsplash.com/photo-1563986768609-322da13575f3?q=80&w=1200"
        },
        "Renda Extra": {
            "headline": "TRANSFORME SEU CELULAR EM UMA FONTE DE LUCRO DIÁRIO COM ARBITRAGEM",
            "descricao": "Método passo a passo para faturar executando micro-tarefas digitais.",
            "beneficios": "Liberdade financeira trabalhando apenas 1 hora por dia.",
            "faq": "Precisa de PC? Não. Precisa vender? Não.",
            "img": "https://images.unsplash.com/photo-1512428559087-560fa5ceab42?q=80&w=1200"
        },
        "Planilha Lucros": {
            "headline": "A PRIMEIRA PLANILHA IA QUE PROJETA SEUS LUCROS E CORTA GASTOS AUTOMATICAMENTE",
            "descricao": "Ferramenta de elite para controle de patrimônio e suporte exclusivo.",
            "beneficios": "Saiba exatamente quando você alcançará sua liberdade financeira.",
            "faq": "Funciona no celular? Sim. É mensalidade? Não.",
            "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1200"
        },
        "IA Investor Pro": {
            "headline": "IA INVESTOR PRO: O ROBÔ QUE OPERA TENDÊNCIAS DE MERCADO PARA VOCÊ",
            "descricao": "Algoritmo avançado que identifica as melhores oportunidades de investimento em tempo real.",
            "beneficios": "Tecnologia de ponta para quem busca rendimentos acima da média.",
            "faq": "Como recebo? Via e-mail após a compra. É difícil? Não, o robô faz o trabalho pesado.",
            "img": "https://images.unsplash.com/photo-1611974714658-058f40da23fb?q=80&w=1200"
        }
    }
    return banco.get(tema, banco["Score 900 Turbo"])

def gerar_layout_pagina(tema, preco, link, eh_produto=False, relacionados=[], legal_type=None):
    copy = obter_copy_vendas(tema)
    
    # RELACIONADOS SEM O PRODUTO ATUAL
    html_rel = ""
    for p in relacionados:
        if p['nome'] != tema:
            html_rel += f'''<a href="{p['slug']}.html" class="glass p-6 block hover:bg-white/10 text-center no-underline border border-white/5">
                <h4 class="titulo-master text-xs mb-1" style="color: #39FF14">{p['nome']}</h4>
                <p class="text-white font-bold">{p['preco']}</p></a>'''

    secao_rel = f"""<div class="mt-24 pt-10 border-t border-white/10"><h3 class="titulo-master text-center text-xl mb-8 italic">Outros Protocolos Elite</h3><div class="grid grid-cols-1 md:grid-cols-3 gap-6">{html_rel}</div></div>""" if relacionados else ""

    if legal_type:
        conteudo = f'<div class="glass p-12">{obter_textos_legais(legal_type)}</div>'
    elif eh_produto:
        conteudo = f"""
        <div class="text-center mb-16"><h1 class="titulo-master text-4xl md:text-7xl mb-6 italic">{copy['headline']}</h1></div>
        <div class="grid md:grid-cols-2 gap-12 items-center mb-20">
            <div class="glass p-2"><img src="{copy['img']}" class="img-premium"></div>
            <div class="space-y-6">
                <h3 class="titulo-master text-2xl italic">Descrição Detalhada:</h3>
                <p class="text-slate-300 text-lg">{copy['descricao']}</p>
                <div class="glass p-6"><p class="text-green-400 font-bold uppercase text-xs mb-2">Foco nos Benefícios</p><p>{copy['beneficios']}</p></div>
            </div>
        </div>
        <div class="glass p-10 text-center mb-20">
            <h3 class="titulo-master text-2xl mb-8 italic">AVALIAÇÃO</h3>
            <div class="grid md:grid-cols-2 gap-6 opacity-60 italic text-sm"><p>"Resultados rápidos." - Carlos R.</p><p>"Sistema impecável." - Julia M.</p></div>
        </div>
        <div class="glass p-12 text-center neon-border mb-20">
            <div class="valor-branco text-8xl md:text-9xl mb-10">{preco}</div>
            <a href="{link}" class="btn-venda py-8 text-3xl uppercase">ADQUIRIR AGORA</a>
            <div class="mt-8 flex items-center justify-center gap-4"><i class="fas fa-shield-alt text-2xl text-green-500"></i><span class="font-bold uppercase text-xs">Garantia 7 Dias</span></div>
        </div>
        <div class="glass p-10 mb-10"><h3 class="titulo-master text-center text-2xl mb-6 italic">FAQ</h3><p class="text-center italic opacity-70">{copy['faq']}</p></div>
        """
    else:
        conteudo = f'<h1 class="titulo-master text-7xl md:text-9xl mb-12 italic">#{tema}</h1><a href="detalhes.html" class="btn-venda py-6 text-xl max-w-sm">ENTRAR NO SISTEMA</a>'

    return f"""<!DOCTYPE html>
    <html lang="pt-br"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{tema} | Nexus Alpha</title>{criar_estilo()}</head>
    <body><div class="bg-hero"></div><div class="max-w-6xl mx-auto px-6 py-20">
    <header class="flex justify-between items-center mb-16"><a href="index.html" class="text-2xl font-black italic text-white no-underline">NEXUS<span class="text-green-500">ALPHA</span></a><div class="text-[10px] opacity-40 font-bold italic">V.2026 BR</div></header>
    {conteudo}{secao_rel}
    <footer class="mt-40 py-10 border-t border-white/10 text-[10px] opacity-40 text-center uppercase tracking-widest font-bold">
    <p>© 2026 Nexus Alpha System - Brasil</p><div class="mt-6 flex justify-center gap-8"><a href="privacidade.html" class="text-white no-underline hover:text-green-500">Privacidade</a><a href="termos.html" class="text-white no-underline hover:text-green-500">Termos</a></div></footer></div></body></html>"""

def criar_pagina_vendas(tema, link_stripe):
    link_final = "https://buy.stripe.com/9B6fZ976y7zJ6qn0jl4c80v"
    preco = "R$ 19,90"
    rel = [
        {"nome": "Score 900 Turbo", "preco": preco, "slug": "score", "link": link_final},
        {"nome": "Renda Extra", "preco": preco, "slug": "renda", "link": link_final},
        {"nome": "Planilha Lucros", "preco": preco, "slug": "planilha", "link": link_final},
        {"nome": "IA Investor Pro", "preco": preco, "slug": "ia-pro", "link": link_final}
    ]
    with open("index.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina(tema, preco, "detalhes.html"))
    with open("detalhes.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina(tema, preco, link_final, eh_produto=True, relacionados=rel))
    for p in rel:
        with open(f"{p['slug']}.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina(p['nome'], p['preco'], p['link'], eh_produto=True, relacionados=rel))
    with open("privacidade.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina("Privacidade", "", "", legal_type="privacidade"))
    with open("termos.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina("Termos", "", "", legal_type="termos"))
