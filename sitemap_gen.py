import datetime

def gerar_sitemap():
    url_base = "https://seu-dominio.github.io" # O robô ajusta isso via SEO tags
    paginas = ["index.html", "detalhes.html", "score.html", "renda.html", "planilha.html"]
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d")
    
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for pg in paginas:
        sitemap_content += f'  <url>\n    <loc>{url_base}/{pg}</loc>\n    <lastmod>{data_atual}</lastmod>\n    <priority>{"1.0" if pg == "index.html" else "0.8"}</priority>\n  </url>\n'
    
    sitemap_content += '</urlset>'
    
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("--- NEXUS SEO: Sitemap.xml gerado com sucesso para tráfego orgânico ---")

if __name__ == "__main__":
    gerar_sitemap()
