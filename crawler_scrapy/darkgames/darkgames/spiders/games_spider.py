import os
import scrapy

class GamesSpider(scrapy.Spider):
    name = "games"

    def start_requests(self):
        urls = [
            'https://www.darkpattern.games/games.php?alignment=dark'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for game in response.css('a.gamebox'):
            yield {
                'title': game.css('div.details *::text').getall(),
                'link': game.css('a.gamebox *::attr(href)').getall(),
                'rating': game.css('div.rating *::text').getall()
            }
        next_page = response.css('div.pagination_next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

# Beispiel-Code, der überprüft, ob 'games.json' existiert, bevor er darauf zugreift
def check_games_file():
    file_path = "games.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = f.read()
            print("Dateiinhalt:", data)
    else:
        print(f"Datei {file_path} existiert nicht. Initialisiere eine leere Datei.")
        with open(file_path, "w") as f:
            f.write("{}")

# Nur zur Demonstration, wie du die Datei überprüfst
check_games_file()
