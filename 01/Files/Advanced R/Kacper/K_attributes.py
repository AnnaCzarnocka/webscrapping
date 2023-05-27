from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

links = ['https://www.otodom.pl/pl/oferta/mokotow-powsinska-apartament-118m2-ID4jzWO', 
        'https://www.otodom.pl/pl/oferta/bezposrednio-bez-pcc-nowe-2022-wykonczone-ID4d3ed', 
        'https://www.otodom.pl/pl/oferta/ciche-mieszkanie-na-starym-mokotowie-ID4lgVv', 
        'https://www.otodom.pl/pl/oferta/woronicza-qbik-84-mkw-jednopoziomowe-ID4lnt9']

# find_property_one_attribute_1
## 3 attributes has very similiar structure to find it
## the difference is in name of string and tag which to find

## arguments:
### bs - BeautifulSoup object of html
### tag - tag which to find

def find_property_one_attribute_1(bs, tag, search_dict):
    try:
        return bs.find(tag, search_dict).text
    except:
        return ''

# find_property_one_attribute_2
## 8 attributes has the same structure to find it, the difference is in name of string
## we wrote a function not to repeat code

## arguments:
### bs - BeautifulSoup object of html
### attribute_name - name of the attribute that we want to find

def find_property_one_attribute_2(bs, attribute_name):
    try:
        return bs.find('div', string = attribute_name).find_next('div').find_next('div').text
    except:
        return ''

# find_property_all_attributes
## function to find all attributes that we need from single page
## arguments:
### url - url to the page that we want to scrape

def find_property_all_attributes(url, attributes_1, attributes_2):
    html = request.urlopen(url)
    bs = BS(html.read(), 'html.parser')

    # names of teh property/info that has the same path to find and its map to english names which will be used
    property_attributes = {}

    # find the first 3 attributes and assign them to property_attributes dict
    for attribute, (tag, search_dict) in attributes_1.items():
        property_attributes[attribute] = find_property_one_attribute_1(bs, tag, search_dict)

    # find the reamining 8 attributes and assign them to property_attributes dict
    for english_name, original_name in attributes_2.items():
        property_attributes[english_name] = find_property_one_attribute_2(bs, original_name)

    return property_attributes

# find_all_properties_all_attributes
## function to find all attributes of all properties
## and append them to a all_properties_all_attributes dataframe

## arguments:
### links - list of links to the webpage with adv wchich we want to scrape

def find_all_properties_all_attributes(links):
    df = pd.DataFrame({'price': [],
                        'location':[],
                        'price_m2':[],
                        'area':[], 
                        'property_from':[], 
                        'room_no':[], 
                        'finish_condition':[],
                        'balcony_garden_terrace':[], 
                        'rent':[], 
                        'parking_place':[], 
                        'heating':[], })
    
    # define the first 3 attributes and their location on the page
    # for the purpose of function find_property_one_attribute_1
    attributes_1 = {
    'price': ('strong', {'aria-label': 'Cena'}),
    'location': ('a', {'aria-label': 'Adres'}),
    'price_m2': ('div', {'aria-label': 'Cena za metr kwadratowy'})
    }

    # define the remaining 8 attributes
    # for the purpose of function find_property_one_attribute_2
    attributes_2 = {
        'area': 'Powierzchnia',
        'property_from': 'Forma własności',
        'room_no': 'Liczba pokoi',
        'finish_condition': 'Stan wykończenia',
        'balcony_garden_terrace': 'Balkon / ogród / taras',
        'rent': 'Czynsz',
        'parking_place': 'Miejsce parkingowe',
        'heating': 'Ogrzewanie'
    }

    for link in links:
        property_attributes = find_property_all_attributes(link, attributes_1, attributes_2)
        df = df.append(property_attributes, ignore_index = True)

    return df

print(find_all_properties_all_attributes(links))

