import os

def criar_estilo():
    foto_unificada = "https://images.unsplash.com/photo-1551836022-d5d88e9218df?q=80&w=1600&auto=format&fit=crop"
    return f"""
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,800;1,800&family=Inter:wght@300;400;700&display=swap');
        body {{ font-family: 'Inter', sans-serif; background: #020617; color: #fff; margin: 0; scroll-behavior: smooth; }}
        .bg-hero {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, rgba(2, 6, 23, 0.9) 0%, rgba(2, 6, 23, 1) 100%), url('{foto_unificada}'); background-size: cover; background-position: center; z-index: -1; }}
        .titulo-master {{ font-family: 'Montserrat', sans-serif; font-weight: 800; letter-spacing: -0.05em; color: #39FF14; text-transform: uppercase; font-style: italic; }}
        .glass {{ background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(25px); border-radius: 2rem; }}
        .btn-venda {{ background: #fff; color: #000; font-family: 'Montserrat', sans-serif; font-weight: 800; transition: 0.3s; display: block; width: 100%; text-align: center; border-radius: 1rem; border: none; cursor: pointer; }}
        .btn-venda:hover {{ transform: scale(1.05); box-shadow: 0 0 40px rgba(57, 255, 20, 0.4); }}
        .neon-border {{ border: 1px solid #39FF14; }}
        .conteudo-legal h2 {{ color: #39FF14; font-family: 'Montserrat', sans-serif; text-transform: uppercase; margin-top: 2rem; margin-bottom: 1rem; border-bottom: 1px solid rgba(57,255,20,0.2); }}
        .conteudo-legal p, .conteudo-legal li {{ margin-bottom: 1rem; opacity: 0.8; line-height: 1.8; text-align: justify; }}
        .check-list i {{ color: #39FF14; margin-right: 10px; }}
    </style>
    """

def obter_conteudo_privacidade():
    return """<h2>Política de Privacidade</h2><p>Conforme a LGPD brasileira, informamos que coletamos nome e e-mail para entrega do produto. Dados de pagamento são processados pelo Stripe.</p><ul><li>Direito de acesso e exclusão;</li><li>Segurança de dados criptografada;</li><li>Uso de cookies para análise de mercado (3-7s).</li></ul>"""

def obter_conteudo_termos():
    return """<h2>Termos de Uso</h2><p>Este contrato rege o uso da Nexus Alpha. Ao acessar, você aceita as responsabilidades de uso ético e respeita a propriedade intelectual do conteúdo.</p><ul><li>Garantia de 7 dias (CDC);</li><li>Entrega digital imediata;</li><li>Foro da Comarca Sede.</li></ul>"""

def obter_dados_produto(tema):
    dados = {
        "Score 900 Turbo": {
            "headline": "AUMENTE SEU SCORE PARA 900 PONTOS EM TEMPO RECORDE",
            "desc": "O guia definitivo para destravar seu crédito bancário e ser aprovado em qualquer banco.",
            "mods": ["Módulo 1: O Segredo dos Bancos", "Módulo 2: Limpeza de Consultas", "Módulo 3: Gatilhos de Aprovação"],
            "benefs": "Aprovação de limites altos e juros baixos.",
            "faq": "É seguro? Sim. Quanto tempo? 7 a 15 dias."
        },
        "Renda Extra": {
            "headline": "TRANSFORME SEU CELULAR EM UMA MÁQUINA DE DINHEIRO",
            "desc": "Métodos de arbitragem digital para faturar diariamente.",
            "mods": ["Módulo 1: Configuração", "Módulo 2: Tarefas Digitais", "Módulo 3: Saques"],
            "benefs": "Trabalhe de casa e ganhe em escala.",
            "faq": "Precisa investir? Não. Funciona no Android? Sim."
        },
        "Planilha Lucros": {
            "headline": "DOMINE SUAS FINANÇAS COM INTELIGÊNCIA ARTIFICIAL",
            "desc": "A ferramenta de projeção de lucros automática.",
            "mods": ["Módulo 1: Fluxo de Caixa", "Módulo 2: Projeção IA", "Módulo 3: Dashboard"],
            "benefs": "Clareza total e multiplicação de patrimônio.",
            "faq": "Precisa saber Excel? Não, é automática."
        }
    }
    return dados.get(tema, dados["Score 900 Turbo"])

