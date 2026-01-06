from escoteiro import buscar_demandas
from arquiteto import criar_produto_e_link

def iniciar_sistema():
    print("--- INICIANDO SISTEMA AUTÔNOMO NEXUS-ALPHA ---")
    
    # 1. Descobre a dor do mercado via Google
    ideias = buscar_demandas()
    if not ideias:
        print("Nenhuma demanda encontrada agora.")
        return
    
    # Pegamos a primeira ideia da lista (ex: 'como calcular rescisão')
    escolhida = ideias[0]
    print(f"Ideia escolhida para monetizar: {escolhida}")
    
    # 2. Gera o link de pagamento na sua Stripe automaticamente
    print("Gerando infraestrutura de pagamento...")
    link_venda = criar_produto_e_link(escolhida)
    
    # 3. Cria a página de vendas (O seu site index.html)
    html_vendas = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Solução para {escolhida}</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; padding: 50px; background-color: #f4f7f9; }}
            .card {{ background: white; padding: 40px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); display: inline-block; max-width: 500px; }}
            h1 {{ color: #333; }}
            p {{ color: #666; font-size: 1.1em; }}
            .btn {{ background: #6772E5; color: white; padding: 18px 30px; text-decoration: none; border-radius: 8px; font-weight: bold; display: inline-block; margin-top: 20px; transition: background 0.3s; }}
            .btn:hover {{ background: #5469d4; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Precisa de {escolhida}?</h1>
            <p>Nossa inteligência gerou uma solução exclusiva e simplificada para resolver isso agora mesmo.</p>
            <a href="{link_venda}" class="btn">OBTER SOLUÇÃO PREMIUM</a>
        </div>
    </body>
    </html>
    """
    
    # Salva o site no seu MacBook
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_vendas)
    
    print(f"--- SUCESSO! ---")
    print(f"1. Produto: {escolhida}")
    print(f"2. Link Stripe: {link_venda}")
    print(f"3. Arquivo 'index.html' criado na pasta nexus_alpha.")

if __name__ == "__main__":
    iniciar_sistema()