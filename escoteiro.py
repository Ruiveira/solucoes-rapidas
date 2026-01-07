def criar_estilo():
    return """
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,700&family=Inter:wght@300;400;700&display=swap');
        body { font-family: 'Inter', sans-serif; background-color: #050505; color: #fff; }
        .font-luxury { font-family: 'Playfair Display', serif; }
        .gradient-text { 
            background: linear-gradient(to right, #ffffff, #818cf8); 
            background-clip: text; -webkit-background-clip: text; 
            -webkit-text-fill-color: transparent; color: transparent;
        }
        .glass { background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(12px); }
        .btn-action { background: #ffffff; color: #000; transition: all 0.4s ease; }
        .btn-action:hover { transform: translateY(-3px); box-shadow: 0 15px 30px rgba(99, 102, 241, 0.4); }
    </style>
    """

def gerar_layout_pagina(tema, preco, link, eh_detalhes=False, relacionados=[]):
    # Conteúdo expandido para autoridade
    detalhes_html = ""
    if eh_detalhes:
        detalhes_html = f"""
        <div class="mt-20 grid md:grid-cols-2 gap-16 text-left border-t border-white/10 pt-16">
            <div>
                <h3 class="font-luxury italic text-3xl mb-8 uppercase tracking-tighter">O que você vai dominar</h3>
                <div class="space-y-6 text-slate-400">
                    <p>• <strong class="text-white">Módulo I:</strong> A Anatomia da Maestria em {tema}.</p>
                    <p>• <strong class="text-white">Módulo II:</strong> Protocolos de Execução Rápida e Escala.</p>
                    <p>• <strong class="text-white">Módulo III:</strong> Blindagem de Resultados e Gestão Avançada.</p>
                </div>
            </div>
            <div class="glass p-8 rounded-3xl">
                <h4 class="font-bold text-indigo-400 uppercase text-xs tracking-widest mb-4">Incluso no Acesso</h4>
                <ul class="text-sm space-y-3">
                    <li>✅ Videoaulas em Alta Definição</li>
                    <li>✅ Material de Apoio (PDF Executivo)</li>
                    <li>✅ Planilhas de Implementação</li>
                    <li>✅ Certificado de Conclusão Oficial</li>
                </ul>
            </div>
        </div>
        """

    # Ícones de Pagamento em SVG (Branco para visibilidade)
    icones_pagamento = """
    <div class="flex justify-center gap-6 mt-8 opacity-80">
        <svg class="h-6 w-auto" viewBox="0 0 100 40" fill="white"><path d="M35 15h-3v10h3v-10zM45 15h-5v10h5v-2h-3v-2h3v-2h-3v-2h3v-2z"/></svg> <svg class="h-6 w-auto" viewBox="0 0 100 40" fill="white"><path d="M10 10h80v20h-80z"/></svg> <svg class="h-6 w-auto" viewBox="0 0 100 40" fill="white"><rect x="10" y="5" width="2" height="30"/><rect x="15" y="5" width="4" height="30"/><rect x="22" y="5" width="2" height="30"/></svg> </div>
    """

    return f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{tema} | Oficial</title>
        {criar_estilo()}
    </head>
    <body class="antialiased">
        <div class="max-w-5xl mx-auto px-6 py-20 text-center">
            <span class="text-indigo-500 font-bold tracking-[0.4em] text-[10px] uppercase mb-4 block">Acesso Privilegiado</span>
            <h1 class="text-5xl md:text-7xl font-luxury italic gradient-text uppercase mb-10 leading-none">{tema}</h1>
            
            <p class="max-w-2xl mx-auto text-slate-400 text-lg mb-12 leading-relaxed">
                Descubra os fundamentos que transcendem o senso comum e posicione-se no topo com o protocolo <span class="text-white italic">{tema}</span>.
            </p>

            <div class="glass p-12 rounded-[3rem] max-w-lg mx-auto mb-20">
                <p class="text-indigo-400 text-xs font-bold uppercase mb-2">Valor de Investimento</p>
                <div class="text-6xl font-luxury italic mb-8">{preco}</div>
                <a href="{link}" class="btn-action block w-full py-6 rounded-2xl font-black text-xl uppercase tracking-tighter">
                    { "ADQUIRIR AGORA" if eh_detalhes else "EXPLORAR DETALHES" }
                </a>
                {icones_pagamento}
            </div>

            {detalhes_html}

            { f'<div class="mt-32 pt-16 border-t border-white/10"><h3 class="font-luxury italic text-2xl mb-12">Expandir Inteligência</h3><div class="grid md:grid-cols-3 gap-6">{" ".join([f"<a href=\'{p['slug']}.html\' class=\'glass p-8 rounded-3xl hover:bg-white/5 transition-all\'><h4 class=\'font-bold text-sm uppercase italic mb-2\'>{p['nome']}</h4><p class=\'text-indigo-400 font-bold\'>{p['preco']}</p></a>" for p in relacionados])}</div></div>' if eh_detalhes else "" }
        </div>
    </body>
    </html>
    """

def criar_pagina_vendas(tema, link_stripe):
    # O Robô agora sincroniza o preço de R$ 10,00 como base ou o que você definir
    preco_fixo = "R$ 10,00"
    
    relacionados = [
        {"nome": "O Segredo do Score 900", "preco": preco_fixo, "slug": "score", "link": link_stripe},
        {"nome": "Renda Extra Online", "preco": preco_fixo, "slug": "renda", "link": link_stripe},
        {"nome": "Planilha de Lucros", "preco": preco_fixo, "slug": "planilha", "link": link_stripe}
    ]

    # Home
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(gerar_layout_pagina(tema, preco_fixo, "detalhes.html"))
    
    # Detalhes
    with open("detalhes.html", "w", encoding="utf-8") as f:
        f.write(gerar_layout_pagina(tema, preco_fixo, link_stripe, eh_detalhes=True, relacionados=relacionados))

    # Páginas dos Relacionados (Sempre sincronizadas)
    for p in relacionados:
        with open(f"{p['slug']}.html", "w", encoding="utf-8") as f:
            f.write(gerar_layout_pagina(p['nome'], p['preco'], p['link'], eh_detalhes=True))
