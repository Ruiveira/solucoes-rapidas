def criar_pagina_vendas(tema, link_stripe):
    # PÁGINA DE ENTRADA: O IMPACTO VISUAL
    html_home = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{tema} | Excelência</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body {{ background-color: #000; color: #fff; }}
            .hero-gradient {{ background: radial-gradient(circle at center, #1e1b4b 0%, #000 70%); }}
        </style>
    </head>
    <body class="hero-gradient min-h-screen flex items-center justify-center font-serif">
        <div class="text-center px-6 animate-fade-in">
            <h2 class="text-indigo-500 tracking-[0.5em] text-xs font-bold mb-8 uppercase">Intelligence & Power</h2>
            <h1 class="text-5xl md:text-8xl font-light tracking-tighter mb-12 italic uppercase">{tema}</h1>
            <a href="detalhes.html" class="group relative inline-flex items-center gap-4 px-12 py-6 border border-white/20 rounded-full hover:bg-white hover:text-black transition-all duration-700">
                <span class="text-sm font-bold tracking-widest uppercase">Saiba Mais</span>
                <span class="text-xl transform group-hover:translate-x-2 transition-transform">→</span>
            </a>
        </div>
    </body>
    </html>
    """

    # PÁGINA DE CONVENCIMENTO: O ENCANTAMENTO
    html_detalhes = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>A Experiência - {tema}</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-white text-black font-sans selection:bg-indigo-100">
        <section class="py-24 px-8 max-w-6xl mx-auto">
            <div class="grid md:grid-cols-2 gap-24 items-center">
                <div>
                    <span class="text-indigo-600 font-bold tracking-tighter text-sm uppercase">O Próximo Nível</span>
                    <h1 class="text-6xl font-black mt-4 mb-8 leading-[0.9] italic uppercase">{tema}</h1>
                    <p class="text-2xl text-slate-600 leading-relaxed mb-12">
                        Não vendemos informação. Entregamos a chave para a <span class="text-black font-bold">transcendência</span> da sua realidade atual. Sinta o poder da maestria em suas mãos.
                    </p>
                    
                    <div class="space-y-8 mb-12">
                        <div class="flex gap-4">
                            <span class="text-indigo-600 font-bold text-xl">01</span>
                            <p class="text-slate-500 italic">Metodologia exclusiva desenvolvida por algoritmos de alta performance.</p>
                        </div>
                        <div class="flex gap-4">
                            <span class="text-indigo-600 font-bold text-xl">02</span>
                            <p class="text-slate-500 italic">Suporte de inteligência ativa para implementação imediata.</p>
                        </div>
                    </div>

                    <a href="{link_stripe}" class="inline-block w-full bg-black text-white text-center py-8 rounded-full font-black text-xl hover:bg-indigo-700 transition-all shadow-2xl">
                        ADQUIRIR AGORA
                    </a>
                </div>
                <div class="relative">
                    <div class="aspect-[3/4] bg-slate-100 rounded-[4rem] overflow-hidden border border-slate-200 flex items-center justify-center p-12">
                        <div class="text-center">
                            <p class="text-slate-300 text-[10rem] font-black italic opacity-20 uppercase leading-none">NEXUS</p>
                        </div>
                    </div>
                    <div class="absolute -bottom-10 -left-10 bg-white p-8 rounded-3xl shadow-2xl border border-slate-100">
                        <p class="text-4xl font-black text-indigo-600 italic leading-none">100%</p>
                        <p class="text-xs font-bold uppercase tracking-widest mt-2">Seguro & Vitalício</p>
                    </div>
                </div>
            </div>
        </section>
        
        <footer class="py-20 bg-slate-50 text-center">
             <p class="text-slate-400 text-sm uppercase tracking-widest font-bold">Referência em Soluções Rápidas &copy; 2026</p>
        </footer>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f: f.write(html_home)
    with open("detalhes.html", "w", encoding="utf-8") as f: f.write(html_detalhes)
