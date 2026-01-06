import random
import arquiteto
import escoteiro
import os

# Lista expandida para o robô variar os produtos sozinho
temas_lucrativos = [
    "Como calcular decimo terceiro", "Guia de Declaração de IR 2026", 
    "Planilha de Orçamento Familiar", "Modelo de Contrato de Freelancer",
    "Guia de Investimento em Renda Fixa", "Como sair do cheque especial",
    "Checklist de Viagem Internacional", "Modelo de Currículo para Tecnologia",
    "Como vender no Instagram do zero", "Guia de Organização Doméstica",
    "Dieta de 21 dias para Iniciantes", "Treino de Casa sem Equipamentos",
    "Como criar um CNPJ MEI", "Direitos do Consumidor: Guia Prático",
    "Marketing Digital para Pequenos Negócios", "Guia de SEO para Blogs",
    "Como tirar o Passaporte passo a passo", "Planejamento de Aposentadoria",
    "Como negociar aumento de salário", "Guia de Importação Legal"
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
