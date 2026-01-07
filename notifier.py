import requests

def enviar_notificacao(mensagem):
    token = "8445235516:AAEXsenEi3luT5CdhRygima_v9Sxe2jx_UM" # COLOQUE O TOKEN DO BOTFATHER AQUI
    chat_id = "NexusAlpha2026_Bot" # COLOQUE SEU ID DO TELEGRAM AQUI
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={mensagem}"
    requests.get(url)

# Para descobrir seu CHAT_ID, mande um oi para o bot @userinfobot no Telegram
