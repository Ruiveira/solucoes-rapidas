import stripe
import os
from dotenv import load_dotenv

# Carrega a chave do arquivo .env
load_dotenv()
stripe.api_key = os.getenv("STRIPE_API_KEY")

def criar_produto_e_link(nome_da_demanda):
    try:
        produto = stripe.Product.create(
            name=f"Acesso Premium: {nome_da_demanda}",
            description=f"Solução completa para {nome_da_demanda}."
        )

        preco = stripe.Price.create(
            unit_amount=1000,
            currency="brl",
            product=produto.id,
        )

        link_pagamento = stripe.PaymentLink.create(
            line_items=[{"price": preco.id, "quantity": 1}]
        )

        return link_pagamento.url
    except Exception as e:
        return f"Erro na Stripe: {e}"

if __name__ == "__main__":
    print("Testando geração de link com chave protegida...")
    url = criar_produto_e_link("Teste de Fluxo")
    print(f"LINK GERADO: {url}")