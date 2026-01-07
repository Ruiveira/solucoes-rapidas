def criar_pagina_vendas(tema, link_stripe):
    # PÁGINA 1: A ISCA (Inspirada na entrada da FAAP)
    html_home = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{tema} - Oficial</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-[#0f172a] text-white font-sans antialiased">
        <div class="max-w-xl mx-auto px-6 py-24 text-center">
            <div class="inline-flex items-center gap-2 bg-indigo-500/10 border border-indigo-500/20 px-4 py-2 rounded-full mb-8">
                <span class="text-indigo-400 text-xs font-bold uppercase tracking-widest">Lançamento Exclusivo 2026</span>
            </div>
            <h1 class="text-4xl md:text-6xl font-black mb-6 leading-tight uppercase italic italic">
                {tema}
            </h1>
            <p class="text-slate-400 text-lg mb-10 leading-relaxed">
                Aprimore seu olhar estratégico e criativo para se destacar em um mercado em constante evolução.
            </p>
            <a href="detalhes.html" class="inline-block w-full bg-white text-black font-black py-6 rounded-2xl text-xl hover:bg-slate-200 transition-all uppercase">
                SAIBA MAIS
            </a>
        </div>
    </body>
    </html>
    """

    # PÁGINA 2: O CONVENCIMENTO (Inspirada no LP da FAAP)
    html_detalhes = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Detalhes: {tema}</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-white text-slate-900 font-sans antialiased">
        <header class="bg-[#0f172a] py-12 px-6 text-center text-white">
            <h2 class="text-sm font-bold uppercase tracking-[0.3em] mb-4 text-indigo-400 italic">Estratégia para se Destacar</h2>
            <h1 class="text-4xl md:text-5xl font-black mb-6 italic italic uppercase leading-none">{tema}</h1>
            <p class="text-slate-400 max-w-lg mx-auto">Lidere com clareza e estratégia. Construa resultados de verdade.</p>
        </header>

        <main class="max-w-2xl mx-auto px-6 py-16">
            <div class="grid grid-cols-1 gap-12 mb-16">
                <div class="border-l-4 border-indigo-600 pl-6">
                    <h3 class="font-black text-xl mb-2 italic">Acesso 100% Digital</h3>
                    <p class="text-slate-500">Aprenda no seu ritmo, de onde você estiver, com conteúdo atualizado.</p>
                </div>
                <div class="border-l-4 border-indigo-600 pl-6">
                    <h3 class="font-black text-xl mb-2 italic">Certificado Reconhecido</h3>
                    <p class="text-slate-500">Valorize seu currículo com uma metodologia de alto nível.</p>
                </div>
            </div>

            <div class="bg-slate-100 p-10 rounded-[3rem] text-center border-2 border-slate-200">
                <p class="text-indigo-600 font-bold mb-2 uppercase tracking-widest text-sm">Oferta por tempo limitado</p>
                <h4 class="text-3xl font-black mb-8 italic">Garanta sua vaga com condições exclusivas</h4>
                <a href="{link_stripe}" class="inline-block w-full bg-indigo-600 text-white font-black py-6 rounded-2xl text-xl hover:bg-indigo-700 transition-all uppercase shadow-xl shadow-indigo-200">
                    ADQUIRIR AGORA
                </a>
            </div>
        </main>
    </body>
    </html>
    """

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_home)
    with open("detalhes.html", "w", encoding="utf-8") as f:
        f.write(html_detalhes)
