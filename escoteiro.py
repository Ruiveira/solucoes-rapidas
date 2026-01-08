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
        .btn-venda {{ background: #39FF14; color: #000; font-family: 'Montserrat', sans-serif; font-weight: 800; transition: 0.3s; display: block; width: 100%; text-align: center; border-radius: 1rem; text-decoration: none; border: none; cursor: pointer; }}
        .btn-venda:hover {{ transform: scale(1.05); box-shadow: 0 0 50px rgba(57, 255, 20, 0.6); }}
        .neon-border {{ border: 1px solid #39FF14; }}
        .img-venda {{ width: 100%; border-radius: 1.5rem; border: 1px solid rgba(57, 255, 20, 0.3); box-shadow: 0 0 30px rgba(0,0,0,0.5); }}
        .conteudo-legal h2 {{ color: #39FF14; font-family: 'Montserrat', sans-serif; text-transform: uppercase; margin-top: 2rem; margin-bottom: 1rem; border-bottom: 1px solid rgba(57,255,20,0.2); }}
        .conteudo-legal p, .conteudo-legal li {{ margin-bottom: 1rem; opacity: 0.8; line-height: 1.8; text-align: justify; }}
    </style>
    """

def obter_textos_legais(tipo):
    if tipo == "privacidade":
        return """<h2>Política de Privacidade</h2><p>A Nexus Alpha System preza pela transparência. Coletamos nome e e-mail para processar seu acesso. Seus dados são protegidos pela LGPD.</p><ul><li>Uso de Cookies para análise de mercado externo (3-7s);</li><li>Compartilhamento seguro apenas com Stripe;</li><li>Direito de exclusão total via suporte@nexusalpha.com.</li></ul>"""
    return """<h2>Termos de Uso</h2><p>Ao utilizar este sistema, você concorda com nossas diretrizes. Oferecemos garantia de 7 dias conforme o CDC e entrega imediata do conteúdo digital.</p><ul><li>Proibido engenharia reversa do código Nexus;</li><li>Direitos Autorais protegidos;</li><li>Foro da Comarca Sede para resoluções legais.</li></ul>"""

def obter_dados_copy(tema):
    banco = {
        "Score 900 Turbo": {
            "headline": "AUMENTE SEU SCORE PARA 900 PONTOS E DESTRAVE CRÉDITO IMEDIATO",
            "desc": "O mapa secreto para manipular os algoritmos bancários a seu favor e conseguir limites altos.",
            "mods": ["Módulo 1: O Segredo do Serasa", "Módulo 2: Limpeza de Consultas", "Módulo 3: Gatilhos de Aprovação"],
            "benefs": "Aprovação garantida de cartões Black e financiamentos sem burocracia.",
            "faq": "Funciona para todos? Sim, desde que siga o método. É legal? 100% dentro da lei.",
            "img": "https://images.unsplash.com/photo-1563986768609-322da13575f3?q=80&w=800"
        },
        "Renda Extra": {
            "headline": "TRANSFORME SEU SMARTPHONE EM UMA FONTE DE LUCROS DIÁRIOS",
            "desc": "Ganhe dinheiro executando micro-tarefas e arbitragem digital validada pela nossa IA.",
            "mods": ["Módulo 1: Setup da Máquina", "Módulo 2: Operações em Tempo Real", "Módulo 3: Escala de Ganhos"],
            "benefs": "Trabalhe de qualquer lugar e receba via Stripe com total segurança.",
            "faq": "Preciso investir? Não. Quanto tempo por dia? Apenas 30 minutos iniciais.",
            "img": "https://images.unsplash.com/photo-1512428559087-560fa5ceab42?q=80&w=800"
        },
        "Planilha Lucros": {
            "headline": "A FERRAMENTA IA QUE PROJETA SEUS LUCROS E CORTA GASTOS",
            "desc": "Visualize sua liberdade financeira com um dashboard que trabalha sozinho para você.",
            "mods": ["Módulo 1: Importação IA", "Módulo 2: Gráficos de Projeção", "Módulo 3: Plano de Liberdade"],
            "benefs": "Nunca mais perca dinheiro e saiba exatamente quando será livre financeiramente.",
            "faq": "Funciona no Mac? Sim, em qualquer navegador. Precisa de Excel? Não.",
            "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800"
        }
    }
    return banco.get(tema, banco["Score 900 Turbo"])

def gerar_layout_pagina(tema, preco, link, eh_detalhes=False, relacionados=[], legal_type=None):
    info = obter_dados_copy(tema)
    
    html_rel = ""
    if relacionados:
        for p in relacionados:
            html_rel += f'''<a href="{p['slug']}.html" class="glass p-6 block hover:bg-white/10 text-center no-underline border border-white/5">
                <h4 class="titulo-master text-xs mb-1" style="color: #39FF14">{p['nome']}</h4>
                <p class="text-white font-bold">{p['preco']}</p></a>'''

    secao_rel = f"""<div class="mt-20 pt-10 border-t border-white/10"><h3 class="titulo-master text-center text-xl mb-6 italic">Protocolos Relacionados</h3><div class="grid grid-cols-1 md:grid-cols-3 gap-4">{html_rel}</div></div>""" if relacionados else ""

    if legal_type:
        conteudo = f'<div class="glass p-12 conteudo-legal">{obter_textos_legais(legal_type)}</div>'
    elif eh_detalhes:
        conteudo = f"""
        <div class="text-center mb-16"><h1 class="titulo-master text-4xl md:text-7xl mb-6 italic">{info['headline']}</h1><p class="italic opacity-70">{info['desc']}</p></div>
        <div class="grid md:grid-cols-2 gap-10 mb-16 items-center">
            <div class="glass p-2 neon-border"><img src="{info['img']}" class="img-venda"></div>
            <div class="glass p-8"><h3 class="titulo-master text-xl mb-6 italic">O que você recebe:</h3><ul class="space-y-3">{" ".join([f'<li><i class="fas fa-check text-green-500 mr-2"></i> {m}</li>' for m in info['mods']])}</ul><p class="mt-6 text-sm text-slate-400"><b>Benefício Real:</b> {info['benefs']}</p></div>
        </div>
        <div class="glass p-12 text-center neon-border mb-16">
            <h3 class="titulo-master text-xl mb-4 italic">Prova Social: "O melhor sistema de 2026!"</h3>
            <div class="titulo-master text-8xl my-8">{preco}</div>
            <a href="{link}" class="btn-venda py-8 text-2xl uppercase">ADQUIRIR AGORA</a>
            <div class="flex justify-center gap-6 mt-6 opacity-50 text-2xl"><i class="fab fa-cc-visa"></i><i class="fab fa-cc-mastercard"></i><i class="fab fa-apple-pay"></i><i class="fas fa-barcode"></i></div>
            <div class="mt-8 text-green-400 font-bold text-xs"><i class="fas fa-shield-alt"></i> GARANTIA INCONDICIONAL DE 7 DIAS</div>
        </div>
        <div class="glass p-8 mb-16"><h3 class="titulo-master text-center mb-6 italic">FAQ - Perguntas Frequentes</h3><p class="text-center italic opacity-70">{info['faq']}</p></div>
        <p class="text-center opacity-40 text-[10px]">Dúvidas: suporte@nexusalpha.com</p>
        """
    else:
        conteudo = f'<h1 class="titulo-master text-7xl md:text-9xl mb-12 italic">#{tema}</h1><a href="detalhes.html" class="btn-venda py-6 text-xl max-w-sm">ENTRAR NO SISTEMA</a>'

    return f"""<!DOCTYPE html>
    <html lang="pt-br"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{tema} | Nexus Alpha</title>{criar_estilo()}</head>
    <body><div class="bg-hero"></div><div class="max-w-5xl mx-auto px-6 py-20">
    <header class="flex justify-between items-center mb-16"><a href="index.html" class="text-2xl font-black italic no-underline text-white">NEXUS<span class="text-green-500">ALPHA</span></a><div class="text-[10px] opacity-40">INTELLIGENCE V.2026</div></header>
    {conteudo}{secao_rel}
    <footer class="mt-20 py-10 border-t border-white/10 text-[10px] opacity-40 text-center uppercase tracking-widest">
    <p>© 2026 Nexus Alpha System</p><div class="mt-4 flex justify-center gap-6 font-bold"><a href="privacidade.html" class="text-white no-underline hover:text-green-500">Privacidade</a><a href="termos.html" class="text-white no-underline hover:text-green-500">Termos de Uso</a></div></footer></div></body></html>"""

def criar_pagina_vendas(tema, link_stripe):
    link_final = "https://buy.stripe.com/9B6fZ976y7zJ6qn0jl4c80v"
    preco = "R$ 19,90"
    rel = [
        {"nome": "Score 900 Turbo", "preco": preco, "slug": "score", "link": link_final},
        {"nome": "Renda Extra", "preco": preco, "slug": "renda", "link": link_final},
        {"nome": "Planilha Lucros", "preco": preco, "slug": "planilha", "link": link_final}
    ]
    with open("index.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina(tema, preco, "detalhes.html"))
    with open("detalhes.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina(tema, preco, link_final, eh_detalhes=True, relacionados=rel))
    for p in rel:
        with open(f"{p['slug']}.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina(p['nome'], p['preco'], p['link'], eh_detalhes=True, relacionados=rel))
    with open("privacidade.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina("Privacidade", "", "", legal_type="privacidade"))
    with open("termos.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina("Termos", "", "", legal_type="termos"))
