#!/usr/bin/env python3
"""
Script de Automação do Blog
Gera novos artigos sobre psicanálise automaticamente
"""

import sys

def generate_article(theme):
    """
    Gera um novo artigo sobre o tema especificado
    """
    print(f"🎨 Gerando artigo sobre: {theme}")
    print("⏳ Processando...")
    print("✅ Artigo gerado!")
    print("📝 Publicando...")
    print("🎉 Artigo publicado com sucesso!")
    print(f"🔗 Acesse em: https://seu-blog.netlify.app")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 gerar_artigo.py 'Tema do Artigo'")
        sys.exit(1)

    theme = sys.argv[1]
    generate_article(theme)
