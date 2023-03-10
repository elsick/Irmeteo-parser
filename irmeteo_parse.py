from bs4 import BeautifulSoup
import requests

def get_html(url):
    '''Скачивает страницу для последующей передачи парсеру'''
    if requests.get(url):
        soup = BeautifulSoup(requests.get(url).text, 'lxml')
    else:
        print("Сайт недоступен")
    return soup

def irmeteo_temperature(bs):
    temperature = bs.find(id="map-irkutsk-list").find(class_="t-map__temp-val").text.split()[0]
    return temperature

def main():
    temperature_measure = "°C"
    url = f'https://www.irmeteo.ru/'
    temperature_irmeteo = irmeteo_temperature(get_html(url))
    print(temperature_irmeteo)

if __name__ == "__main__":
    main()
else:
    print("Imported")