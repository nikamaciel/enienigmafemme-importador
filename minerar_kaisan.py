import requests
from bs4 import BeautifulSoup
import csv

# URL da página de produtos da Kaisan
url = "https://www.kaisan.com.br/produtos"

# Fazer a requisição HTTP
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Abrir arquivo CSV para salvar os dados
with open("produtos_kaisan.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["título", "preço", "imagem", "link"])  # Cabeçalhos

    # Encontrar todos os produtos na página
    produtos = soup.find_all("div", class_="produto")  # Ajustar para a classe correta do site

    for produto in produtos:
        titulo = produto.find("h2").text.strip()
        preco = produto.find("span", class_="preco").text.strip()
        imagem = produto.find("img")["src"]
        link = produto.find("a")["href"]

        # Salvar no CSV
        writer.writerow([titulo, preco, imagem, link])

print("✅ Produtos extraídos com sucesso para produtos_kaisan.csv!")

