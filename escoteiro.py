def criar_pagina_vendas(tema, link_stripe):
    html = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SISTEMA VALIDADO: {tema}</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            .btn-vendas {{
                background: linear-gradient(90deg, #4f46e5, #06b6d4);
                box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.4);
                transition: all 0.3s ease;
            }}
            .btn-vendas:hover {{ transform: scale(1.02); brightness: 1.1; }}
        </style>
    </head>
    <body class="bg-[#050505] text-slate-200 font-sans">
        <div class="max-w-2xl mx-auto px-6 py-20 text-center">
            <div class="inline-block bg-green-500/20 text-green-400 border border-green-500/30 px-4 py-1 rounded-full text-xs font-bold mb-6">
                ● ACESSO DISPONÍVEL AGORA
            </div>
            
            <h1 class="text-4xl md:text-6xl font-black text-white mb-6 leading-tight tracking-tighter">
                Descubra o Protocolo: <br>
                <span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-cyan-400 uppercase">
                    {tema}
                </span>
            </h1>

            <p class="text-xl text-slate-400 mb-10 leading-relaxed">
                Este não é mais um curso. É o <span class="text-white font-bold">Método Direto</span> para você dominar {tema} e obter resultados imediatos, sem perder tempo com teorias inúteis.
            </p>

            <div class="bg-slate-900/50 border border-slate-800 p-8 rounded-3xl mb-10">
                <ul class="text-left space-y-4 mb-8">
                    <li class="flex items-center gap-3">✅ <span class="text-slate-300 font-medium">Acesso Vitalício e Imediato</span></li>
                    <li class="flex items-center gap-3">✅ <span class="text-slate-300 font-medium">Material 100% Prático e Direto</span></li>
                    <li class="flex items-center gap-3">✅ <span class="text-slate-300 font-medium">Garantia de Satisfação Total</span></li>
                </ul>
                
                <a href="{link_stripe}" class="btn-vendas block w-full text-white font-black py-6 rounded-2xl text-2xl uppercase tracking-tighter">
                    ADQUIRIR AGORA →
                </a>
                <p class="mt-4 text-xs text-slate-500 italic">Oferta válida apenas para o tráfego orgânico de hoje.</p>
            </div>

            <div class="flex justify-center items-center gap-8 opacity-40">
                <img src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Stripe_Logo%2C_revised_2016.svg" class="h-6 filter grayscale brightness-200" alt="Stripe">
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a4/SSL_Certified_Logo.png" class="h-10 filter grayscale brightness-200" alt="SSL">
            </div>
        </div>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
