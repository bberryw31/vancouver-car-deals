import requests
from bs4 import BeautifulSoup

url = 'https://www.vanchosun.com/market/main/frame.php?main=cardealer'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

listings = soup.find_all('div', style="position: relative; margin: 1px; width: 190px; border: 1px solid #F5F5F5; border-radius: 4px;")

cars = []
for listing in listings:
    car_name_div = listing.find('div', style="margin: 4px 0; height: 23px; font-size: 12px; overflow: hidden;")

    if car_name_div:
        car_name = car_name_div.text.strip()
    else:
        print("Car name not found for this listing, skipping.")
        continue

    price_div = listing.find('div', style="margin: 4px 0; font-weight: 700; overflow: hidden;")

    if price_div:
        price_raw = price_div.text.strip()
        price = int(price_raw.replace('$', '').replace(',', ''))
    else:
        print("Price not found for this listing, skipping.")
        continue

    if price < 25000:
        cars.append({
            'Car Name': car_name,
            'Price': price
        })

for car in cars:
    print(f"Car: {car['Car Name']}, Price: {car['Price']}")
