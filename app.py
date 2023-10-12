from autoscraper import AutoScraper
# url de donde obtendremos los datos
url = "https://www.farmacenter.com.py/catalogo/tratamientos-dermocosmeticos-c66"
# tomamos una muestra de los datos que queremos obtener
wanted_list = ["Uriage Hyséac Gel Limpiador Purificante Gel Nettoyant - Pomo de 150 ml","₲. 113.670"]

scraper = AutoScraper()

# set the rules to scraper / retorna una lista de resultados similares a wanted_list
scraper.build(url, wanted_list)

# Ordenar por precio de forma ascendente

# agrupar/separar por nombre y precio by an unique id
result = scraper.get_result_similar(url,grouped=True)
print(result)
# matchear cada producto con su precio

scraper.set_rule_aliases({'rule_hi6e':'product', 'rule_1e4i':'price'})
scraper.keep_rules(['rule_hi6e','rule_1e4i'])
result = scraper.get_result_similar(url,group_by_alias=True)
print(result)
price = result['price']