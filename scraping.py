import scrapy
import pandas as pd
import re



class FootballSpider(scrapy.Spider):
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    name = "Football"
    start_urls = ["https://www.transfermarkt.world/spieler-statistik/wertvollstespieler/marktwertetop/plus/0/galerie/0?ausrichtung=alle&spielerposition_id=alle&altersklasse=alle&jahrgang=0&land_id=0&kontinent_id=0&yt0=%D0%9F%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D1%8C"]


    def parse(self, response):
        # Используем CSS-селекторы для извлечения данных
        #listings = response.css('div#yw1.grid-view')
        listings = response.css('tr.odd')
        results = []

        for listing in listings:
            name = listing.css('td.hauptlink').get()
            price = listing.css('td.rechts.hauptlink').get()
            print("price", price)

            name_clean = re.search(r'(?<=title=")[^"]+', name).group()
            price_clean = re.search(r'\d+(?=,00 млн €)', price).group()

            # Добавляем данные в список результатов
            results.append({
                'Name': name_clean,
                'Price': price_clean
            })

        listings = response.css('tr.even')

        for listing in listings:
            name = listing.css('td.hauptlink').get()
            price = listing.css('td.rechts.hauptlink').get()
            print("price", price)

            name_clean = re.search(r'(?<=title=")[^"]+', name).group()
            price_clean = re.search(r'\d+(?=,00 млн €)', price).group()

            # Добавляем данные в список результатов
            results.append({
                'Name': name_clean,
                'Price': price_clean
            })
        # Создаем DataFrame из списка результатов
        df_res = pd.DataFrame(results)
        df_res.to_csv('Football.csv', index=False)

        # Выводим DataFrame в консоль
        print(df_res)
