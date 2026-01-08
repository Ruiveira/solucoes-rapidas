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
        .btn-venda:hover {{ transform: scale(1.05); box-shadow: 0 0 50px rgba(57, 255, 20, 0.5); border: 2px solid #39FF14; }}
        .neon-border {{ border: 1px solid #39FF14; }}
        .faq-item {{ border-bottom: 1px solid rgba(255,255,255,0.1); padding: 15px 0; }}
        .beneficio-card {{ background: rgba(57, 255, 20, 0.05); border-left: 4px solid #39FF14; padding: 20px; border-radius: 0 1rem 1rem 0; }}
    </style>
    """

def obter_copy_produto(tema):
    # Base de dados de copy detalhada para cada produto
    dados = {
        "Score 900 Turbo": {
            "headline": "A Chave Mestra para destravar seu Crédito Bancário em tempo recorde.",
            "descricao": "O Protocolo Score 900 é um método matemático testado para elevar sua pontuação nos birôs de crédito através de gatilhos de comportamento bancário.",
            "modulos": ["Módulo 1: O Algoritmo Bancário Oculto", "Módulo 2: Limpeza de Consultas Excessivas", "Módulo 3: O Gatilho de Aprovação Imediata"],
            "beneficios": "Consiga financiamentos, cartões de crédito de alto limite e juros menores em qualquer banco.",
            "faq": [("É seguro?", "Sim, o método utiliza apenas leis de transparência bancária."), ("Quanto tempo leva?", "Os primeiros resultados aparecem entre 7 a 14 dias.")]
        },
        "Renda Extra": {
            "headline": "Transforme seu Tempo Livre em uma Máquina de Ganhos Diários.",
            "descricao": "Aprenda as estratégias de arbitragem digital e micro-tarefas premium que as empresas não querem que você saiba.",
            "modulos": ["Módulo 1: Configuração de Carteiras Digitais", "Módulo 2: O Mercado de Micro-arbitragem", "Módulo 3: Escala de Ganhos com Automação"],
            "beneficios": "Liberdade geográfica e financeira trabalhando apenas 2 horas por dia usando seu celular.",
            "faq": [("Preciso investir?", "Não, o método foca em gerar renda com custo zero."), ("Funciona em qualquer celular?", "Sim, basta ter acesso à internet.")]
        },
        "Planilha Lucros": {
            "headline": "A Inteligência Artificial que Organiza e Multiplica seu Patrimônio.",
            "descricao": "Uma ferramenta automatizada que analisa seus gastos e projeta sua liberdade financeira com dashboards profissionais.",
            "modulos": ["Módulo 1: Integração IA de Gastos", "Módulo 2: Projeção de Investimentos", "Módulo 3: Identificação de Desperdício Oculto"],
            "beneficios": "Tenha clareza total de cada centavo e saiba exatamente quando você poderá se aposentar.",
            "faq": [("É difícil de usar?", "Não, a planilha é 100% intuitiva e automatizada."), ("Funciona no celular?", "Sim, via Google Sheets ou Excel Mobile.")]
        }
    }
    return dados.get(tema, dados["Score 900 Turbo"])

def gerar_layout_pagina(tema, preco, link, eh_detalhes=False, relacionados=[]):
    copy = obter_copy_produto(tema)
    
    # 3 Relacionados Garantidos
    html_relacionados = ""
    for p in relacionados:
        html_relacionados += f'''
        <a href="{p['slug']}.html" class="glass p-8 block hover:bg-white/10 transition-all text-center border border-white/5">
            <h4 class="titulo-master text-lg mb-2 italic" style="color: #39FF14">{p['nome']}</h4>
            <p class="text-white font-bold text-2xl">{p['preco']}</p>
        </a>'''

    # Estrutura de Landing Page (Headline, Benefícios, FAQ, Garantia)
    conteudo_venda = ""
    if eh_detalhes:
        html_modulos = "".join([f'<li class="mb-2"><i class="fas fa-arrow-right text-green-500 mr-2"></i>{m}</li>' for m in copy['modulos']])
        html_faq = "".join([f'<div class="faq-item"><strong>{q}</strong><p class="opacity-70 text-sm mt-2">{a}</p></div>' for q, a in copy['faq']])
        
        conteudo_venda = f"""
        <div class="mt-10 space-y-16">
            <div class="text-center">
                <h1 class="titulo-master text-4xl md:text-7xl mb-6 italic leading-tight">{copy['headline']}</h1>
                <p class="text-xl opacity-80 max-w-2xl mx-auto">{copy['descricao']}</p>
            </div>

            <div class="grid md:grid-cols-2 gap-10 items-center">
                <div class="glass p-4 neon-border shadow-2xl">
                    <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=600" class="rounded-xl w-full">
                </div>
                <div class="glass p-10 text-center">
                    <span class="text-green-500 font-bold uppercase tracking-widest text-xs">Oferta Exclusiva Nexus</span>
                    <div class="titulo-master text-8xl my-6">{preco}</div>
                    <a href="{link}" class="btn-venda py-8 text-2xl uppercase shadow-lg">Comprar Agora</a>
                    <div class="flex justify-center gap-4 mt-6 text-xl opacity-60">
                        <i class="fab fa-cc-visa"></i> <i class="fab fa-cc-mastercard"></i> <i class="fab fa-apple-pay"></i> <i class="fas fa-barcode"></i>
                    </div>
                </div>
            </div>

            <div class="grid md:grid-cols-2 gap-10">
                <div class="beneficio-card">
                    <h3 class="titulo-master text-xl mb-4">Principais Benefícios:</h3>
                    <p class="opacity-90">{copy['beneficios']}</p>
                </div>
                <div class="glass p-8">
                    <h3 class="titulo-master text-xl mb-4">Conteúdo do Produto:</h3>
                    <ul class="text-sm">{html_modulos}</ul>
                </div>
            </div>

            <div class="grid md:grid-cols-2 gap-8">
                <div class="glass p-8 italic border-l-4 border-green-500">
                    "Mudou meu jogo. Em 10 dias meu limite subiu 4x. Recomendo muito!"<br><br><strong>- João P., São Paulo</strong>
                </div>
                <div class="glass p-8 flex items-center gap-6">
                    <i class="fas fa-shield-alt text-5xl text-green-500"></i>
                    <div>
                        <h4 class="font-bold uppercase">Garantia Blindada</h4>
                        <p class="text-xs opacity-70">Satisfação garantida ou seu dinheiro de volta em 7 dias. Risco zero para você.</p>
                    </div>
                </div>
            </div>

            <div class="glass p-10">
                <h3 class="titulo-master text-2xl mb-6 text-center italic">Perguntas Frequentes</h3>
                <div class="max-w-2xl mx-auto">{html_faq}</div>
            </div>
            
            <div class="mt-20 p-8 glass text-[10px] opacity-40 border-t border-white/10">
                <p class="mb-4"><b>Termos de Uso e LGPD:</b> Ao adquirir, você aceita nossas cláusulas de responsabilidade e tratamento de dados. Aceitação imediata via checkout seguro Stripe.</p>
            </div>
        </div>"""
    else:
        conteudo_venda = f'<h1 class="titulo-master text-7xl md:text-9xl mb-12 italic">#{tema}</h1><a href="detalhes.html" class="btn-venda py-6 text-xl max-w-sm">ENTRAR NO SISTEMA</a>'

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
        <div class="max-w-6xl mx-auto px-6 py-20">
            <header class="flex justify-between items-center mb-10">
                <a href="index.html" class="text-2xl font-black italic tracking-tighter uppercase">NEXUS<span class="text-green-500">ALPHA</span></a>
                <div class="text-[10px] font-bold uppercase tracking-widest opacity-50">High Conversion System v8.0</div>
            </header>
            
            {conteudo_venda}
            
            <div class="mt-24 pt-16 border-t border-white/10">
                <h3 class="text-white titulo-master text-3xl mb-10 uppercase italic text-center">Protocolos Relacionados</h3>
                <div class="grid md:grid-cols-3 gap-6">{html_relacionados}</div>
            </div>

            <footer class="mt-32 py-10 border-t border-white/10 text-[10px] opacity-40 text-center uppercase tracking-widest font-bold">
                <p>© 2026 Nexus Alpha System - Brasil | Suporte: suporte@nexusalpha.com</p>
                <div class="mt-6 flex justify-center gap-8 font-bold">
                    <a href="privacidade.html" class="hover:text-green-500">Política de Privacidade</a>
                    <a href="termos.html" class="hover:text-green-500">Termos de Uso</a>
                </div>
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
            f.write(gerar_layout_pagina(p['nome'], p['preco'], p['link'], eh_detalhes=True, relacionados=relacionados))
    with open("privacidade.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina("Política de Privacidade", "", "", eh_detalhes=True))
    with open("termos.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina("Termos de Uso", "", "", eh_detalhes=True))

if __name__ == "__main__":
    criar_pagina_vendas("Score 900 Turbo", "https://buy.stripe.com/9B6fZ976y7zJ6qn0jl4c80v")
