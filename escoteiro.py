import os

def criar_estilo():
    foto_unificada = "https://images.unsplash.com/photo-1551836022-d5d88e9218df?q=80&w=1600&auto=format&fit=crop"
    return f"""
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,800;1,800&family=Inter:wght@300;400;700&display=swap');
        body {{ font-family: 'Inter', sans-serif; background: #020617; color: #fff; margin: 0; scroll-behavior: smooth; }}
        .bg-hero {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to bottom, rgba(2, 6, 23, 0.9) 0%, rgba(2, 6, 23, 1) 100%), url('{foto_unificada}'); background-size: cover; background-position: center; z-index: -1; }}
        .titulo-master {{ font-family: 'Montserrat', sans-serif; font-weight: 800; letter-spacing: -0.05em; color: #39FF14; text-transform: uppercase; font-style: italic; }}
        .glass {{ background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(25px); border-radius: 2rem; }}
        .btn-venda {{ background: #fff; color: #000; font-family: 'Montserrat', sans-serif; font-weight: 800; transition: 0.3s; display: block; width: 100%; text-align: center; border-radius: 1rem; }}
        .btn-venda:hover {{ transform: scale(1.05); box-shadow: 0 0 40px rgba(57, 255, 20, 0.4); }}
        .neon-border {{ border: 1px solid #39FF14; }}
    </style>
    """

