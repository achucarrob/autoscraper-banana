from autoscraper import AutoScraper

url = "https://www.farmacenter.com.py/catalogo/tratamientos-dermocosmeticos-c66"

wanted_list = ["Uriage Hyséac Gel Limpiador Purificante Gel Nettoyant - Pomo de 150 ml","₲. 113.670"]

scraper = AutoScraper()

# retorna una lista de resultados similares a wanted_list
result = scraper.build(url, wanted_list)

# print(result)

# Ordenar por precio de forma ascendente

# agrupar/separar por nombre y precio
result = scraper.get_result_similar(url,grouped=True)
print(result)
