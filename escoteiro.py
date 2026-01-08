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
        .glass {{ background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(25px); border-radius: 1.5rem; }}
        
        /* BOTÃO AJUSTADO PARA NÃO QUEBRAR LINHA */
        .btn-venda {{ 
            background: #39FF14 !important; 
            color: #000 !important; 
            font-family: 'Montserrat', sans-serif; 
            font-weight: 800; 
            display: inline-flex; 
            align-items: center; 
            justify-content: center;
            width: 100%; 
            max-width: 400px; 
            border-radius: 0.8rem; 
            text-decoration: none; 
            padding: 1rem 0.5rem; 
            font-size: 1.4rem; 
            white-space: nowrap; 
            text-transform: uppercase;
        }}
        
        /* VALOR AJUSTADO LADO A LADO */
        .valor-branco {{ 
            color: #FFFFFF !important; 
            font-family: 'Montserrat', sans-serif; 
            font-weight: 800; 
            font-size: 3.5rem; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            gap: 8px; 
            white-space: nowrap;
        }}
        .valor-branco span {{ font-size: 1.5rem; }}

        /* RESPONSIVIDADE MOBILE ESTREITA */
        @media (max-width: 480px) {{
            .valor-branco {{ font-size: 2.8rem; }}
            .valor-branco span {{ font-size: 1.2rem; }}
            .btn-venda {{ font-size: 1.1rem; padding: 0.8rem 0.3rem; }}
            .titulo-master {{ font-size: 1.8rem !important; }}
        }}
        
        .img-premium {{ width: 100%; border-radius: 1rem; border: 1px solid #39FF14; box-shadow: 0 0 30px rgba(57, 255, 20, 0.2); }}
    </style>
    """

def obter_textos_legais(tipo):
    if tipo == "privacidade":
        return """<h2>Privacidade</h2><p>Nexus Alpha 2026. Analisamos tendências de 3-7s.</p>"""
    return """<h2>Termos</h2><p>Contrato de uso Nexus Alpha System.</p>"""

def obter_copy_vendas(tema):
    banco = {
        "Score 900 Turbo": {
            "headline": "SCORE 900 TURBO",
            "descricao": "IA limpando seu histórico e ativando gatilhos bancários.",
            "beneficios": "Aprovação imediata em cartões Black.",
            "img": "https://images.unsplash.com/photo-1563986768609-322da13575f3?q=80&w=1200",
            "avaliacoes": ["'Meu score subiu em 12 dias!' - Ricardo S.", "'Finalmente aprovado.' - Amanda L."]
        },
        "Renda Extra": {
            "headline": "RENDA EXTRA DIÁRIA",
            "descricao": "Sistema de arbitragem IA para faturar com micro-tarefas.",
            "beneficios": "Liberdade financeira com 1h por dia.",
            "img": "https://images.unsplash.com/photo-1512428559087-560fa5ceab42?q=80&w=1200",
            "avaliacoes": ["'R$ 150 no primeiro dia.' - Marcos V.", "'Muito simples.' - Beatriz F."]
        },
        "Planilha Lucros": {
            "headline": "PLANILHA IA ELITE",
            "descricao": "Controle total de ganhos e gastos com inteligência de dados.",
            "beneficios": "Acelere sua independência financeira.",
            "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1200",
            "avaliacoes": ["'Organizei tudo em 1 hora.' - Paulo J.", "'A melhor ferramenta.' - Helena M."]
        },
        "IA Investor Pro": {
            "headline": "IA INVESTOR PRO",
            "descricao": "Algoritmo avançado identificando lucros em tempo real.",
            "beneficios": "Tecnologia de ponta para automatizar rentabilidade.",
            "img": "https://images.squarespace-cdn.com/content/v1/5f973693e54f0a28f4f3e696/1706645353153-6U1V5X7X9P4Z4W5Z5X5Z/IA_Investor_Pro_Expert.jpg",
            "avaliacoes": ["'IA cirúrgica nos sinais.' - Gabriel T.", "'O robô trabalha por mim.' - Sofia R."]
        }
    }
    return banco.get(tema, banco["Score 900 Turbo"])

def gerar_layout_pagina(tema, preco, link, eh_produto=False, relacionados=[], legal_type=None):
    copy = obter_copy_vendas(tema)
    html_rel = ""
    for p in relacionados:
        if p['nome'] != tema:
            html_rel += f'''<a href="{p['slug']}.html" class="glass p-4 block hover:bg-white/10 text-center no-underline border border-white/5">
                <h4 class="titulo-master text-[9px] mb-1" style="color: #39FF14">{p['nome']}</h4>
                <p class="text-white font-bold text-xs">{p['preco']}</p></a>'''

    secao_rel = f"""<div class="mt-16 pt-8 border-t border-white/10"><h3 class="titulo-master text-center text-sm mb-6 italic">Outros Protocolos Elite</h3><div class="grid grid-cols-2 md:grid-cols-3 gap-3">{html_rel}</div></div>""" if relacionados else ""

    if legal_type:
        conteudo = f'<div class="glass p-8">{obter_textos_legais(legal_type)}</div>'
    elif eh_produto:
        html_avalia = "".join([f'<p class="mb-1 italic">"{a}"</p>' for a in copy['avaliacoes']])
        conteudo = f"""
        <div class="text-center mb-8"><h1 class="titulo-master text-2xl md:text-5xl italic">{copy['headline']}</h1></div>
        <div class="grid md:grid-cols-2 gap-8 items-center mb-12">
            <div class="glass p-2"><img src="{copy['img']}" class="img-premium" alt="IMAGEM {tema}"></div>
            <div class="space-y-4">
                <p class="text-slate-300 text-sm text-center md:text-left">{copy['descricao']}</p>
                <div class="glass p-4 text-[11px]"><p class="text-green-400 font-bold uppercase mb-1">Diferencial</p><p>{copy['beneficios']}</p></div>
            </div>
        </div>
        <div class="glass p-6 text-center mb-12">
            <h3 class="titulo-master text-lg mb-4 italic">AVALIAÇÃO</h3>
            <div class="grid md:grid-cols-2 gap-3 opacity-70 text-[11px]">{html_avalia}</div>
        </div>
        <div class="glass p-8 text-center mb-12">
            <div class="valor-branco mb-4"><span>R$</span> 19,90</div>
            <a href="{link}" class="btn-venda">ADQUIRIR AGORA</a>
            <div class="mt-4 flex items-center justify-center gap-2 text-[10px] font-bold uppercase"><i class="fas fa-check-circle text-green-500"></i><span>Acesso Imediato</span></div>
        </div>
        """
    else:
        conteudo = f'<h1 class="titulo-master text-5xl md:text-8xl mb-8 italic">#{tema}</h1><a href="detalhes.html" class="btn-venda">ENTRAR NO SISTEMA</a>'

    return f"""<!DOCTYPE html>
    <html lang="pt-br"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{tema} | Nexus Alpha</title>{criar_estilo()}</head>
    <body><div class="bg-hero"></div><div class="max-w-4xl mx-auto px-5 py-10">
    <header class="flex justify-between items-center mb-10"><a href="index.html" class="text-lg font-black italic text-white no-underline">NEXUS<span class="text-green-500">ALPHA</span></a><div class="text-[8px] opacity-40 font-bold italic text-white">FULL SYNC 24/7</div></header>
    {conteudo}{secao_rel}
    <footer class="mt-20 py-6 border-t border-white/10 text-[8px] opacity-40 text-center uppercase font-bold">
    <p>© 2026 Nexus Alpha System</p></footer></div></body></html>"""

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
    for p in rel:
        with open(f"{p['slug']}.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina(p['nome'], p['preco'], p['link'], eh_produto=True, relacionados=rel))
    with open("privacidade.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina("Privacidade", "", "", legal_type="privacidade"))
    with open("termos.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina("Termos", "", "", legal_type="termos"))
