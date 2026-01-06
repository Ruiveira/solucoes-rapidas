import random
import arquiteto
import escoteiro
import os

temas_lucrativos = [
    "Como calcular decimo terceiro",
    "Planilha de Gastos Mensais 2026",
    "Guia de Declaração de Imposto de Renda",
    "Como sair das dívidas rapidamente",
    "Modelo de Contrato de Aluguel Profissional",
    "Guia de Investimento para Iniciantes"
]

def rodar_sistema():
    print("--- INICIANDO SISTEMA NEXUS-ALPHA ---")
    tema = random.choice(temas_lucrativos)
    print(f"Ideia do dia: {tema}")
    link = arquiteto.criar_produto_e_link(tema)
    escoteiro.criar_pagina_vendas(tema, link)
    print(f"--- SUCESSO! Site atualizado com: {tema} ---")

if __name__ == "__main__":
    rodar_sistema()
