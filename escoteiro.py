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
        a {{ transition: 0.3s; }}
        .conteudo-legal h2 {{ color: #39FF14; font-family: 'Montserrat', sans-serif; text-transform: uppercase; margin-top: 2rem; margin-bottom: 1rem; font-size: 1.25rem; }}
        .conteudo-legal p {{ margin-bottom: 1rem; opacity: 0.8; line-height: 1.6; }}
    </style>
    """

def obter_conteudo_legal(tipo):
    if tipo == "privacidade":
        return """
        <h2>1. Informações sobre o Controlador</h2><p>Nexus Alpha System, operando sob a legislação brasileira. Contato: suporte@nexusalpha.com</p>
        <h2>2. Tipos de Dados Coletados</h2><p>Coletamos nome, e-mail e dados de navegação via cookies para melhorar sua experiência. Dados de pagamento são processados de forma segura pelo Stripe.</p>
        <h2>3. Finalidade e Base Legal</h2><p>Os dados são utilizados para execução de contrato (entrega do produto digital) e cumprimento de obrigações legais em conformidade com a LGPD.</p>
        <h2>4. Direitos dos Titulares</h2><p>Você tem direito ao acesso, correção e eliminação de seus dados a qualquer momento, conforme garantido pela Lei Geral de Proteção de Dados.</p>
        <h2>5. Segurança</h2><p>Utilizamos criptografia de ponta e medidas administrativas rigorosas para proteger suas informações contra acessos não autorizados.</p>
        """
    else:
        return """
        <h2>1. Aceitação dos Termos</h2><p>Ao acessar este site, você concorda em cumprir estes termos de serviço e todas as leis aplicáveis no território brasileiro.</p>
        <h2>2. Uso de Licença</h2><p>É concedida permissão para baixar temporariamente uma cópia dos materiais para visualização pessoal e não comercial.</p>
        <h2>3. Responsabilidades</h2><p>O usuário é responsável pelo uso ético da plataforma. A Nexus Alpha não se responsabiliza por mau uso dos métodos ensinados.</p>
        <h2>4. Propriedade Intelectual</h2><p>Todo conteúdo, logotipos e textos são de propriedade exclusiva da Nexus Alpha, protegidos por direitos autorais.</p>
        <h2>5. Foro</h2><p>Fica eleito o foro da comarca da sede da empresa para dirimir quaisquer controvérsias oriundas deste contrato.</p>
        """

def gerar_layout_pagina(tema, preco, link, eh_detalhes=False, relacionados=[], legal_type=None):
    # Lógica de Relacionados (Sempre 3)
    html_relacionados = ""
    if relacionados:
        for p in relacionados:
            html_relacionados += f'''
            <a href="{p['slug']}.html" class="glass p-8 block hover:bg-white/10 transition-all text-center border border-white/5">
                <h4 class="titulo-master text-lg mb-2 italic">{p['nome']}</h4>
                <p class="text-white font-bold text-2xl">{p['preco']}</p>
                <span class="text-[10px] uppercase opacity-50 mt-4 block">Acessar Agora</span>
            </a>'''

    secao_relacionados = f"""
    <div class="mt-32 pt-16 border-t border-white/10">
        <h3 class="text-white titulo-master text-3xl mb-10 uppercase italic text-center">Protocolos Relacionados</h3>
        <div class="grid md:grid-cols-3 gap-6">{html_relacionados}</div>
    </div>""" if (eh_detalhes and relacionados) else ""

    # Conteúdo Principal
    conteudo = ""
    if legal_type:
        conteudo = f'<div class="glass p-10 conteudo-legal"><h1 class="titulo-master text-4xl mb-8">#{tema}</h1>{obter_conteudo_legal(legal_type)}</div>'
    elif eh_detalhes:
        conteudo = f"""
        <div class="mt-16 space-y-12">
            <div class="text-center">
                <h2 class="titulo-master text-4xl md:text-6xl mb-4 italic">#{tema}</h2>
                <div class="glass p-4 inline-block neon-border mt-6"><img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=500" class="rounded-xl"></div>
            </div>
            <div class="glass p-12 text-center neon-border">
                <div class="titulo-master text-8xl my-8">{preco}</div>
                <a href="{link}" class="btn-venda py-8 text-2xl uppercase">ADQUIRIR AGORA</a>
                <div class="flex justify-center gap-6 mt-6 text-2xl opacity-70">
                    <i class="fab fa-cc-visa"></i> <i class="fab fa-cc-mastercard"></i> <i class="fab fa-apple-pay"></i> <i class="fas fa-barcode"></i>
                </div>
            </div>
        </div>
        """
    else:
        conteudo = f'<h1 class="titulo-master text-7xl md:text-9xl mb-12 italic">#{tema}</h1><a href="detalhes.html" class="btn-venda py-6 text-xl max-w-md">ENTRAR NO SISTEMA</a>'

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
                <a href="index.html" class="text-2xl font-black italic tracking-tighter">NEXUS<span class="text-green-500">ALPHA</span></a>
                <div class="text-[10px] font-bold uppercase tracking-widest opacity-50">Market Intelligence v5.0</div>
            </header>
            
            {conteudo}
            {secao_relacionados}

            <footer class="mt-40 py-10 border-t border-white/10 text-[10px] opacity-50 text-center uppercase tracking-widest">
                <p>© 2026 Nexus Alpha System - Brasil</p>
                <div class="mt-4 flex justify-center gap-6">
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
    
    # Base de dados fixa para garantir relacionados
    relacionados = [
        {"nome": "Score 900 Turbo", "preco": preco_final, "slug": "score", "link": link_venda},
        {"nome": "Renda Extra", "preco": preco_final, "slug": "renda", "link": link_venda},
        {"nome": "Planilha Lucros", "preco": preco_final, "slug": "planilha", "link": link_venda}
    ]

    # 1. Index e Detalhes
    with open("index.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina(tema, preco_final, "detalhes.html"))
    with open("detalhes.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina(tema, preco_final, link_venda, eh_detalhes=True, relacionados=relacionados))
    
    # 2. Produtos Individuais (Garantindo que apareçam 3 relacionados)
    for p in relacionados:
        with open(f"{p['slug']}.html", "w", encoding="utf-8") as f:
            f.write(gerar_layout_pagina(p['nome'], p['preco'], p['link'], eh_detalhes=True, relacionados=relacionados))

    # 3. Páginas Legais
    with open("privacidade.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina("Política de Privacidade", "", "", legal_type="privacidade"))
    with open("termos.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina("Termos de Uso", "", "", legal_type="termos"))

if __name__ == "__main__":
    criar_pagina_vendas("Score 900 Turbo", "https://buy.stripe.com/9B6fZ976y7zJ6qn0jl4c80v")
