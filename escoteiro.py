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
        .conteudo-legal h2 {{ color: #39FF14; font-family: 'Montserrat', sans-serif; text-transform: uppercase; margin-top: 2.5rem; margin-bottom: 1rem; font-size: 1.4rem; border-bottom: 1px solid rgba(57, 255, 20, 0.2); padding-bottom: 0.5rem; }}
        .conteudo-legal p, .conteudo-legal li {{ margin-bottom: 1rem; opacity: 0.8; line-height: 1.8; text-align: justify; }}
        .conteudo-legal ul {{ list-style-type: disc; margin-left: 1.5rem; margin-bottom: 1.5rem; }}
    </style>
    """

def obter_conteudo_privacidade_completo():
    return """
    <h2>1. Informações sobre o Controlador dos Dados</h2>
    <p>A Nexus Alpha System, como controladora, é responsável pelo tratamento dos seus dados pessoais. Contato via: suporte@nexusalpha.com. Nosso Encarregado de Dados (DPO) pode ser contatado pelo mesmo endereço.</p>
    <h2>2. Tipos de Dados Coletados</h2>
    <p><b>Dados Pessoais:</b> Coletamos nome e e-mail no ato da compra. <b>Dados de Navegação:</b> IP, tipo de navegador e páginas visitadas. Não coletamos dados sensíveis conforme definido pela LGPD.</p>
    <h2>3. Finalidade e Base Legal</h2>
    <p>Os dados são coletados para: Execução de Contrato (processar sua compra), Legítimo Interesse (melhorar o site) e Cumprimento de Obrigação Legal (emissão de recibos).</p>
    <h2>4. Compartilhamento de Informações</h2>
    <p>Seus dados são compartilhados com o <b>Stripe</b> para processamento de pagamentos. Não vendemos seus dados para terceiros.</p>
    <h2>5. Direitos dos Titulares (LGPD)</h2>
    <ul>
        <li>Confirmação da existência de tratamento;</li>
        <li>Acesso e correção de dados;</li>
        <li>Eliminação ou portabilidade dos dados;</li>
        <li>Revogação do consentimento.</li>
    </ul>
    <h2>6. Armazenamento e Segurança</h2>
    <p>Mantemos seus dados pelo período necessário para a prestação do serviço. Utilizamos criptografia SSL e servidores seguros.</p>
    <h2>7. Uso de Cookies</h2>
    <p>Utilizamos cookies de análise para entender as tendências do mercado (retenção de 3-7s) em sites de terceiros para aprimorar nossos algoritmos.</p>
    <h2>8. Atualizações e Foro</h2>
    <p>Esta política é regida pelas leis brasileiras. Qualquer disputa será resolvida no foro da nossa sede administrativa.</p>
    """

def obter_conteudo_termos_completo():
    return """
    <h2>1. Aceitação dos Termos</h2>
    <p>Ao utilizar a plataforma Nexus Alpha, você concorda automaticamente com estes termos. Se não concordar, deve cessar o uso imediatamente.</p>
    <h2>2. Descrição do Serviço e Requisitos</h2>
    <p>Oferecemos protocolos digitais de alta performance financeira. O acesso requer idade mínima de 18 anos e cadastro válido.</p>
    <h2>3. Responsabilidades</h2>
    <p><b>Do Usuário:</b> Proibido hacking, distribuição de malware ou uso de robôs para extrair dados da nossa página. <b>Da Empresa:</b> Não nos responsabilizamos por falhas externas de internet ou ganhos não garantidos.</p>
    <h2>4. Propriedade Intelectual</h2>
    <p>Todos os logotipos, textos e o código "Escoteiro" são propriedade da Nexus Alpha. Proibida cópia total ou parcial sob pena de lei.</p>
    <h2>5. Preços e Pagamentos (E-commerce)</h2>
    <p>Aceitamos Cartões Visa, Master, Apple Pay e Boleto via Stripe. Os preços estão sujeitos a alteração sem aviso prévio.</p>
    <h2>6. Política de Reembolso e Devolução</h2>
    <p>Em conformidade com o <b>Código de Defesa do Consumidor</b>, oferecemos garantia incondicional de 7 dias para produtos digitais.</p>
    <h2>7. Entrega e Prazos</h2>
    <p>A entrega é digital e imediata via e-mail após a confirmação do pagamento pelo processador.</p>
    <h2>8. Modificações e Foro</h2>
    <p>Reservamos o direito de alterar estes termos. Este contrato é regido pela legislação brasileira. Foro eleito: Comarca da Sede.</p>
    """

def gerar_layout_pagina(tema, preco, link, eh_detalhes=False, relacionados=[], legal_type=None):
    # Lógica de Relacionados (Fixada em 3)
    html_relacionados = ""
    if relacionados:
        for p in relacionados:
            html_relacionados += f'''
            <a href="{p['slug']}.html" class="glass p-8 block hover:bg-white/10 transition-all text-center border border-white/5">
                <h4 class="titulo-master text-lg mb-2 italic" style="color: #39FF14">{p['nome']}</h4>
                <p class="text-white font-bold text-2xl">{p['preco']}</p>
                <span class="text-[10px] uppercase opacity-50 mt-4 block">Acessar Sistema</span>
            </a>'''

    secao_relacionados = f"""
    <div class="mt-32 pt-16 border-t border-white/10">
        <h3 class="text-white titulo-master text-3xl mb-10 uppercase italic text-center">Protocolos Relacionados</h3>
        <div class="grid md:grid-cols-3 gap-6">{html_relacionados}</div>
    </div>""" if (eh_detalhes and relacionados) else ""

    # Lógica de Conteúdo por Tipo
    conteudo_final = ""
    if legal_type == "privacidade":
        conteudo_final = f'<div class="glass p-12 conteudo-legal"><h1 class="titulo-master text-4xl mb-10 italic">#{tema}</h1>{obter_conteudo_privacidade_completo()}</div>'
    elif legal_type == "termos":
        conteudo_final = f'<div class="glass p-12 conteudo-legal"><h1 class="titulo-master text-4xl mb-10 italic">#{tema}</h1>{obter_conteudo_termos_completo()}</div>'
    elif eh_detalhes:
        conteudo_final = f"""
        <div class="mt-16 space-y-12">
            <div class="text-center">
                <h2 class="titulo-master text-6xl md:text-8xl mb-4 italic">#{tema}</h2>
                <div class="glass p-4 inline-block neon-border mt-10"><img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=500" class="rounded-xl"></div>
            </div>
            <div class="glass p-12 text-center neon-border">
                <div class="titulo-master text-8xl my-8">{preco}</div>
                <a href="{link}" class="btn-venda py-8 text-2xl uppercase">ADQUIRIR AGORA</a>
                <div class="flex justify-center gap-6 mt-6 text-2xl opacity-70">
                    <i class="fab fa-cc-visa"></i> <i class="fab fa-cc-mastercard"></i> <i class="fab fa-apple-pay"></i> <i class="fas fa-barcode"></i>
                </div>
                <p class="text-[10px] mt-6 opacity-40 uppercase tracking-widest text-white">Processamento Seguro Stripe</p>
            </div>
        </div>"""
    else:
        conteudo_final = f'<h1 class="titulo-master text-7xl md:text-9xl mb-12 italic">#{tema}</h1><a href="detalhes.html" class="btn-venda py-6 text-xl max-w-sm">ENTRAR NO SISTEMA</a>'

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
                <div class="text-[10px] font-bold uppercase tracking-widest opacity-50">Market Intelligence v6.0</div>
            </header>
            
            {conteudo_final}
            {secao_relacionados}

            <footer class="mt-40 py-10 border-t border-white/10 text-[10px] opacity-50 text-center uppercase tracking-[0.2em]">
                <p>© 2026 Nexus Alpha System - Brasil</p>
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
    with open("privacidade.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina("Política de Privacidade", "", "", legal_type="privacidade"))
    with open("termos.html", "w", encoding="utf-8") as f: f.write(gerar_layout_pagina("Termos de Uso", "", "", legal_type="termos"))

if __name__ == "__main__":
    criar_pagina_vendas("Score 900 Turbo", "https://buy.stripe.com/9B6fZ976y7zJ6qn0jl4c80v")
