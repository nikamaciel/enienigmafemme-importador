import requests
import csv

# Definir as credenciais da API do Shopify
SHOPIFY_STORE = "https://enigmafemme.myshopify.com"
API_KEY = "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"
PASSWORD = "Enigm@2025Ana"

# URL da API do Shopify para criar produtos
url = f"{SHOPIFY_STORE}/admin/api/2023-10/products.json"

# Headers de autenticação
headers = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": PASSWORD
}

# Ler os produtos extraídos do CSV
with open("produtos_kaisan.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Pular o cabeçalho

    for row in reader:
        title, price, image, link = row  # Pegar os dados do CSV

        #  Criar o JSON do produto para enviar ao Shopify
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

        # Enviar requisição para criar o produto
        response = requests.post(url, json=product_data, headers=headers)

        if response.status_code == 201:
            print(f"✅ Produto '{title}' importado com sucesso!")
        else:
            print(f"❌ Erro ao importar '{title}':", response.text)
