import requests
from bs4 import BeautifulSoup
from typing import Dict, Optional

class PriceScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
    
    def get_price(self, url: str) -> Optional[float]:
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            # Ejemplo para Amazon (necesitarás ajustar selectores)
            price_span = soup.select_one('span.a-price span')
            if price_span:
                return float(price_span.text.strip().replace('$', '').replace(',', ''))
            return None
        except Exception as e:
            print(f"Error scraping {url}: {str(e)}")
            return None