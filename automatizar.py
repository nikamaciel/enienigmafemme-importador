import os

print("⏳ Mineração dos produtos em andamento...")
os.system("python minerar_kaisan.py")

print("⏳ Importação dos produtos para Shopify em andamento...")
os.system("python importar_shopify.py")

print("🚀 Processo concluído!")
