import os

def criar_estilo(tema_slug):
    # Imagens contextuais de alta performance (sem rádio)
    fotos = {
        "score": "https://images.unsplash.com/photo-1551836022-d5d88e9218df?q=80&w=1600&auto=format&fit=crop",
        "renda": "https://images.unsplash.com/photo-1573161559525-460699b66235?q=80&w=1600&auto=format&fit=crop",
        "planilha": "https://images.unsplash.com/photo-1600880212340-02344079113f?q=80&w=1600&auto=format&fit=crop",
        "padrao": "https://images.unsplash.com/photo-15222071820081-009f0129c71c?q=80&w=1600&auto=format&fit=crop"
    }
    img = fotos.get(tema_slug, fotos["padrao"])

    return f"""
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,800;1,800&family=Inter:wght@300;400;700&display=swap');
        
        body {{ 
            font-family: 'Inter', sans-serif; 
            margin: 0; padding: 0;
            background: #020617;
            min-height: 100vh;
            color: #fff;
        }}
        
        .bg-hero {{
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(to bottom, rgba(2, 6, 23, 0.8) 0%, rgba(2, 6, 23, 1) 100%), url('{img}');
            background-size: cover; background-position: center; z-index: -1;
        }}

        .titulo-master {{ 
            font-family: 'Montserrat', sans-serif; font-weight: 800;
            letter-spacing: -0.05em; line-height: 0.85;
            color: #39FF14;
        }}

        .neon-text {{ color: #39FF14; }}
        .white-text {{ color: #ffffff; }}

        .glass {{ 
            background: rgba(255, 255, 255, 0.03); 
            border: 1px solid rgba(255, 255, 255, 0.1); 
            backdrop-filter: blur(25px); border-radius: 3rem;
        }}

        .btn-venda {{ 
            background: #ffffff; 
            color: #000000; 
            font-family: 'Montserrat', sans-serif;
            font-weight: 800; 
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }}

        .btn-venda:hover {{ transform: scale(1.05); box-shadow: 0 0 30px rgba(255, 255, 255, 0.4); }}
    </style>
    """

def gerar_layout_pagina(tema, preco, link, slug="padrao", eh_detalhes=False, relacionados=[]):
    copy_convencimento = f"Você está a um passo de dominar o <strong>{tema}</strong>. Este protocolo exclusivo foi desenhado para quem busca autonomia e resultados inquestionáveis."

    conteudo_extra = ""
    if eh_detalhes:
        conteudo_extra = f"""
        <div class="grid md:grid-cols-2 gap-8 mt-20 text-left border-t border-white/10 pt-16">
            <div class="glass p-10">
                <h3 class="titulo-master text-2xl mb-6 uppercase italic">#Plano de Ação</h3>
                <ul class="space-y-4">
                    <li class="white-text"><i class="fas fa-bolt mr-2" style="color: #FFD700;"></i> Implementação em menos de 24h</li>
                    <li class="white-text"><i class="fas fa-lock mr-2" style="color: #39FF14;"></i> Estratégia Blindada Antiautolote</li>
                    <li class="white-text"><i class="fas fa-chart-line mr-2" style="color: #A855F7;"></i> Escalonamento de Ganhos</li>
                </ul>
            </div>
            <div class="glass p-10 text-center flex flex-col justify-center">
                <span class="text-xs font-bold uppercase tracking-widest neon-text mb-2 italic">Oferta Vitalícia</span>
                <div class="white-text titulo-master text-6xl mb-8 tracking-tighter" style="color: white;">{preco}</div>
                <a href="{link}" class="btn-venda py-6 rounded-2xl text-xl uppercase tracking-tighter shadow-lg">Adquirir Agora</a>
                <div class="flex justify-center gap-6 mt-8 opacity-80">
                    <i class="fab fa-apple-pay text-3xl"></i>
                    <i class="fab fa-cc-visa text-3xl"></i>
                    <i class="fab fa-cc-mastercard text-3xl"></i>
                    <i class="fas fa-barcode text-2xl"></i>
                </div>
            </div>
        </div>
        """

    return f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{tema} | Nexus Alpha</title>
        {criar_estilo(slug)}
    </head>
    <body>
        <div class="bg-hero"></div>
        <div class="max-w-6xl mx-auto px-6 py-20">
            <header class="text-left mb-20">
                <div class="bg-white/10 w-fit px-4 py-1 rounded-full text-[10px] font-bold uppercase tracking-widest mb-10 neon-text">AI Premium Environment</div>
                <h1 class="titulo-master text-6xl md:text-[100px] uppercase italic mb-8">#{tema}</h1>
                <p class="max-w-xl text-slate-300 text-xl leading-relaxed mb-10">{copy_convencimento}</p>
                {f'<a href="detalhes.html" class="btn-venda px-12 py-5 rounded-full uppercase tracking-widest text-sm">Explorar Solução</a>' if not eh_detalhes else ""}
            </header>

            {conteudo_extra}

            { f'<div class="mt-40 pt-20 border-t border-white/10 text-center"><h3 class="white-text titulo-master text-4xl mb-12 uppercase italic" style="color:white">Produtos Relacionados</h3><div class="grid md:grid-cols-3 gap-8">{" ".join([f"<a href=\'{p['slug']}.html\' class=\'glass p-10 block hover:bg-white/10 transition-all\'><h4 class=\'titulo-master text-xl mb-4 uppercase\' style=\'color: #39FF14\'>{p['nome']}</h4><p class=\'white-text font-bold text-3xl\' style=\'color:white\'>{p['preco']}</p></a>" for p in relacionados])}</div></div>' if eh_detalhes else "" }
        </div>
    </body>
    </html>
    """

def criar_pagina_vendas(tema, link_stripe):
    # LINK OFICIAL STRIPE ATUALIZADO
    link_venda = "https://buy.stripe.com/9B6fZ976y7zJ6qn0jl4c80v"
    preco_final = "R$ 19,90"
    
    relacionados = [
        {"nome": "Score 900 Turbo", "preco": preco_final, "slug": "score", "link": link_venda},
        {"nome": "Renda Passiva", "preco": preco_final, "slug": "renda", "link": link_venda},
        {"nome": "Planilha Lucros", "preco": preco_final, "slug": "planilha", "link": link_venda}
    ]

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(gerar_layout_pagina(tema, preco_final, "detalhes.html", slug="padrao"))
    
    with open("detalhes.html", "w", encoding="utf-8") as f:
        f.write(gerar_layout_pagina(tema, preco_final, link_venda, slug="padrao", eh_detalhes=True, relacionados=relacionados))

    for p in relacionados:
        with open(f"{p['slug']}.html", "w", encoding="utf-8") as f:
            outros = [i for i in relacionados if i['slug'] != p['slug']]
            f.write(gerar_layout_pagina(p['nome'], p['preco'], p['link'], slug=p['slug'], eh_detalhes=True, relacionados=outros))
