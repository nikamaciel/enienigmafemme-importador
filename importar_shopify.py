import requests
import csv
import os
from dotenv import load_dotenv

# 🔹 Carregar as variáveis do arquivo .env
load_dotenv()

SHOPIFY_STORE = os.getenv("SHOPIFY_STORE")
API_KEY = os.getenv("SHOPIFY_API_KEY")
PASSWORD = os.getenv("SHOPIFY_PASSWORD")

# 🔹 URL da API do Shopify
url = f"{SHOPIFY_STORE}/admin/api/2023-10/products.json"

# 🔹 Headers para autenticação
headers = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": PASSWORD
}

# 🔹 Ler os produtos do CSV e enviá-los ao Shopify
with open("produtos_kaisan.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Pular o cabeçalho

    for row in reader:
        title, price, image, link = row  

        product_data = {
            "product": {
                "title": title,
                "body_html": f"<p>Produto da Kaisan. Veja mais detalhes <a href='{link}'>aqui</a></p>",
                "vendor": "Kaisan",
                "product_type": "Fitness",
                "variants": [{"price": price}],
                "images": [{"src": image}]
            }
        }

        response = requests.post(url, json=product_data, headers=headers)

        if response.status_code == 201:
            print(f"✅ Produto '{title}' importado com sucesso!")
        else:
            print(f"❌ Erro ao importar '{title}':", response.text)
