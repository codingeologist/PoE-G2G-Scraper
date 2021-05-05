import os
import time
import requests
import numpy as np
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup as bs

def get_data(url):

    html = requests.get(url).content
    
    unicode_str = html.decode('utf8')
    encoded_str = unicode_str.encode('ascii','ignore')
    soup = bs(encoded_str, 'lxml')
    dt = datetime.now()
    
    tag_name = []
    tag_text = []
    soup_date = []
    for tag in soup.find_all('span', class_='products__exch-rate input-gold'):
        tag_name.append(tag.name)
        tag_text.append(float(tag.text.split('£',1)[1]))
        soup_date.append(dt)
    
    prices = np.array(tag_text)
    soup_date_0 = [soup_date[0]]
    min_price = [np.min(prices)]
    max_price = [np.max(prices)]
    std_price = [np.std(prices)]
    df1 = pd.DataFrame(zip(soup_date, prices), columns=['timestamp', 'price'])
    df2 = pd.DataFrame(zip(soup_date_0, min_price, max_price, std_price), columns=['timestamp', 'min price', 'max price', 'deviation'])
    
    return df1, df2

def main():
    
    url = 'https://www.g2g.com/path-of-exile-global/Item-19398-19400?item_type=24296&server=40554&sorting=lowest_price'
    
    df1, df2 = get_data(url)
    
    if not os.path.isfile('full_price_chart.csv'):
        df1.to_csv('full_price_chart.csv', header=True, index=False)
    else:
        df1.to_csv('full_price_chart.csv', mode='a', header=False, index=False)

    if not os.path.isfile('price_summary.csv'):
        df2.to_csv('price_summary.csv', header=True, index=False)
    else:
        df2.to_csv('price_summary.csv', mode='a', header=False, index=False)
        
if __name__ == '__main__':
    
    main()