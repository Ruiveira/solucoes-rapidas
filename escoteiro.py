import os

def criar_estilo():
    return """
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,900;1,900&family=Inter:wght@300;400;700&display=swap');
        body { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
        .font-luxury { font-family: 'Playfair Display', serif; }
        .glass { background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); }
        .gradient-text { background: linear-gradient(to right, #fff, #6366f1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .btn-gold { background: #fff; color: #000; transition: all 0.5s cubic-bezier(0.19, 1, 0.22, 1); }
        .btn-gold:hover { transform: scale(1.05); letter-spacing: 2px; box-shadow: 0 0 30px rgba(255,255,255,0.2); }
    </style>
    """

def gerar_layout_pagina(tema, preco, link, outros_produtos=[], eh_principal=True):
    # O Robô gera o conteúdo com base no tema para "Encantar"
    html = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{tema} | L'Excellence</title>
        {criar_estilo()}
    </head>
    <body class="antialiased overflow-x-hidden">
        <section class="min-h-screen flex flex-col items-center justify-center px-6 relative">
            <div class="absolute top-0 left-0 w-full h-full bg-[radial-gradient(circle_at_50%_50%,_rgba(67,56,202,0.15),_transparent)] pointer-events-none"></div>
            
            <span class="text-indigo-500 font-bold tracking-[0.4em] text-[10px] uppercase mb-6">A Nova Era da Maestria</span>
            <h1 class="text-6xl md:text-[120px] font-luxury italic leading-none mb-12 text-center gradient-text uppercase">{tema}</h1>
            
            <p class="max-w-2xl text-center text-slate-400 text-lg md:text-xl font-light leading-relaxed mb-16">
                Não é apenas um produto. É o portal para uma nova realidade. Desenhado para quem não aceita o comum e busca o <span class="text-white font-bold italic">poder absoluto</span> sobre os resultados.
            </p>

            <a href="#checkout" class="btn-gold px-16 py-6 rounded-full font-black text-sm tracking-widest uppercase">Explorar Detalhes</a>
        </section>

        <section id="checkout" class="py-32 px-6 max-w-7xl mx-auto">
            <div class="grid lg:grid-cols-2 gap-24">
                <div class="space-y-12">
                    <h2 class="text-4xl font-luxury italic uppercase tracking-tighter">O que torna isso <br> <span class="text-indigo-500">Inesquecível?</span></h2>
                    <div class="space-y-8 text-slate-400">
                        <div class="flex gap-6 pb-8 border-b border-white/10">
                            <span class="text-2xl">✧</span>
                            <p><strong class="text-white">Conhecimento Hermético:</strong> Estratégias que 99% do mercado desconhece.</p>
                        </div>
                        <div class="flex gap-6 pb-8 border-b border-white/10">
                            <span class="text-2xl">✧</span>
                            <p><strong class="text-white">Implementação Imediata:</strong> Do desejo à ação em menos de 24 horas.</p>
                        </div>
                    </div>
                </div>

                <div class="glass p-12 rounded-[4rem] text-center flex flex-col justify-center sticky top-10">
                    <h3 class="text-sm font-bold tracking-widest uppercase mb-4 text-indigo-400">Investimento Único</h3>
                    <div class="text-7xl font-luxury italic mb-10">{preco}</div>
                    <a href="{link}" class="btn-gold w-full py-8 rounded-3xl font-black text-xl mb-8">ADQUIRIR AGORA</a>
                    <div class="flex justify-center gap-6 opacity-30">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/b/b0/Apple_Pay_logo.svg" class="h-5 invert">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/Visa_Inc._logo.svg" class="h-4 invert">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/d/d6/Boleto_logo.svg" class="h-6 invert">
                    </div>
                </div>
            </div>
        </section>

        <section class="py-32 bg-white/5">
            <div class="max-w-7xl mx-auto px-6">
                <h2 class="text-center font-luxury italic text-3xl mb-16 italic">Complete sua Coleção</h2>
                <div class="grid md:grid-cols-3 gap-10">
                    {" ".join([f'''
                    <a href="{p['slug']}.html" class="glass p-10 rounded-[3rem] group hover:bg-white hover:text-black transition-all duration-500">
                        <p class="text-[10px] font-bold uppercase tracking-widest mb-4 opacity-50">Próximo Passo</p>
                        <h4 class="text-xl font-luxury mb-4 uppercase">{p['nome']}</h4>
                        <p class="font-bold text-indigo-500 group-hover:text-black">{p['preco']}</p>
                    </a>
                    ''' for p in outros_produtos])}
                </div>
            </div>
        </section>
    </body>
    </html>
    """
    return html

def criar_pagina_vendas(tema, link_stripe):
    # O Robô define preços autônomos baseados na complexidade do tema
    preco_principal = "R$ 197,00" if "Investimento" in tema else "R$ 97,00"
    
    produtos_relacionados = [
        {"nome": "O Segredo do Score 900", "preco": "R$ 47,00", "slug": "score", "link": link_stripe},
        {"nome": "Renda Extra Online", "preco": "R$ 67,00", "slug": "renda", "link": link_stripe},
        {"nome": "Planilha de Lucros", "preco": "R$ 27,00", "slug": "planilha", "link": link_stripe}
    ]

    # Salva a página principal e as relacionadas
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(gerar_layout_pagina(tema, preco_principal, "detalhes.html"))
    
    with open("detalhes.html", "w", encoding="utf-8") as f:
        f.write(gerar_layout_pagina(tema, preco_principal, link_stripe, produtos_relacionados))

    # Cria as páginas dos relacionados automaticamente
    for p in produtos_relacionados:
        with open(f"{p['slug']}.html", "w", encoding="utf-8") as f:
            f.write(gerar_layout_pagina(p['nome'], p['preco'], p['link'], eh_principal=False))
