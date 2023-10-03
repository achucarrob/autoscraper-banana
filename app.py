from autoscraper import AutoScraper

url = "https://www.farmacenter.com.py/catalogo/tratamientos-dermocosmeticos-c66"

wanted_list = ["Uriage Hyséac Gel Limpiador Purificante Gel Nettoyant - Pomo de 150 ml","₲. 113.670"]

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
for i in result:
    print(i)
    