import os

def criar_estilo(tema_slug):
    # Dicionário de imagens contextuais (Homem e Mulher conversando sobre o tema)
    fotos = {
        "score": "https://images.unsplash.com/photo-1556742044-3c52d6e88c62?auto=format&fit=crop&q=80&w=1600",
        "renda": "https://images.unsplash.com/photo-1553729459-efe14ef6055d?auto=format&fit=crop&q=80&w=1600",
        "planilha": "https://images.unsplash.com/photo-1454165833767-027eeef1593e?auto=format&fit=crop&q=80&w=1600",
        "padrao": "https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?auto=format&fit=crop&q=80&w=1600"
    }
    foto_fundo = fotos.get(tema_slug, fotos["padrao"])

    return f"""
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800&family=Inter:wght@300;400;600&display=swap');
        
        body {{ 
            font-family: 'Inter', sans-serif; 
            background: linear-gradient(to bottom, rgba(15, 23, 42, 0.9), rgba(2, 6, 23, 1)), url('{foto_fundo}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: #fff; 
            min-height: 100vh;
        }}
        
        .titulo-master {{ 
            font-family: 'Montserrat', sans-serif; 
            font-weight: 800;
            letter-spacing: -0.04em;
            line-height: 0.9;
        }}

        .glass {{ 
            background: rgba(15, 23, 42, 0.6); 
            border: 1px solid rgba(255, 255, 255, 0.1); 
            backdrop-filter: blur(15px); 
        }}

        .btn-venda {{ 
            background: #fff; 
            color: #000; 
            transition: all 0.3s ease; 
            font-family: 'Montserrat', sans-serif;
            font-weight: 800;
        }}

        .btn-venda:hover {{ 
            transform: translateY(-5px); 
            box-shadow: 0 20px 40px rgba(255, 255, 255, 0.2); 
        }}

        .icon-accent {{ color: #818cf8; }}
    </style>
    """

def gerar_layout_pagina(tema, preco, link, slug="padrao", eh_detalhes=False, relacionados=[]):
    intro = f"O protocolo <strong>{tema}</strong> foi estruturado para entregar clareza e resultados reais. Removemos barreiras técnicas e entregamos o mapa para você dominar este tema com segurança e autoridade."

    conteudo_detalhes = ""
    if eh_detalhes:
        conteudo_detalhes = f"""
        <div class="mt-20 grid md:grid-cols-2 gap-8 text-left border-t border-white/10 pt-16">
            <div class="glass p-10 rounded-[2rem]">
                <h3 class="titulo-master text-2xl mb-8 uppercase">O que você vai dominar</h3>
                <ul class="space-y-4 text-slate-300">
                    <li><i class="fas fa-check-circle icon-accent mr-2"></i> Fundamentos de Alta Performance</li>
                    <li><i class="fas fa-check-circle icon-accent mr-2"></i> Aplicação Prática Imediata</li>
                    <li><i class="fas fa-check-circle icon-accent mr-2"></i> Estratégias de Escalonamento</li>
                </ul>
            </div>
            <div class="glass p-10 rounded-[2rem]">
                <h4 class="font-bold text-indigo-400 uppercase text-xs mb-6">Recursos Inclusos</h4>
                <div class="text-4xl titulo-master mb-4">{preco}</div>
                <a href="{link}" class="btn-venda block w-full py-6 rounded-2xl text-center uppercase tracking-tighter">ADQUIRIR AGORA</a>
            </div>
        </div>
        """

    return f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{tema} | Oficial</title>
        {criar_estilo(slug)}
    </head>
    <body class="py-12 px-6">
        <div class="max-w-6xl mx-auto">
            <header class="mb-20">
                <div class="flex items-center gap-2 mb-8">
                    <div class="w-8 h-8 bg-white rounded-full flex items-center justify-center text-black font-black italic">N</div>
                    <span class="font-bold tracking-widest uppercase text-xs">Nexus Alpha</span>
                </div>
                <h1 class="text-6xl md:text-8xl titulo-master uppercase mb-8 max-w-4xl tracking-tighter italic">#{tema}</h1>
                <p class="max-w-xl text-slate-300 text-lg leading-relaxed mb-10">{intro}</p>
                
                {f'<a href="detalhes.html" class="btn-venda inline-block px-12 py-5 rounded-full uppercase tracking-widest text-sm">Saiba Mais</a>' if not eh_detalhes else ""}
            </header>

            {conteudo_detalhes}

            { f'<div class="mt-32 pt-20 border-t border-white/10 text-center"><h3 class="titulo-master text-3xl mb-12 uppercase">Ecossistema de Soluções</h3><div class="grid md:grid-cols-3 gap-6">{" ".join([f"<a href=\'{p['slug']}.html\' class=\'glass p-10 rounded-[3rem] block hover:bg-white/5 transition-all\'><h4 class=\'titulo-master text-sm mb-4 uppercase\'>{p['nome']}</h4><p class=\'text-indigo-400 font-bold text-2xl\'>{p['preco']}</p></a>" for p in relacionados])}</div></div>' if eh_detalhes else "" }
        </div>
    </body>
    </html>
    """

def criar_pagina_vendas(tema, link_stripe):
    # AJUSTE FINAL: R$ 19,90 em todo o sistema
    preco_venda = "R$ 19,90"
    
    # Cada produto relacionado agora aponta para o link da Stripe de 19,90
    relacionados = [
        {"nome": "O Segredo do Score 900", "preco": preco_venda, "slug": "score", "link": link_stripe},
        {"nome": "Renda Extra Online", "preco": preco_venda, "slug": "renda", "link": link_stripe},
        {"nome": "Planilha de Lucros", "preco": preco_venda, "slug": "planilha", "link": link_stripe}
    ]

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(gerar_layout_pagina(tema, preco_venda, "detalhes.html", slug="padrao"))
    
    with open("detalhes.html", "w", encoding="utf-8") as f:
        f.write(gerar_layout_pagina(tema, preco_venda, link_stripe, slug="padrao", eh_detalhes=True, relacionados=relacionados))

    for p in relacionados:
        with open(f"{p['slug']}.html", "w", encoding="utf-8") as f:
            outros = [i for i in relacionados if i['slug'] != p['slug']]
            f.write(gerar_layout_pagina(p['nome'], p['preco'], p['link'], slug=p['slug'], eh_detalhes=True, relacionados=outros))
