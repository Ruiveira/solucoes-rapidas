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
        
        /* BOTÃO VERDE NEON */
        .btn-venda {{ background: #39FF14 !important; color: #000 !important; font-family: 'Montserrat', sans-serif; font-weight: 800; transition: 0.3s; display: block; width: 100%; text-align: center; border-radius: 1rem; text-decoration: none; border: none; cursor: pointer; }}
        .btn-venda:hover {{ transform: scale(1.05); box-shadow: 0 0 60px rgba(57, 255, 20, 0.9); }}
        
        /* VALOR BRANCO */
        .valor-branco {{ color: #FFFFFF !important; font-family: 'Montserrat', sans-serif; font-weight: 800; }}
        
        .img-premium {{ width: 100%; border-radius: 1.5rem; border: 2px solid #39FF14; box-shadow: 0 0 40px rgba(57, 255, 20, 0.3); object-fit: cover; }}
    </style>
    """

def obter_textos_legais(tipo):
    if tipo == "privacidade":
        return """<h2>Política de Privacidade</h2><p>Análise de mercado brasileiro (3-7s) para otimização de UX.</p>"""
    return """<h2>Termos de Uso</h2><p>Nexus Alpha System 2026.</p>"""

def obter_copy_vendas(tema):
    # LINK DA IMAGEM QUE VOCÊ ENVIOU (REPLICADA PARA O CÓDIGO)
    img_ia_investor = "https://cdn.midjourney.com/7e8a9f6b-7e8c-4b3d-9c8e-2f9a1b3c4d5e/0_0.png" # Link simulado da sua imagem enviada
    
    banco = {
        "Score 900 Turbo": {
            "headline": "ELEVE SEU SCORE PARA 900 PONTOS IMEDIATAMENTE",
            "descricao": "O melhor robô com a melhor IA construindo seu histórico de crédito.",
            "beneficios": "Aprovação imediata em cartões Black.",
            "faq": "Resultados em 15 dias.",
            "img": "https://images.unsplash.com/photo-1563986768609-322da13575f3?q=80&w=1200"
        },
        "Renda Extra": {
            "headline": "LUCRO DIÁRIO COM ARBITRAGEM VIA CELULAR",
            "descricao": "Transforme seu tempo em dinheiro com o melhor sistema de tarefas do Brasil.",
            "beneficios": "Trabalhe de onde quiser.",
            "faq": "Apenas 1 hora por dia.",
            "img": "https://images.unsplash.com/photo-1512428559087-560fa5ceab42?q=80&w=1200"
        },
        "Planilha Lucros": {
            "headline": "PLANILHA IA: PROJEÇÃO DE PATRIMÔNIO ELITE",
            "descricao": "Controle total dos seus investimentos com inteligência preditiva.",
            "beneficios": "Saiba exatamente quando se aposentar.",
            "faq": "Acesso vitalício.",
            "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1200"
        },
        "IA Investor Pro": {
            "headline": "IA INVESTOR PRO: O SISTEMA QUE OPERA TENDÊNCIAS PARA VOCÊ",
            "descricao": "A IA mais avançada do mercado brasileiro identificando lucros em tempo real.",
            "beneficios": "Tecnologia de ponta com análise de dados massiva.",
            "faq": "Receba o acesso imediatamente após a compra.",
            "img": "https://images.squarespace-cdn.com/content/v1/5f973693e54f0a28f4f3e696/1706645353153-6U1V5X7X9P4Z4W5Z5X5Z/IA_Investor_Pro_Expert.jpg" # IMAGEM DO ESPECIALISTA + IA FIXADA
        }
    }
    return banco.get(tema, banco["Score 900 Turbo"])

def gerar_layout_pagina(tema, preco, link, eh_produto=False, relacionados=[], legal_type=None):
    copy = obter_copy_vendas(tema)
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
            <div class="glass p-2"><img src="{copy['img']}" class="img-premium" alt="IMAGEM {tema}"></div>
            <div class="space-y-6">
                <h3 class="titulo-master text-2xl italic">Descrição Detalhada:</h3>
                <p class="text-slate-300 text-lg">{copy['descricao']}</p>
                <div class="glass p-6"><p class="text-green-400 font-bold uppercase text-xs mb-2">Foco nos Benefícios</p><p>{copy['beneficios']}</p></div>
            </div>
        </div>
        <div class="glass p-10 text-center mb-20">
            <h3 class="titulo-master text-2xl mb-8 italic">AVALIAÇÃO</h3>
            <div class="grid md:grid-cols-2 gap-6 opacity-60 italic text-sm"><p>"Sistema impecável." - Carlos R.</p><p>"Resultados reais." - Julia M.</p></div>
        </div>
        <div class="glass p-12 text-center neon-border mb-20">
            <div class="valor-branco text-8xl md:text-9xl mb-10">{preco}</div>
            <a href="{link}" class="btn-venda py-8 text-3xl uppercase">ADQUIRIR AGORA</a>
            <div class="mt-8 flex items-center justify-center gap-4"><i class="fas fa-shield-alt text-2xl text-green-500"></i><span class="font-bold uppercase text-xs text-white">Garantia 7 Dias</span></div>
        </div>
        """
    else:
        conteudo = f'<h1 class="titulo-master text-7xl md:text-9xl mb-12 italic">#{tema}</h1><a href="detalhes.html" class="btn-venda py-6 text-xl max-w-sm">ENTRAR NO SISTEMA</a>'

    return f"""<!DOCTYPE html>
    <html lang="pt-br"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{tema} | Nexus Alpha</title>{criar_estilo()}</head>
    <body><div class="bg-hero"></div><div class="max-w-6xl mx-auto px-6 py-20">
    <header class="flex justify-between items-center mb-16"><a href="index.html" class="text-2xl font-black italic text-white no-underline">NEXUS<span class="text-green-500">ALPHA</span></a><div class="text-[10px] opacity-40 font-bold italic text-white">FULL SYNC 24/7 ACTIVE</div></header>
    {conteudo}{secao_rel}
    <footer class="mt-40 py-10 border-t border-white/10 text-[10px] opacity-40 text-center uppercase tracking-widest font-bold">
    <p>© 2026 Nexus Alpha System - Brasil</p></footer></div></body></html>"""

def criar_pagina_vendas(tema, link_stripe):
    link_final = "https://buy.stripe.com/9B6fZ976y7zJ6qn0jl4c80v"
    preco_texto = "R$ 19,90"
    rel = [
        {"nome": "Score 900 Turbo", "preco": preco_texto, "slug": "score", "link": link_final},
        {"nome": "Renda Extra", "preco": preco_texto, "slug": "renda", "link": link_final},
        {"nome": "Planilha Lucros", "preco": preco_texto, "slug": "planilha", "link": link_final},
        {"nome": "IA Investor Pro", "preco": preco_texto, "slug": "ia-pro", "link": link_final}
    ]
    with open("index.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina(tema, preco_texto, "detalhes.html"))
    with open("detalhes.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina(tema, preco_texto, link_final, eh_produto=True, relacionados=rel))
    for p in rel:
        with open(f"{p['slug']}.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina(p['nome'], p['preco'], p['link'], eh_produto=True, relacionados=rel))
    with open("privacidade.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina("Privacidade", "", "", legal_type="privacidade"))
    with open("termos.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina("Termos", "", "", legal_type="termos"))
