from bs4 import BeautifulSoup
import requests
import pickle

def get_html(url):
    '''Получаем страницу и передаем ее в парсер'''
    if requests.get(url):
        soup = BeautifulSoup(requests.get(url).text, 'lxml')
        return soup
    else:
        print('Сайт не доступен')

def read_cities_dict():
    '''Считываем список городов из файла'''
    with open('cities_dict', 'rb') as fileobj:
        cities_dict = pickle.load(fileobj)
    return cities_dict

def irmeteo_temperature(bs,city):
    temperature = bs.find(id="map-"+city+"-list").find(class_="t-map__temp-val").text.split()[0]
    return temperature

def main():
    temperature_measure = "°C"
    url = f'https://www.irmeteo.ru/'
    cities = read_cities_dict()
    print('Введите город из списка')
    print(list(cities.keys()))
    city = input()
    soup = get_html(url)
    temperature = irmeteo_temperature(soup,cities[city])
    print(temperature+" "+temperature_measure)

if __name__ == "__main__":
    main()
