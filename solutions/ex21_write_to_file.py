from bs4 import BeautifulSoup
import requests

open_file = open('file_to_save.txt', 'w')

def get_gundem_titles():
    url = "https://eksisozluk.com/"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Gündem bölümünü bul
        index_section = soup.find('div', id='index-section')
        if not index_section:
            return []
        
        # Topic list'i bul
        topic_list = index_section.find('ul', class_='topic-list')
        if not topic_list:
            return []
        
        titles = []
        
        for li in topic_list.find_all('li'):
            # Reklam/sponsored içerikleri filtrele
            li_id = li.get('id', '')
            if 'sponsored' in li_id or 'nativespot' in li_id:
                continue
            
            a_tag = li.find('a')
            if not a_tag:
                continue
            
            # Başlık metnini al (small tag'ini içermez)
            title = a_tag.get_text(strip=True)
            
            # Entry sayısını al 
            small = a_tag.find('small')
            entry_count = small.get_text(strip=True) if small else None
            
            if title and len(title) > 2:
                titles.append({
                    'title': title,
                    'entry_count': entry_count
                })
        with open('file_to_save.txt', 'w', encoding='utf-8') as f:
            for item in titles:
                f.write(f"{item['title']}")
                if item['entry_count']:
                    f.write(f" ({item['entry_count']} entry)")
                    f.write("\n") 
        return titles
       
    except Exception as e:
        print(f"Hata: {e}")
        return []

# Ana program
if __name__ == "__main__":
    titles = get_gundem_titles()
    
    if titles:
        print(f"\n📰 GÜNDEM - {len(titles)} başlık\n")
        print("=" * 70)
        for i, item in enumerate(titles, 1):
            count_info = f" ({item['entry_count']} entry)" if item['entry_count'] else ""
            print(f"{i:2}. {item['title']}{count_info}")
    else:
        print("❌ Gündem başlıkları bulunamadı.")

open_file.close()