import stripe

# COLOQUE SUA CHAVE DA STRIPE ENTRE AS ASPAS ABAIXO
stripe.api_key = ""

def criar_produto_e_link(nome_da_demanda):
    try:
        # Cria um produto automático baseado na busca do Google
        produto = stripe.Product.create(
            name=f"Acesso Premium: {nome_da_demanda}",
            description=f"Solução completa e automatizada para {nome_da_demanda}."
        )

        # Cria um preço de R$ 10,00 (1000 centavos)
        preco = stripe.Price.create(
            unit_amount=1000,
            currency="brl",
            product=produto.id,
        )

        # Cria o link que o cliente vai clicar para pagar
        link_pagamento = stripe.PaymentLink.create(
            line_items=[{"price": preco.id, "quantity": 1}]
        )

        return link_pagamento.url
    except Exception as e:
        return f"Erro na Stripe: {e}"

if __name__ == "__main__":
    # Teste rápido:
    print("Gerando link de teste para 'Calculadora de Rescisão'...")
    url = criar_produto_e_link("Calculadora de Rescisão")
    print(f"LINK DE PAGAMENTO GERADO: {url}")