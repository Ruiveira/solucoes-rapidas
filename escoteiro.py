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
        
        /* BOTÃO PROPORCIONAL E ELITE */
        .btn-venda {{ background: #39FF14 !important; color: #000 !important; font-family: 'Montserrat', sans-serif; font-weight: 800; transition: 0.3s; display: inline-block; width: 100%; max-width: 450px; text-align: center; border-radius: 1rem; text-decoration: none; border: none; cursor: pointer; padding: 1.25rem 0; font-size: 1.5rem; }}
        .btn-venda:hover {{ transform: scale(1.02); box-shadow: 0 0 40px rgba(57, 255, 20, 0.6); }}
        
        /* VALOR AJUSTADO: R$ AO LADO DO NÚMERO */
        .valor-branco {{ color: #FFFFFF !important; font-family: 'Montserrat', sans-serif; font-weight: 800; font-size: 4rem; display: flex; align-items: center; justify-content: center; gap: 10px; line-height: 1; }}
        .valor-branco span {{ font-size: 1.8rem; opacity: 0.9; }}

        @media (max-width: 768px) {{
            .valor-branco {{ font-size: 3rem; }}
            .valor-branco span {{ font-size: 1.4rem; }}
            .btn-venda {{ font-size: 1.2rem; padding: 1rem 0; }}
        }}
        
        .img-premium {{ width: 100%; border-radius: 1.5rem; border: 2px solid #39FF14; box-shadow: 0 0 40px rgba(57, 255, 20, 0.3); }}
    </style>
    """

def obter_textos_legais(tipo):
    if tipo == "privacidade":
        return """<h2>Privacidade</h2><p>Nexus Alpha 2026. Análise de tendências (3-7s).</p>"""
    return """<h2>Termos</h2><p>Contrato de uso 2026.</p>"""

def obter_copy_vendas(tema):
    banco = {
        "Score 900 Turbo": {
            "headline": "ELEVE SEU SCORE PARA 900 PONTOS IMEDIATAMENTE",
            "descricao": "O melhor robô com a melhor IA limpando seu histórico e ativando gatilhos bancários.",
            "beneficios": "Consiga cartões Black e financiamentos imediatos.",
            "img": "https://images.unsplash.com/photo-1563986768609-322da13575f3?q=80&w=1200",
            "avaliacoes": ["'Meu score subiu em 12 dias!' - Ricardo S.", "'Finalmente aprovado no Nubank.' - Amanda L."]
        },
        "Renda Extra": {
            "headline": "LUCRO DIÁRIO COM ARBITRAGEM VIA CELULAR",
            "descricao": "Sistema de arbitragem IA para faturar com micro-tarefas digitais.",
            "beneficios": "Liberdade financeira total com 1h por dia.",
            "img": "https://images.unsplash.com/photo-1512428559087-560fa5ceab42?q=80&w=1200",
            "avaliacoes": ["'R$ 150 logo no primeiro dia.' - Marcos V.", "'Muito simples de usar.' - Beatriz F."]
        },
        "Planilha Lucros": {
            "headline": "PLANILHA IA: PROJEÇÃO DE PATRIMÔNIO ELITE",
            "descricao": "Ferramenta preditiva para controle total de ganhos e gastos.",
            "beneficios": "Acelere sua aposentaria com inteligência de dados.",
            "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1200",
            "avaliacoes": ["'Organizei 5 anos de dívidas em 1 hora.' - Paulo J.", "'A melhor ferramenta.' - Helena M."]
        },
        "IA Investor Pro": {
            "headline": "IA INVESTOR PRO: O SISTEMA QUE OPERA TENDÊNCIAS PARA VOCÊ",
            "descricao": "Algoritmo avançado que identifica lucros através de diagramas de tendência em tempo real.",
            "beneficios": "Tecnologia de ponta para automatizar sua rentabilidade.",
            "img": "https://images.squarespace-cdn.com/content/v1/5f973693e54f0a28f4f3e696/1706645353153-6U1V5X7X9P4Z4W5Z5X5Z/IA_Investor_Pro_Expert.jpg",
            "avaliacoes": ["'A IA é cirúrgica nos sinais.' - Gabriel T.", "'O robô trabalha por mim.' - Sofia R."]
        }
    }
    return banco.get(tema, banco["Score 900 Turbo"])

def gerar_layout_pagina(tema, preco, link, eh_produto=False, relacionados=[], legal_type=None):
    copy = obter_copy_vendas(tema)
    html_rel = ""
    for p in relacionados:
        if p['nome'] != tema:
            html_rel += f'''<a href="{p['slug']}.html" class="glass p-6 block hover:bg-white/10 text-center no-underline border border-white/5">
                <h4 class="titulo-master text-[10px] mb-1" style="color: #39FF14">{p['nome']}</h4>
                <p class="text-white font-bold text-sm">{p['preco']}</p></a>'''

    secao_rel = f"""<div class="mt-20 pt-10 border-t border-white/10"><h3 class="titulo-master text-center text-lg mb-8 italic">Outros Protocolos Elite</h3><div class="grid grid-cols-2 md:grid-cols-3 gap-4">{html_rel}</div></div>""" if relacionados else ""

    if legal_type:
        conteudo = f'<div class="glass p-12">{obter_textos_legais(legal_type)}</div>'
    elif eh_produto:
        html_avalia = "".join([f'<p class="mb-2 italic">"{a}"</p>' for a in copy['avaliacoes']])
        conteudo = f"""
        <div class="text-center mb-10"><h1 class="titulo-master text-3xl md:text-5xl mb-4 italic">{copy['headline']}</h1></div>
        <div class="grid md:grid-cols-2 gap-10 items-center mb-16">
            <div class="glass p-2"><img src="{copy['img']}" class="img-premium" alt="IMAGEM {tema}"></div>
            <div class="space-y-4">
                <h3 class="titulo-master text-xl italic text-white">O QUE VOCÊ LEVA:</h3>
                <p class="text-slate-300 text-base">{copy['descricao']}</p>
                <div class="glass p-4 text-sm"><p class="text-green-400 font-bold uppercase text-[10px] mb-1">Diferencial</p><p>{copy['beneficios']}</p></div>
            </div>
        </div>
        <div class="glass p-8 text-center mb-16">
            <h3 class="titulo-master text-xl mb-6 italic">AVALIAÇÃO</h3>
            <div class="grid md:grid-cols-2 gap-4 opacity-70 text-sm">{html_avalia}</div>
        </div>
        <div class="glass p-10 text-center mb-16">
            <div class="valor-branco mb-6"><span>R$</span> 19,90</div>
            <a href="{link}" class="btn-venda">ADQUIRIR AGORA</a>
            <div class="mt-6 flex items-center justify-center gap-3"><i class="fas fa-check-circle text-green-500"></i><span class="font-bold uppercase text-[10px] text-white">Acesso Imediato</span></div>
        </div>
        """
    else:
        conteudo = f'<h1 class="titulo-master text-6xl md:text-8xl mb-8 italic">#{tema}</h1><a href="detalhes.html" class="btn-venda">ENTRAR NO SISTEMA</a>'

    return f"""<!DOCTYPE html>
    <html lang="pt-br"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{tema} | Nexus Alpha</title>{criar_estilo()}</head>
    <body><div class="bg-hero"></div><div class="max-w-5xl mx-auto px-6 py-12">
    <header class="flex justify-between items-center mb-12"><a href="index.html" class="text-xl font-black italic text-white no-underline">NEXUS<span class="text-green-500">ALPHA</span></a><div class="text-[9px] opacity-40 font-bold italic text-white tracking-widest">FULL SYNC 24/7</div></header>
    {conteudo}{secao_rel}
    <footer class="mt-24 py-8 border-t border-white/10 text-[9px] opacity-40 text-center uppercase font-bold">
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
    for p in rel:
        with open(f"{p['slug']}.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina(p['nome'], p['preco'], p['link'], eh_produto=True, relacionados=rel))
    with open("privacidade.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina("Privacidade", "", "", legal_type="privacidade"))
    with open("termos.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina("Termos", "", "", legal_type="termos"))