def gerar_layout_pagina(tema, preco, link, eh_detalhes=False, relacionados=[]):
    # Conteúdo expandido baseado nos Elementos Essenciais
    detalhes_produtos = {
        "Score 900 Turbo": {
            "subtitulo": "O segredo para ter aprovação imediata em qualquer banco.",
            "beneficios": "Aprenda a manipular os gatilhos de crédito e subir sua pontuação de forma orgânica.",
            "modulos": ["Módulo 1: O Sistema Bancário Oculto", "Módulo 2: Limpando o Histórico de Consultas", "Módulo 3: O Gatilho dos 900 Pontos"],
            "faq": "É seguro? Sim, 100% dentro das leis bancárias. Quanto tempo demora? Os resultados aparecem em até 14 dias."
        },
        "Renda Extra": {
            "subtitulo": "Transforme seu celular em uma fonte diária de lucro.",
            "beneficios": "Métodos de arbitragem digital e tarefas remuneradas que pagam em dólar e real.",
            "modulos": ["Módulo 1: Configuração da Carteira", "Módulo 2: Arbitragem de Micro-tarefas", "Módulo 3: Escalando para R$ 100/dia"],
            "faq": "Preciso investir? Não, apenas seu tempo. Funciona no iPhone? Sim, Android e iOS."
        },
        "Planilha Lucros": {
            "subtitulo": "Domine cada centavo com Inteligência Artificial.",
            "beneficios": "Visualize gargalos financeiros e projete sua liberdade em um dashboard profissional.",
            "modulos": ["Módulo 1: Importação de Dados IA", "Módulo 2: Projeção de Patrimônio", "Módulo 3: Corte de Gastos Invisíveis"],
            "faq": "É difícil usar? Não, ela é 100% automatizada. Precisa de Excel? Funciona no Google Sheets e Excel."
        }
    }
    
    info = detalhes_produtos.get(tema, {"subtitulo": "Alta Performance", "beneficios": "Resultados reais.", "modulos": [], "faq": ""})

    # Logos Stripe (Sem Pix)
    logos_pagamento = """
    <div class="flex justify-center gap-6 mt-6 text-2xl opacity-70">
        <i class="fab fa-cc-visa"></i> <i class="fab fa-cc-mastercard"></i> <i class="fab fa-apple-pay"></i> <i class="fas fa-barcode"></i>
    </div>
    """

    conteudo_venda = ""
    if eh_detalhes:
        conteudo_venda = f"""
        <div class="mt-16 space-y-12">
            <div class="text-center">
                <h2 class="titulo-master text-4xl md:text-6xl mb-4 italic">#{tema}</h2>
                <p class="text-xl text-green-400 font-bold uppercase tracking-widest mb-8">{info['subtitulo']}</p>
                <div class="glass p-4 inline-block neon-border"><img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=500" class="rounded-xl shadow-2xl"></div>
            </div>

            <div class="glass p-10">
                <h3 class="titulo-master text-2xl mb-6">Porque este método é para você:</h3>
                <p class="text-slate-300 text-lg leading-relaxed mb-8">{info['beneficios']}</p>
                <div class="grid md:grid-cols-3 gap-6">
                    {" ".join([f'<div class="bg-white/5 p-6 rounded-2xl border border-white/10"><i class="fas fa-check-circle text-green-500 mb-4 text-2xl"></i><p class="font-bold">{m}</p></div>' for m in info['modulos']])}
                </div>
            </div>

            <div class="grid md:grid-cols-2 gap-8">
                <div class="glass p-10 italic">"Minha vida financeira mudou em 10 dias. O suporte é impecável."<br><br><strong>- Carlos M., Aluno Nexus</strong></div>
                <div class="glass p-10">
                    <h3 class="titulo-master text-xl mb-4">Sobre o Autor</h3>
                    <p class="text-sm opacity-80">Especialista em algoritmos e sistemas de crédito com mais de 10 anos de mercado.</p>
                </div>
            </div>

            <div class="glass p-12 text-center neon-border">
                <span class="bg-green-500 text-black px-4 py-1 rounded-full font-bold text-xs uppercase">Bônus: Suporte VIP IA incluso</span>
                <div class="titulo-master text-8xl my-8">{preco}</div>
                <a href="{link}" class="btn-venda py-8 text-2xl uppercase">ADQUIRIR AGORA</a>
                {logos_pagamento}
                <div class="mt-8 flex items-center justify-center gap-4 text-sm text-green-400">
                    <i class="fas fa-shield-alt text-3xl"></i>
                    <p class="text-left font-bold uppercase tracking-tighter">Garantia Incondicional de 7 Dias<br><span class="text-white opacity-50 text-[10px]">Risco Zero para o seu Bolso</span></p>
                </div>
            </div>

            <div class="glass p-10">
                <h3 class="titulo-master text-2xl mb-6 text-center">Perguntas Frequentes</h3>
                <p class="text-slate-400 italic text-center">{info['faq']}</p>
            </div>
        </div>
        """

    return f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{tema} | Nexus Alpha</title>
        {criar_estilo()}
    </head>
    <body>
        <div class="bg-hero"></div>
        <div class="max-w-5xl mx-auto px-6 py-20">
            <header class="flex justify-between items-center mb-20">
                <div class="text-2xl font-black italic tracking-tighter">NEXUS<span class="text-green-500">ALPHA</span></div>
                <div class="text-[10px] font-bold uppercase tracking-[0.3em] opacity-50">Market Intelligence Active</div>
            </header>
            
            {conteudo_venda if eh_detalhes else f'<h1 class="titulo-master text-7xl md:text-9xl mb-12 italic">#{tema}</h1><a href="detalhes.html" class="btn-venda py-6 text-xl">ACESSAR PROTOCOLO</a>'}
            
            <footer class="mt-40 py-10 border-t border-white/10 text-[10px] opacity-30 text-center uppercase tracking-widest">
                <p>© 2026 Nexus Alpha System - CNPJ 00.000.000/0001-00</p>
                <p class="mt-2">Política de Privacidade | Termos de Uso</p>
            </footer>
        </div>
    </body>
    </html>
    """

def criar_pagina_vendas(tema, link_stripe):
    link_venda = "https://buy.stripe.com/9B6fZ976y7zJ6qn0jl4c80v"
    preco_final = "R$ 19,90"
    relacionados = [
        {"nome": "Score 900 Turbo", "preco": preco_final, "slug": "score", "link": link_venda},
        {"nome": "Renda Extra", "preco": preco_final, "slug": "renda", "link": link_venda},
        {"nome": "Planilha Lucros", "preco": preco_final, "slug": "planilha", "link": link_venda}
    ]
    with open("index.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina(tema, preco_final, "detalhes.html"))
    with open("detalhes.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina(tema, preco_final, link_venda, eh_detalhes=True, relacionados=relacionados))
    for p in relacionados:
        with open(f"{p['slug']}.html", "w", encoding="utf-8") as f:
            f.write(gerar_layout_pagina(p['nome'], p['preco'], p['link'], eh_detalhes=True))
