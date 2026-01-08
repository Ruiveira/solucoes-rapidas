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
        .check-list li {{ margin-bottom: 12px; display: flex; align-items: start; gap: 10px; opacity: 0.9; }}
        .check-list i {{ color: #39FF14; margin-top: 4px; }}
        .faq-box {{ border-bottom: 1px solid rgba(255,255,255,0.1); padding: 15px 0; }}
        .conteudo-legal h2 {{ color: #39FF14; font-family: 'Montserrat', sans-serif; text-transform: uppercase; margin-top: 2rem; }}
    </style>
    """

def obter_dados_copy(tema):
    biblioteca = {
        "Score 900 Turbo": {
            "headline": "AUMENTE SEU SCORE PARA 900 PONTOS E LIBERE CRÉDITO IMEDIATO",
            "desc": "O passo a passo detalhado para sair do zero e dominar o sistema bancário brasileiro.",
            "beneficio": "Tenha em mãos o poder de aprovar qualquer financiamento, cartão ou empréstimo com as menores taxas.",
            "modulos": ["Módulo 1: O Código Secreto dos Bancos", "Módulo 2: Blindagem de Perfil", "Módulo 3: O Gatilho da Pontuação Máxima"],
            "faq": "Quanto tempo demora? De 7 a 21 dias. É legal? Sim, usamos as regras do próprio sistema a seu favor."
        },
        "Renda Extra": {
            "headline": "TRANSFORME SEU CELULAR EM UMA FONTE DE LUCRO DIÁRIO NO PILOTO AUTOMÁTICO",
            "desc": "Métodos validados de arbitragem e micro-vendas digitais que geram receita 24h por dia.",
            "beneficio": "Liberdade de tempo e local. Ganhe dinheiro enquanto dorme com automações inteligentes.",
            "modulos": ["Módulo 1: Configuração do Robô de Vendas", "Módulo 2: Escala de Ganhos", "Módulo 3: Saques Instantâneos"],
            "faq": "Preciso investir? Não, apenas seguir o método. É garantido? Sim, se seguir o passo a passo."
        },
        "Planilha Lucros": {
            "headline": "A FERRAMENTA DE IA QUE PROJETA SEUS LUCROS E ESTANCA SUAS PERDAS",
            "desc": "Assuma o controle total da sua vida financeira com a dashboard usada por investidores de elite.",
            "beneficio": "Saiba exatamente para onde vai cada centavo e multiplique seu patrimônio com previsibilidade.",
            "modulos": ["Módulo 1: Mapeamento de Gastos Invisíveis", "Módulo 2: Projeção de Riqueza", "Módulo 3: Dashboard de Investimentos"],
            "faq": "É difícil usar? Não, é 100% automatizada. Funciona no celular? Sim, perfeitamente."
        }
    }
    return biblioteca.get(tema, biblioteca["Score 900 Turbo"])

def gerar_layout_pagina(tema, preco, link, eh_detalhes=False, relacionados=[], legal_type=None):
    copy = obter_dados_copy(tema)
    
    html_relacionados = ""
    if relacionados:
        for p in relacionados:
            html_relacionados += f'''
            <a href="{p['slug']}.html" class="glass p-6 block hover:bg-white/10 text-center border border-white/5">
                <h4 class="titulo-master text-xs mb-1 italic" style="color: #39FF14">{p['nome']}</h4>
                <p class="font-bold">{p['preco']}</p>
            </a>'''

    secao_relacionados = f"""<div class="mt-20 pt-10 border-t border-white/10"><h3 class="titulo-master text-center text-xl mb-10">Outras Oportunidades</h3><div class="grid grid-cols-1 md:grid-cols-3 gap-6">{html_relacionados}</div></div>""" if relacionados else ""

    conteudo = ""
    if legal_type:
        # Páginas de Política e Termos (Conteúdo simplificado para o exemplo, mas mantendo a estrutura)
        conteudo = f'<div class="glass p-10 conteudo-legal"><h1 class="titulo-master text-3xl mb-10 italic">#{tema}</h1><p>Conteúdo em conformidade com a LGPD e CDC.</p></div>'
    elif eh_detalhes:
        conteudo = f"""
        <div class="text-center mb-16">
            <h1 class="titulo-master text-4xl md:text-7xl mb-6 italic leading-tight">{copy['headline']}</h1>
            <p class="text-xl text-slate-400 max-w-3xl mx-auto">{copy['desc']}</p>
        </div>

        <div class="grid md:grid-cols-2 gap-10 mb-20 items-center">
            <div class="glass p-4 neon-border">
                <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=600" class="rounded-xl w-full">
            </div>
            <div class="glass p-10 text-center">
                <span class="bg-green-500 text-black px-4 py-1 rounded-full font-bold text-[10px] uppercase mb-4 inline-block italic">Oferta Exclusiva</span>
                <div class="titulo-master text-7xl my-6">{preco}</div>
                <a href="{link}" class="btn-venda py-8 text-2xl uppercase tracking-tighter">ADQUIRIR AGORA</a>
                <div class="flex justify-center gap-6 mt-6 text-2xl opacity-50">
                    <i class="fab fa-cc-visa"></i> <i class="fab fa-cc-mastercard"></i> <i class="fab fa-apple-pay"></i> <i class="fas fa-barcode"></i>
                </div>
                <p class="mt-8 text-xs font-bold text-green-400 uppercase italic"><i class="fas fa-shield-alt mr-2"></i> 7 Dias de Garantia Incondicional</p>
            </div>
        </div>

        <div class="grid md:grid-cols-2 gap-10 mb-20">
            <div class="glass p-10">
                <h3 class="titulo-master text-2xl mb-6 italic">O que você recebe:</h3>
                <ul class="check-list">
                    {" ".join([f"<li><i class='fas fa-check-circle'></i>{m}</li>" for m in copy['modulos']])}
                    <li><i class='fas fa-check-circle'></i>Materiais Complementares e Suporte VIP</li>
                </ul>
            </div>
            <div class="glass p-10">
                <h3 class="titulo-master text-2xl mb-6 italic">Seus Resultados:</h3>
                <p class="text-slate-300 leading-relaxed text-lg">{copy['beneficio']}</p>
            </div>
        </div>

        <div class="glass p-10 text-center mb-20">
            <h3 class="titulo-master text-2xl mb-10 italic">Depoimentos de Sucesso</h3>
            <div class="grid md:grid-cols-2 gap-8 italic text-slate-400">
                <div class="bg-white/5 p-6 rounded-2xl">"O Score Turbo realmente funciona! Em 15 dias meu crédito foi aprovado."<br><br><strong>- Ricardo M.</strong></div>
                <div class="bg-white/5 p-6 rounded-2xl">"A planilha me deu uma clareza que eu nunca tive. Recomendo a todos."<br><br><strong>- Amanda S.</strong></div>
            </div>
        </div>

        <div class="glass p-10 mb-10">
            <h3 class="titulo-master text-2xl mb-8 italic text-center">Perguntas Frequentes</h3>
            <div class="faq-box"><p class="font-bold">Como recebo o acesso?</p><p class="text-sm opacity-70">Imediatamente após a confirmação do pagamento no seu e-mail.</p></div>
            <div class="faq-box"><p class="font-bold">E se eu não gostar?</p><p class="text-sm opacity-70">{copy['faq']}</p></div>
        </div>

        <div class="text-center opacity-50 text-xs">
            <p>Dúvidas? <a href="mailto:suporte@nexusalpha.com" class="underline">suporte@nexusalpha.com</a></p>
        </div>
        """
    else:
        conteudo = f'<h1 class="titulo-master text-7xl md:text-9xl mb-12 italic">#{tema}</h1><a href="detalhes.html" class="btn-venda py-6 text-xl max-w-sm">ENTRAR NO SISTEMA</a>'

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
        <div class="max-w-5xl mx-auto px-6 py-20">
            <header class="flex justify-between items-center mb-16">
                <a href="index.html" class="text-2xl font-black italic tracking-tighter">NEXUS<span class="text-green-500">ALPHA</span></a>
                <div class="text-[9px] font-bold uppercase tracking-widest opacity-40">AI Scraper v.2026</div>
            </header>
            {conteudo}{secao_relacionados}
            <footer class="mt-32 py-10 border-t border-white/10 text-[10px] opacity-40 text-center uppercase tracking-widest">
                <p>© 2026 Nexus Alpha System - Brasil</p>
                <div class="mt-4 flex justify-center gap-6"><a href="privacidade.html" class="hover:text-green-500">Privacidade</a><a href="termos.html" class="hover:text-green-500">Termos</a></div>
            </footer>
        </div>
    </body>
    </html>
    """

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
