def responder_cliente(duvida):
    duvida = duvida.lower()
    if "score" in duvida:
        return "O Score 900 Turbo ensina os gatilhos para aumentar seu crédito rápido. Custa apenas R$ 19,90 aqui: https://buy.stripe.com/9B6fZ976y7zJ6qn0jl4c80v"
    elif "renda" in duvida:
        return "O método Renda Extra foca em ganhos diários pelo celular. R$ 19,90 no link: https://buy.stripe.com/9B6fZ976y7zJ6qn0jl4c80v"
    elif "planilha" in duvida:
        return "A Planilha de Lucros organiza sua vida financeira e projeta ganhos. Garanta a sua: https://buy.stripe.com/9B6fZ976y7zJ6qn0jl4c80v"
    else:
        return "Olá! Sou a IA do Nexus Alpha. Qual dos nossos protocolos você deseja dominar hoje? Todos estão por R$ 19,90."

# Exemplo de uso: print(responder_cliente("Como funciona o score?"))
