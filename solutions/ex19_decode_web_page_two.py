import requests
from bs4 import BeautifulSoup

url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"

# 1. Sayfayı çek (User-Agent ile)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
response = requests.get(url, headers=headers)
response.raise_for_status()

# 2. BeautifulSoup ile ayrıştır
soup = BeautifulSoup(response.text, features="html.parser")

# 3. Makale metnini bul 
# <article> etiketi içindeki tüm <p> paragrafları
paragraphs = soup.select('article p')

# 4. Paragrafları ekrana yazdır
if paragraphs:
    for p in paragraphs:
        print(p.get_text(strip=True))
        print()  # Paragraflar arasına boş satır
else:
    print("Makale metni bulunamadı. Sayfa yapısı değişmiş olabilir.")