import os

def criar_estilo():
    # URL da imagem do especialista solicitada
    img_ia_investor = "https://images.squarespace-cdn.com/content/v1/5f973693e54f0a28f4f3e696/1706645353153-6U1V5X7X9P4Z4W5Z5X5Z/IA_Investor_Pro_Expert.jpg"
    
    return f"""
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,900;1,900&family=Inter:wght@400;700;900&display=swap');
        
        :root {{ --neon: #39FF14; --dark: #020617; }}
        
        body {{ 
            font-family: 'Inter', sans-serif; 
            background: var(--dark); 
            color: #fff; 
            margin: 0; 
            scroll-behavior: smooth; 
            overflow-x: hidden; 
        }}

        /* Camada de Fundo Estática para Performance */
        .bg-fixed {{ 
            position: fixed; top: 0; left: 0; width: 100%; height: 100%; 
            background: radial-gradient(circle at top right, rgba(57, 255, 20, 0.05), transparent), var(--dark);
            z-index: -1; 
        }}
        
        /* Títulos com Força de Conversão */
        .titulo-master {{ 
            font-family: 'Montserrat', sans-serif; 
            font-weight: 900; 
            color: var(--neon); 
            text-transform: uppercase; 
            font-style: italic; 
            line-height: 1;
            letter-spacing: -2px;
        }}

        .glass {{ 
            background: rgba(255, 255, 255, 0.02); 
            border: 1px solid rgba(255, 255, 255, 0.08); 
            backdrop-filter: blur(20px); 
            border-radius: 2rem; 
        }}

        /* VALOR R$ 19,90 - TAMANHO UNIFICADO E GIGANTE */
        .valor-container {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            color: #ffffff;
            font-family: 'Montserrat', sans-serif;
            font-weight: 900;
            font-size: 5rem; /* Tamanho Elite */
            line-height: 1;
            margin-bottom: 1.5rem;
            white-space: nowrap;
        }}
        .valor-container span {{ font-size: 5rem; }}

        /* BOTÃO ADQUIRIR AGORA - LINHA ÚNICA */
        .btn-cta {{ 
            background: var(--neon); 
            color: #000; 
            font-family: 'Montserrat', sans-serif; 
            font-weight: 900; 
            font-size: 1.8rem; 
            padding: 1.5rem 2rem; 
            border-radius: 1.2rem; 
            text-decoration: none; 
            display: inline-flex; 
            align-items: center; 
            justify-content: center;
            width: 100%;
            max-width: 600px;
            white-space: nowrap;
            text-transform: uppercase;
            box-shadow: 0 0 30px rgba(57, 255, 20, 0.4);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .btn-cta:hover {{ transform: scale(1.03); box-shadow: 0 0 60px rgba(57, 255, 20, 0.6); }}

        /* Textos de Apoio */
        .texto-corpo {{ font-size: 1.5rem; line-height: 1.6; color: #94a3b8; }}
        .badge-neon {{ color: var(--neon); font-weight: 900; font-size: 1.2rem; text-transform: uppercase; }}

        /* Otimização Mobile Extrema */
        @media (max-width: 640px) {{
            .valor-container, .valor-container span {{ font-size: 3.5rem; }}
            .btn-cta {{ font-size: 1.4rem; padding: 1.2rem 1rem; }}
            .titulo-master {{ font-size: 2.8rem !important; }}
            .texto-corpo {{ font-size: 1.2rem; }}
        }}

        .img-ia {{ 
            width: 100%; 
            border-radius: 1.5rem; 
            border: 2px solid var(--neon); 
            box-shadow: 0 20px 50px rgba(0,0,0,0.5); 
        }}
    </style>
    """

