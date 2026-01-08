import os

def criar_estilo():
    foto_unificada = "https://images.unsplash.com/photo-1551836022-d5d88e9218df?q=80&w=1600&auto=format&fit=crop"
    return f"""
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,800;1,800&family=Inter:wght@300;400;700&display=swap');
        body {{ font-family: 'Inter', sans-serif; background: #020617; color: #fff; margin: 0; }}
        .bg-hero {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, rgba(2, 6, 23, 0.85) 0%, rgba(2, 6, 23, 1) 100%), url('{foto_unificada}'); background-size: cover; background-position: center; z-index: -1; }}
        .titulo-master {{ font-family: 'Montserrat', sans-serif; font-weight: 800; letter-spacing: -0.05em; color: #39FF14; }}
        .glass {{ background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(25px); border-radius: 2rem; }}
        .btn-venda {{ background: #fff; color: #000; font-family: 'Montserrat', sans-serif; font-weight: 800; transition: 0.3s; display: block; width: 100%; text-align: center; }}
        .btn-venda:hover {{ transform: scale(1.05); box-shadow: 0 0 30px rgba(255, 255, 255, 0.4); }}
        .payment-container {{ margin-top: 25px; display: flex; flex-direction: column; align-items: center; gap: 10px; }}
        .logos-row {{ display: flex; justify-content: center; align-items: center; gap: 20px; font-size: 28px; }}
    </style>
    """

def obter_copy(tema):
    copys = {
        "Score 900 Turbo": "Protocolo para destravar seu crédito e elevar sua pontuação bancária rapidamente.",
        "Renda Extra": "Método validado para gerar ganhos diários usando apenas o celular.",
        "Planilha Lucros": "Ferramenta de IA para organizar finanças e projetar lucros reais.",
        "IA Automação": "O segredo para colocar processos digitais no piloto automático e lucrar dormindo.",
        "Copywriting Master": "A arte de escrever textos que vendem qualquer produto em segundos."
    }
    return copys.get(tema, "Protocolo de Alta Performance Nexus Alpha.")

def gerar_layout_pagina(tema, preco, link, eh_detalhes=False, relacionados=[]):
    copy_detalhada = obter_copy(tema)
    
    html_relacionados = ""
    for p in relacionados:
        html_relacionados += f'''
        <a href="{p['slug']}.html" class="glass p-8 block hover:bg-white/10 transition-all text-center">
            <h4 class="titulo-master text-lg mb-2 uppercase italic" style="color: #39FF14">{p['nome']}</h4>
            <p class="text-white font-bold text-2xl">{p['preco']}</p>
        </a>'''

    secao_relacionados = f"""
    <div class="mt-32 pt-16 border-t border-white/10">
        <h3 class="text-white titulo-master text-3xl mb-10 uppercase italic text-center">Produtos Relacionados</h3>
        <div class="grid md:grid-cols-3 gap-6">{html_relacionados}</div>
    </div>""" if eh_detalhes else ""

    # Pix Removido - Apenas Stripe Nativo
    logos_pagamento = """
    <div class="payment-container">
        <div class="logos-row">
            <i class="fab fa-cc-visa" style="color: #fff; opacity: 0.9;"></i>
            <i class="fab fa-cc-mastercard" style="color: #fff; opacity: 0.9;"></i>
            <i class="fab fa-apple-pay" style="color: #fff; opacity: 0.9;"></i>
            <i class="fas fa-barcode" style="color: #fff; opacity: 0.7;"></i>
        </div>
        <p class="text-[9px] opacity-40 uppercase tracking-widest text-center">Pagamento 100% Seguro via Stripe</p>
    </div>
    """

    conteudo_venda = f"""
    <div class="grid md:grid-cols-2 gap-12 mt-16">
        <div class="glass p-10">
            <h3 class="titulo-master text-2xl mb-6 uppercase italic">Protocolo {tema}:</h3>
            <p class="text-slate-300 leading-relaxed mb-6">{copy_detalhada}</p>
            <ul class="space-y-4 text-sm">
                <li><i class="fas fa-check-circle mr-2 text-green-500"></i> Entrega Digital via E-mail</li>
                <li><i class="fas fa-check-circle mr-2 text-green-500"></i> Metodologia Passo a Passo</li>
            </ul>
        </div>
        <div class="glass p-10 text-center flex flex-col justify-center">
            <span class="text-xs font-bold uppercase tracking-widest text-green-400 mb-2 italic">Oferta Nexus Alpha</span>
            <div class="text-white titulo-master text-7xl mb-8 tracking-tighter" style="color:white">{preco}</div>
            <a href="{link}" class="btn-venda py-6 rounded-2xl text-xl uppercase tracking-tighter shadow-lg">Adquirir Agora</a>
            {logos_pagamento}
        </div>
    </div>""" if eh_detalhes else ""

    return f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{tema} | Nexus Alpha</title>
        {criar_estilo()}
    </head>
    <body>
        <div class="bg-hero"></div>
        <div class="max-w-6xl mx-auto px-6 py-20">
            <header class="mb-12">
                <div class="bg-white/10 w-fit px-4 py-1 rounded-full text-[10px] font-bold text-green-400 mb-6">NEXUS AI SYSTEMS</div>
                <h1 class="titulo-master text-6xl md:text-[90px] uppercase italic mb-6">#{tema}</h1>
                {f'<a href="detalhes.html" class="btn-venda px-12 py-5 mt-10 inline-block rounded-full uppercase text-sm">Acessar Conteúdo</a>' if not eh_detalhes else ""}
            </header>
            {conteudo_venda}
            {secao_relacionados}
        </div>
    </body>
    </html>
    """

def criar_pagina_vendas(tema, link_stripe):
    link_venda = "https://buy.stripe.com/9B6fZ976y7zJ6qn0jl4c80v"
    preco_final = "R$ 19,90"
    
    # Base de Dados Dinâmica (Robô pode adicionar mais aqui)
    relacionados = [
        {"nome": "Score 900 Turbo", "preco": preco_final, "slug": "score", "link": link_venda},
        {"nome": "Renda Extra", "preco": preco_final, "slug": "renda", "link": link_venda},
        {"nome": "Planilha Lucros", "preco": preco_final, "slug": "planilha", "link": link_venda}
    ]

    with open("index.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina(tema, preco_final, "detalhes.html"))
    with open("detalhes.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina(tema, preco_final, link_venda, eh_detalhes=True, relacionados=relacionados))
    for p in relacionados:
        with open(f"{p['slug']}.html", "w", encoding="utf-8") as f:
            outros = [i for i in relacionados if i['slug'] != p['slug']]
            f.write(gerar_layout_pagina(p['nome'], p['preco'], p['link'], eh_detalhes=True, relacionados=outros))