def gerar_layout_pagina(tema, preco, link, eh_detalhes=False, relacionados=[], legal_type=None):
    info = obter_dados_produto(tema)
    html_relacionados = ""
    if relacionados:
        for p in relacionados:
            html_relacionados += f'''<a href="{p['slug']}.html" class="glass p-6 block hover:bg-white/10 text-center">
                <h4 class="titulo-master text-xs mb-1">{p['nome']}</h4>
                <p class="font-bold">{p['preco']}</p></a>'''

    secao_relacionados = f"""<div class="mt-20 pt-10 border-t border-white/10"><h3 class="titulo-master text-center mb-6">Produtos Relacionados</h3><div class="grid grid-cols-1 md:grid-cols-3 gap-4">{html_relacionados}</div></div>""" if relacionados else ""

    conteudo = ""
    if legal_type:
        txt = obter_conteudo_privacidade() if legal_type == "privacidade" else obter_conteudo_termos()
        conteudo = f'<div class="glass p-10 conteudo-legal">{txt}</div>'
    elif eh_detalhes:
        conteudo = f"""
        <div class="text-center mb-10"><h1 class="titulo-master text-4xl md:text-6xl mb-6 italic">{info['headline']}</h1></div>
        <div class="grid md:grid-cols-2 gap-8 mb-10">
            <div class="glass p-8"><h3 class="titulo-master mb-4">Módulos:</h3><ul class="check-list">{" ".join([f"<li><i class='fas fa-check'></i>{m}</li>" for m in info['mods']])}</ul></div>
            <div class="glass p-8"><h3 class="titulo-master mb-4">Benefícios:</h3><p>{info['benefs']}</p></div>
        </div>
        <div class="glass p-10 text-center neon-border mb-10">
            <div class="titulo-master text-7xl mb-6">{preco}</div>
            <a href="{link}" class="btn-venda py-6 text-xl uppercase">COMPRAR AGORA</a>
            <div class="flex justify-center gap-4 mt-4 opacity-50"><i class="fab fa-cc-visa"></i><i class="fab fa-cc-mastercard"></i><i class="fab fa-apple-pay"></i><i class="fas fa-barcode"></i></div>
            <p class="mt-4 text-xs font-bold text-green-400"><i class="fas fa-shield-alt"></i> 7 DIAS DE GARANTIA INCONDICIONAL</p>
        </div>
        <div class="glass p-8 text-center mb-10"><h3 class="titulo-master mb-4 italic">FAQ:</h3><p>{info['faq']}</p></div>
        <p class="text-center opacity-50 text-xs">Suporte: suporte@nexusalpha.com</p>
        """
    else:
        conteudo = f'<h1 class="titulo-master text-7xl md:text-9xl mb-12 italic">#{tema}</h1><a href="detalhes.html" class="btn-venda py-6 text-xl max-w-sm">ENTRAR NO SISTEMA</a>'

    return f"""<!DOCTYPE html>
    <html lang="pt-br"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{tema} | Nexus Alpha</title>{criar_estilo()}</head>
    <body><div class="bg-hero"></div><div class="max-w-5xl mx-auto px-6 py-20">
    <header class="flex justify-between items-center mb-10"><a href="index.html" class="text-2xl font-black italic tracking-tighter">NEXUS<span class="text-green-500">ALPHA</span></a><div class="text-[8px] opacity-40">INTELLIGENCE V.2026</div></header>
    {conteudo}{secao_relacionados}
    <footer class="mt-20 py-10 border-t border-white/10 text-[10px] opacity-40 text-center uppercase tracking-widest">
    <p>© 2026 Nexus Alpha System</p><div class="mt-4 flex justify-center gap-4"><a href="privacidade.html">Privacidade</a><a href="termos.html">Termos</a></div></footer></div></body></html>"""

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
