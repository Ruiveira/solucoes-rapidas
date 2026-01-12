#!/usr/bin/env python3
import os
import shutil
import subprocess
import sys

print("🚀 DEPLOY FINAL NEXUS ALPHA")
print("=" * 60)

# Configurações
HOME = os.path.expanduser("~")
NEXUS_DIR = os.path.join(HOME, "nexus_alpha")
REPO_DIR = os.path.join(HOME, "Desktop", "solucoes-rapidas")

print(f"Nexus Alpha: {NEXUS_DIR}")
print(f"Repositório: {REPO_DIR}")
print("-" * 60)

# Verificar se nexus_alpha existe
if not os.path.exists(NEXUS_DIR):
    print(f"❌ Pasta não encontrada: {NEXUS_DIR}")
    sys.exit(1)

# Verificar se repositório existe
if not os.path.exists(REPO_DIR):
    print(f"❌ Repositório não encontrado: {REPO_DIR}")
    sys.exit(1)

# Lista de arquivos para copiar
arquivos = [
    ("index.html", "Arquivo principal"),
    ("css", "Estilos"),
    ("js", "JavaScript"),
    ("img", "Imagens")
]

print("📁 Copiando arquivos...")
print("-" * 60)

for arquivo, descricao in arquivos:
    origem = os.path.join(NEXUS_DIR, arquivo)
    destino = os.path.join(REPO_DIR, arquivo)
    
    if not os.path.exists(origem):
        print(f"❌ Não encontrado: {arquivo}")
        continue
    
    try:
        if os.path.isdir(origem):
            if os.path.exists(destino):
                shutil.rmtree(destino)
            shutil.copytree(origem, destino)
        else:
            shutil.copy2(origem, destino)
        
        print(f"✅ {descricao}: {arquivo}")
        
    except Exception as e:
        print(f"❌ Erro ao copiar {arquivo}: {e}")

print("-" * 60)

# Mudar para diretório do repositório
os.chdir(REPO_DIR)

print("📊 Verificando arquivos...")
subprocess.run(["ls", "-la", "index.html", "css", "js", "img"], check=False)

print("\n🚀 Fazendo deploy no GitHub...")
try:
    subprocess.run(["git", "add", "."], check=True)
    print("✅ git add .")
    
    subprocess.run(["git", "commit", "-m", "🚀 Nexus Alpha - Site completo"], check=True)
    print("✅ git commit")
    
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("✅ git push")
    
    print("\n🎉 DEPLOY CONCLUÍDO!")
    
except subprocess.CalledProcessError as e:
    print(f"❌ Erro: {e}")

print("\n" + "=" * 60)
print("🌐 SEU SITE ESTÁ EM:")
print("https://ruiveira.github.io/solucoes-rapidas/")
print("=" * 60)
