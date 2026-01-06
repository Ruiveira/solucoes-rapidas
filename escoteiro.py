def criar_pagina_vendas(tema, link_stripe):
    # O robô gera palavras-chave automáticas para o Google te achar (Tráfego Orgânico)
    keywords = f"{tema}, solução rápida, como resolver {tema}, guia passo a passo, oficial"
    
    html = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="A solução definitiva para {tema}. Acesse agora.">
        <meta name="keywords" content="{keywords}">
        <title>OFICIAL: {tema}</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-slate-900 flex items-center justify-center min-h-screen p-6 font-sans">
        <div class="max-w-md w-full bg-white rounded-[2.5rem] shadow-[0_35px_60px_-15px_rgba(0,0,0,0.5)] p-10 text-center border-t-8 border-indigo-600">
            <span class="bg-indigo-100 text-indigo-700 text-xs font-bold px-3 py-1 rounded-full uppercase tracking-widest">Acesso Exclusivo</span>
            <h1 class="text-3xl font-black text-slate-900 mt-4 mb-4 leading-tight">
                Resolva agora: <br><span class="text-indigo-600">{tema}</span>
            </h1>
            <p class="text-slate-500 mb-8 text-base leading-relaxed">
                Nossa IA identificou que você precisa de uma solução para <b>{tema}</b>. Libere o acesso ao guia prático e automatizado.
            </p>
            <a href="{link_stripe}" class="inline-block w-full bg-indigo-600 hover:bg-indigo-700 text-white font-black py-5 px-6 rounded-2xl transition-all transform hover:scale-105 shadow-xl shadow-indigo-300 text-xl tracking-tight">
                QUERO ESSA SOLUÇÃO →
            </a>
            <div class="mt-8 flex justify-center gap-2">
                <div class="h-1 w-12 bg-slate-200 rounded-full"></div>
                <div class="h-1 w-12 bg-indigo-600 rounded-full"></div>
                <div class="h-1 w-12 bg-slate-200 rounded-full"></div>
            </div>
        </div>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)