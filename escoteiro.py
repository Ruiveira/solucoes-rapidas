def criar_pagina_vendas(tema, link_stripe):
    # Simulação de outros produtos para o Cross-Sell (Aumento de Ticket)
    outros_produtos = [
        {"nome": "Mentoria VIP: Liberdade Financeira", "preco": "R$ 197,00"},
        {"nome": "Planilha Automática de Lucros", "preco": "R$ 47,00"},
        {"nome": "Acesso à Comunidade Nexus", "preco": "R$ 97,00"}
    ]

    # PÁGINA 1: A ISCA (Index) continua minimalista e impactante
    html_home = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{tema}</title><script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-black text-white flex items-center justify-center min-h-screen">
        <div class="text-center px-4">
            <h1 class="text-6xl font-black italic uppercase mb-8">{tema}</h1>
            <a href="detalhes.html" class="px-12 py-5 border border-white font-bold uppercase hover:bg-white hover:text-black transition-all">SAIBA MAIS</a>
        </div>
    </body>
    </html>
    """

    # PÁGINA 2: O ENCANTAMENTO (Detalhes) - Arquitetura de Conversão Total
    html_detalhes = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Oferta Exclusiva: {tema}</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-white text-slate-900 font-sans selection:bg-indigo-100">
        <div class="bg-slate-50 border-b border-slate-200 py-16 px-6">
            <div class="max-w-5xl mx-auto grid md:grid-cols-2 gap-12 items-center">
                <div>
                    <h1 class="text-5xl font-black leading-none mb-6 italic uppercase">{tema}</h1>
                    <p class="text-xl text-slate-600 mb-8 italic">O guia definitivo para transformar sua realidade através da maestria em {tema}.</p>
                    <div class="flex items-center gap-4 text-sm font-bold text-indigo-600 uppercase tracking-widest">
                        <span>Apple Pay</span> • <span>Cartão</span> • <span>Boleto</span>
                    </div>
                </div>
                <div class="rounded-3xl shadow-2xl overflow-hidden border-8 border-white">
                    <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80&w=800" alt="Dashboard de Sucesso" class="w-full">
                </div>
            </div>
        </div>

        <main class="max-w-5xl mx-auto px-6 py-20">
            <div class="grid md:grid-cols-3 gap-16">
                <div class="md:col-span-2">
                    <h2 class="text-3xl font-black mb-6 uppercase italic border-b-4 border-indigo-600 inline-block">O que você vai dominar</h2>
                    <p class="text-lg text-slate-600 mb-10 leading-relaxed">Este material foi estruturado para ser sua arma definitiva. Não é apenas teoria; é o passo a passo prático para resolver {tema} de uma vez por todas.</p>
                    
                    <div class="space-y-6">
                        <div class="p-6 bg-slate-50 rounded-2xl flex gap-6 items-start">
                            <span class="bg-white p-3 rounded-full shadow-sm text-xl">📋</span>
                            <div>
                                <h3 class="font-bold text-lg italic">Sumário Executivo</h3>
                                <ul class="mt-2 text-slate-500 space-y-2 text-sm">
                                    <li>• Módulo 1: O fundamento oculto de {tema}</li>
                                    <li>• Módulo 2: Estratégias de implementação rápida</li>
                                    <li>• Módulo 3: Maximização de resultados e escala</li>
                                    <li>• Bônus: Checklist de verificação final</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="bg-[#0f172a] text-white p-8 rounded-[2.5rem] h-fit sticky top-10 shadow-3xl shadow-indigo-200">
                    <p class="text-indigo-400 font-bold uppercase text-xs mb-2">Preço Exclusivo</p>
                    <p class="text-5xl font-black mb-6 italic">R$ 97,00</p>
                    <a href="{link_stripe}" class="block w-full bg-indigo-600 py-6 rounded-2xl text-center font-black text-xl hover:bg-indigo-500 transition-all shadow-lg mb-4">ADQUIRIR AGORA</a>
                    <div class="flex justify-center gap-4 opacity-50 grayscale hover:grayscale-0 transition-all cursor-pointer">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/b/b0/Apple_Pay_logo.svg" class="h-4">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/Visa_Inc._logo.svg" class="h-4">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/d/d6/Boleto_logo.svg" class="h-6">
                    </div>
                </div>
            </div>

            <section class="mt-32 pt-20 border-t border-slate-100 text-center">
                <h2 class="text-2xl font-black uppercase italic mb-12">Complete sua Jornada</h2>
                <div class="grid md:grid-cols-3 gap-8">
                    { "".join([f'<div class="p-8 border border-slate-100 rounded-3xl hover:border-indigo-200 transition-all"><h3 class="font-bold text-lg mb-2 italic uppercase">{p["nome"]}</h3><p class="text-indigo-600 font-black mb-4">{p["preco"]}</p><span class="text-xs font-bold text-slate-400">Apple Pay / Cartão / Boleto</span></div>' for p in outros_produtos]) }
                </div>
            </section>
        </main>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f: f.write(html_home)
    with open("detalhes.html", "w", encoding="utf-8") as f: f.write(html_detalhes)