def obter_copy(tema):
    img_ia = "https://images.squarespace-cdn.com/content/v1/5f973693e54f0a28f4f3e696/1706645353153-6U1V5X7X9P4Z4W5Z5X5Z/IA_Investor_Pro_Expert.jpg"
    banco = {
        "IA Investor Pro": {
            "h1": "IA INVESTOR PRO",
            "p": "O algoritmo avançado que opera diagramas de tendência em tempo real. Lucratividade automatizada com precisão cirúrgica.",
            "check": "Tecnologia de Arbitragem 2026",
            "img": img_ia,
            "av": ["'O robô trabalha por mim 24h.' - Sofia R.", "'Minha rentabilidade mudou.' - Gabriel T."]
        },
        "Score 900 Turbo": {
            "h1": "SCORE 900 TURBO",
            "p": "Limpeza de histórico e ativação de gatilhos bancários. Destrave cartões Black e limites altos hoje.",
            "check": "Aprovação Imediata",
            "img": "https://images.unsplash.com/photo-1563986768609-322da13575f3?q=80&w=1200",
            "av": ["'Meu score foi de 300 para 850.' - Ricardo S.", "'Cartão aprovado na hora.' - Amanda L."]
        }
    }
    return banco.get(tema, banco["IA Investor Pro"])

def gerar_layout_pagina(tema, preco, link, eh_produto=False):
    copy = obter_copy(tema)
    
    if eh_produto:
        html_av = "".join([f'<div class="glass p-6 italic text-xl">"{a}"</div>' for a in copy['av']])
        conteudo = f"""
        <div class="text-center mb-16"><h1 class="titulo-master text-6xl md:text-8xl italic">{copy['h1']}</h1></div>
        
        <div class="grid md:grid-cols-2 gap-12 items-center mb-24">
            <div><img src="{copy['img']}" class="img-ia" alt="IA Investor"></div>
            <div class="space-y-8">
                <p class="badge-neon"><i class="fas fa-microchip mr-2"></i> EXCLUSIVO NEXUS ALPHA</p>
                <p class="texto-corpo">{copy['p']}</p>
                <div class="glass p-6 border-l-4 border-green-500">
                    <p class="font-bold text-white text-xl">{copy['check']}</p>
                </div>
            </div>
        </div>

        <div class="mb-24">
            <h2 class="titulo-master text-center text-3xl mb-12 italic">AVALIAÇÕES REAIS</h2>
            <div class="grid md:grid-cols-2 gap-8">{html_av}</div>
        </div>

        <div class="glass p-12 text-center border-2 border-green-500/30">
            <div class="valor-container"><span>R$</span> 19,90</div>
            <a href="{link}" class="btn-cta">ADQUIRIR AGORA</a>
            <p class="mt-8 text-sm opacity-50 uppercase tracking-widest font-bold">
                <i class="fas fa-lock mr-2"></i> Pagamento Seguro | Acesso Imediato
            </p>
        </div>
        """
    else:
        conteudo = f'<div class="text-center py-32"><h1 class="titulo-master text-8xl md:text-9xl mb-16 italic">#{tema}</h1><a href="ia-pro.html" class="btn-cta">INICIAR SISTEMA</a></div>'

    return f"""<!DOCTYPE html>
    <html lang="pt-br"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{tema}</title>{criar_estilo()}</head>
    <body><div class="bg-fixed"></div><div class="max-w-6xl mx-auto px-6 py-12">
    <header class="flex justify-between items-center mb-20"><span class="text-2xl font-black italic">NEXUS<span class="text-green-500">ALPHA</span></span><span class="text-[10px] opacity-40 font-bold uppercase tracking-widest">IA Active 2026</span></header>
    {conteudo}
    <footer class="mt-40 py-12 border-t border-white/10 text-center opacity-20 text-[10px] font-bold uppercase tracking-widest">Nexus Alpha System Brasil</footer></div></body></html>"""

def criar_pagina_vendas(tema, link_stripe):
    link_final = "https://buy.stripe.com/9B6fZ976y7zJ6qn0jl4c80v"
    with open("index.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina(tema, "R$ 19,90", "ia-pro.html"))
    with open("ia-pro.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina("IA Investor Pro", "R$ 19,90", link_final, eh_produto=True))
    with open("score.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina("Score 900 Turbo", "R$ 19,90", link_final, eh_produto=True))