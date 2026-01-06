import random
import arquiteto
import escoteiro
import os

# Temas filtrados pela maior probabilidade de venda rápida e fácil (Impulso)
temas_venda_rapida = [
    "Como calcular decimo terceiro", "Guia: Sair das Dividas em 30 dias",
    "Planilha Financeira Automática", "Como aumentar seu Score de Crédito",
    "Ganhar dinheiro com Milhas", "Manual do Reembolso de Impostos",
    "Aposentadoria Antecipada: O Guia", "Direitos Trabalhistas: Guia Urgente"
]

def rodar_sistema():
    print("--- SISTEMA NEXUS-ALPHA: MODO ALTA CONVERSÃO ---")
    # O robô sempre escolhe o tema com foco em dor financeira imediata
    tema = random.choice(temas_venda_rapida)
    print(f"Produto de Alta Probabilidade: {tema}")
    link = arquiteto.criar_produto_e_link(tema)
    escoteiro.criar_pagina_vendas(tema, link)
    print(f"--- SUCESSO! Robô escolheu e publicou: {tema} ---")

if __name__ == "__main__":
    rodar_sistema()