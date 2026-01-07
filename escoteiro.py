def criar_estilo():
    return """
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,700&family=Inter:wght@300;400;600;800&display=swap');
        body { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; scroll-behavior: smooth; }
        .font-luxury { font-family: 'Playfair Display', serif; }
        .gradient-text { 
            background: linear-gradient(to right, #ffffff, #a5b4fc); 
            background-clip: text; -webkit-background-clip: text; 
            -webkit-text-fill-color: transparent; color: transparent;
        }
        .glass { background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.08); backdrop-filter: blur(20px); }
        .btn-action { background: #ffffff; color: #000; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
        .btn-action:hover { transform: scale(1.05); box-shadow: 0 20px 40px rgba(99, 102, 241, 0.3); }
        .card-relacionado { transition: all 0.3s ease; }
        .card-relacionado:hover { background: rgba(255, 255, 255, 0.05); border-color: rgba(99, 102, 241, 0.5); }
    </style>
    """

def gerar_layout_pagina(tema, preco, link, eh_detalhes=False, relacionados=[]):
    # Conteúdo Didático e Persuasivo Exclusivo por Tema
    intro_didatica = f"""
    O método <strong>{tema}</strong> foi desenvolvido para quem busca clareza absoluta e resultados imediatos. 
    Diferente de tudo o que você já viu, aqui nós removemos a complexidade e entregamos um mapa mental e prático 
    capaz de transformar {tema} em uma vantagem competitiva real na sua vida. Imagine dominar cada detalhe 
    com a confiança de um especialista, eliminando erros comuns e acelerando seu progresso em tempo recorde.
    """

    conteudo_detalhes = ""
    if eh_detalhes:
        conteudo_detalhes = f"""
        <div class="mt-24 grid md:grid-cols-2 gap-16 text-left border-t border-white/10 pt-16">
            <div>
                <h3 class="font-luxury italic text-4xl mb-8 gradient-text uppercase">O Que Você Vai Descobrir</h3>
                <div class="space-y-8 text-slate-300 text-lg leading-relaxed">
                    <p><i class="fas fa-check-circle text-indigo-500 mr-3"></i> <strong>A Estrutura Mestra:</strong> Entenda os pilares fundamentais que sustentam o sucesso em {tema}.</p>
                    <p><i class="fas fa-check-circle text-indigo-500 mr-3"></i> <strong>Aceleração de Resultados:</strong> Técnicas validadas para reduzir meses de aprendizado em poucos dias.</p>
                    <p><i class="fas fa-check-circle text-indigo-500 mr-3"></i> <strong>Blindagem Estratégica:</strong> Como manter seus ganhos e evoluir de forma consistente e segura.</p>
                </div>
            </div>
            <div class="glass p-10 rounded-[3rem] border-indigo-500/20">
                <h4 class="font-black text-indigo-400 uppercase text-xs tracking-[0.3em] mb-6">Conteúdo Premium Incluso</h4>
                <ul class="space-y-4 text-slate-300">
                    <li class="flex items-center gap-3"><i class="fas fa-video text-indigo-500"></i> Videoaulas Didáticas Passo a Passo</li>
                    <li class="flex items-center gap-3"><i class="fas fa-file-pdf text-indigo-500"></i> Guia Prático de Implementação</li>
                    <li class="flex items-center gap-3"><i class="fas fa-chart-line text-indigo-500"></i> Planilha de Acompanhamento Real</li>
                    <li class="flex items-center gap-3"><i class="fas fa-certificate text-indigo-500"></i> Certificado de Maestria Nexus-Alpha</li>
                </ul>
            </div>
        </div>
        """

    # Ícones de Pagamento de Alta Definição (FontAwesome)
    icones_pagamento = """
    <div class="flex justify-center items-center gap-8 mt-10 text-white/60 text-2xl">
        <i class="fab fa-apple-pay hover:text-white transition-colors" title="Apple Pay"></i>
        <i class="fab fa-cc-visa hover:text-white transition-colors" title="Cartão de Crédito"></i>
        <i class="fab fa-cc-mastercard hover:text-white transition-colors" title="Cartão de Crédito"></i>
        <i class="fas fa-barcode hover:text-white transition-colors text-xl" title="Boleto"></i>
    </div>
    """

    return f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{tema} | Inteligência e Vantagem</title>
        {criar_estilo()}
    </head>
    <body class="antialiased">
        <div class="max-w-6xl mx-auto px-6 py-20 text-center">
            <span class="text-indigo-500 font-bold tracking-[0.5em] text-xs uppercase mb-6 block">Documento Oficial & Exclusivo</span>
            <h1 class="text-5xl md:text-8xl font-luxury italic gradient-text uppercase mb-12 leading-none tracking-tighter">{tema}</h1>
            
            <div class="max-w-3xl mx-auto text-slate-400 text-xl mb-16 leading-relaxed italic">
                {intro_didatica}
            </div>

            <div class="glass p-12 md:p-20 rounded-[4rem] max-w-2xl mx-auto mb-20 shadow-2xl shadow-indigo-500/10">
                <p class="text-indigo-400 text-sm font-bold uppercase tracking-[0.2em] mb-4">Investimento Único para Acesso Vitalício</p>
                <div class="text-7xl font-luxury italic mb-10 tracking-tighter">{preco}</div>
                <a href="{link}" class="btn-action block w-full py-8 rounded-3xl font-black text-2xl uppercase tracking-widest shadow-xl">
                    { "OBTER ACESSO IMEDIATO" if eh_detalhes else "SAIBA MAIS AGORA" }
                </a>
                {icones_pagamento}
                <p class="mt-8 text-xs text-slate-500 uppercase font-bold tracking-widest">Pagamento Criptografado e Seguro</p>
            </div>

            {conteudo_detalhes}

            { f'<div class="mt-40 pt-20 border-t border-white/10"><h3 class="font-luxury italic text-3xl mb-12 uppercase tracking-widest">Ecossistema de Soluções</h3><div class="grid md:grid-cols-3 gap-8">{" ".join([f"<a href=\'{p['slug']}.html\' class=\'card-relacionado glass p-10 rounded-[3rem] block\'><h4 class=\'font-luxury italic text-xl mb-4 uppercase\'>{p['nome']}</h4><p class=\'text-indigo-400 font-black text-2xl mb-2\'>{p['preco']}</p><span class=\'text-[10px] uppercase font-bold text-slate-500 tracking-widest\'>Explorar Conteúdo →</span></a>" for p in relacionados])}</div></div>' if eh_detalhes else "" }
        </div>
        <footer class="py-20 text-slate-600 text-[10px] uppercase tracking-[0.4em]">Nexus-Alpha &copy; 2026 - Todos os Direitos Reservados</footer>
    </body>
    </html>
    """

def criar_pagina_vendas(tema, link_stripe):
    preco_fixo = "R$ 10,00"
    relacionados = [
        {"nome": "O Segredo do Score 900", "preco": preco_fixo, "slug": "score", "link": link_stripe},
        {"nome": "Renda Extra Online", "preco": preco_fixo, "slug": "renda", "link": link_stripe},
        {"nome": "Planilha de Lucros", "preco": preco_fixo, "slug": "planilha", "link": link_stripe}
    ]

    # Home Principal
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(gerar_layout_pagina(tema, preco_fixo, "detalhes.html", eh_detalhes=False))
    
    # Detalhes do Produto Principal
    with open("detalhes.html", "w", encoding="utf-8") as f:
        f.write(gerar_layout_pagina(tema, preco_fixo, link_stripe, eh_detalhes=True, relacionados=relacionados))

    # Criação das Páginas Relacionadas (Dando vida ao ecossistema)
    for p in relacionados:
        with open(f"{p['slug']}.html", "w", encoding="utf-8") as f:
            # Cada página relacionada também mostra os outros produtos para circular o tráfego
            outros = [i for i in relacionados if i['slug'] != p['slug']]
            f.write(gerar_layout_pagina(p['nome'], p['preco'], p['link'], eh_detalhes=True, relacionados=outros))
