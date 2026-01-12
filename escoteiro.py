import random

def criar_estilo():
    img_fundo = "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=1600"
    return f"""
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,900;1,900&family=Inter:wght@400;700;900&display=swap');
        :root {{ --neon: #39FF14; --dark: #020617; }}
        body {{ font-family: 'Inter', sans-serif; background: var(--dark); color: #fff; margin: 0; overflow-x: hidden; }}
        .bg-nexus {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, rgba(2, 6, 23, 0.94) 0%, rgba(2, 6, 23, 1) 100%), url('{img_fundo}'); background-size: cover; z-index: -1; }}
        .titulo-nexus {{ font-family: 'Montserrat', sans-serif; font-weight: 900; font-style: italic; letter-spacing: -2px; }}
        .logo-link {{ text-decoration: none; transition: 0.3s; }}
        .logo-link:hover {{ transform: scale(1.05); filter: drop-shadow(0 0 10px var(--neon)); }}
        .headline-elite {{ font-family: 'Montserrat', sans-serif; font-weight: 900; color: var(--neon); text-transform: uppercase; font-style: italic; line-height: 0.9; letter-spacing: -3px; }}
        .glass {{ background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(57, 255, 20, 0.2); backdrop-filter: blur(20px); border-radius: 2rem; }}
        .price-box {{ font-family: 'Montserrat', sans-serif; font-weight: 900; font-size: 6rem; line-height: 1; display: flex; align-items: center; justify-content: center; gap: 10px; color: #fff; }}
        .btn-venda-total {{ background: var(--neon) !important; color: #000 !important; font-family: 'Montserrat', sans-serif; font-weight: 900; display: inline-flex; align-items: center; justify-content: center; width: 100%; max-width: 600px; border-radius: 1rem; padding: 1.8rem 1rem; font-size: 2.2rem; text-transform: uppercase; text-decoration: none; box-shadow: 0 0 50px rgba(57, 255, 20, 0.4); transition: 0.4s; }}
        .frame-ia {{ width: 100%; border-radius: 2rem; border: 3px solid var(--neon); box-shadow: 0 0 30px rgba(57, 255, 20, 0.2); }}
        .behance-wrapper {{ position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 1.5rem; border: 1px solid var(--neon); margin: 3rem 0; }}
        .behance-wrapper iframe {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; }}
        @media (max-width: 600px) {{ .price-box {{ font-size: 3.5rem; }} .btn-venda-total {{ font-size: 1.4rem; }} .headline-elite {{ font-size: 2.8rem !important; }} }}
    </style>
    """

def gerar_layout_pagina(tema, preco, link, eh_produto=False, relacionados=[], legal_body=None, copy_data=None):
    # Logotipo clicável conforme solicitado
    header = f'''<header class="flex justify-between items-center mb-24">
        <a href="index.html" class="logo-link titulo-nexus text-4xl no-underline text-white">NEXUS<span class="text-green-500">ALPHA</span></a>
        <div class="text-[10px] opacity-40 font-bold italic text-white uppercase tracking-widest">Server 2026 Ready</div>
    </header>'''

    if legal_body:
        conteudo = f'<div class="glass p-12 mt-10"><h1 class="headline-elite mb-8 text-4xl">{tema}</h1><div class="text-slate-400 leading-relaxed">{legal_body}</div></div>'
    elif eh_produto and copy_data:
        # 3 Produtos Relacionados Aleatórios
        outros = [p for p in relacionados if p['nome'] != tema]
        selecionados = random.sample(outros, 3) if len(outros) >= 3 else outros
        rel_html = "".join([f'''<a href="{p['slug']}.html" class="glass p-6 border border-white/10 hover:border-green-400 block no-underline">
            <h4 class="titulo-nexus text-green-400 text-sm mb-2 uppercase">{p['nome']}</h4>
            <p class="text-white font-black">R$ 19,90</p></a>''' for p in selecionados])

        conteudo = f"""
        <div class="text-center mb-16"><h1 class="headline-elite text-6xl md:text-9xl">{copy_data['h1']}</h1></div>
        <div class="grid md:grid-cols-2 gap-12 items-center mb-20">
            <div><img src="{copy_data['img']}" class="frame-ia" alt="PRODUTO"></div>
            <div class="space-y-8"><p class="text-2xl font-light text-slate-300">{copy_data['desc']}</p></div>
        </div>
        <div class="behance-wrapper"><iframe src="https://www.behance.net/embed/project/240268905?ilo0=1" allowfullscreen frameborder="0"></iframe></div>
        <div class="glass p-16 text-center mb-20 border-2 border-green-500/30">
            <div class="price-box mb-8">R$ 19,90</div>
            <a href="{link}" class="btn-venda-total">ADQUIRIR AGORA</a>
        </div>
        <div class="mt-32"><h3 class="titulo-nexus text-center text-xl mb-12 italic uppercase">Soluções Relacionadas</h3><div class="grid grid-cols-1 md:grid-cols-3 gap-6">{rel_html}</div></div>
        """
    else:
        conteudo = f'<div class="text-center py-32"><h1 class="headline-elite text-8xl italic">NEXUS ALPHA</h1><a href="ia-pro.html" class="btn-venda-total">INICIAR</a></div>'

    return f"""<!DOCTYPE html><html lang="pt-br"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{tema}</title>{criar_estilo()}</head><body><div class="bg-nexus"></div>
    <div class="max-w-6xl mx-auto px-6 py-12">{header}{conteudo}
    <footer class="mt-40 py-20 border-t border-white/10 text-center">
    <div class="flex justify-center gap-10 mb-10 text-xs font-bold uppercase opacity-60">
        <a href="privacidade.html" class="text-white no-underline hover:text-green-500">Privacidade</a>
        <a href="termos.html" class="text-white no-underline hover:text-green-500">Termos de Uso</a>
    </div></footer></div></body></html>"""