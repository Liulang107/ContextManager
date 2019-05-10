# Задача 1. Написать программу для файла в формате json.

import json
from collections import OrderedDict


def sort_by_length(input_str):
    return len(input_str)


def get_data_from_json():
    word_list = []
    with open('newsafr.json') as file:
        news = json.load(file)
        for item in news['rss']['channel']['items']:
            for word in item['description'].split(' '):
                if len(word) > 6:
                    word_list.append(word.lower())
    return word_list


def search_for_10_top(words):
    words.sort(key=sort_by_length, reverse = True)
    word_dict = {x:words.count(x) for x in words}
    word_dict = OrderedDict(sorted(word_dict.items(), key=lambda x: x[1], reverse=True))
    for i, word in enumerate(word_dict.items()):
      print(f'Слово "{word[0]}" встречается {word[1]} раз')
      if i == 10:
          break


# Задача 2. Написать программу для файла в формате xml.

import xml.etree.ElementTree as ET


def get_data_from_xml():
    tree = ET.parse('newsafr.xml')
    root = tree.getroot()
    word_list = []
    for description in root.findall('./channel/item/description'):
        for word in description.text.split(' '):
            if len(word) > 6:
                word_list.append(word.lower())
    return word_list


def main():
    while True:
        user_input = input('Введите команду (j, x или q): ')
        if user_input == 'j':
            print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов в файле json: ')
            search_for_10_top(get_data_from_json())
        elif user_input == 'x':
            print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов в файле xml: ')
            search_for_10_top(get_data_from_xml())
        elif user_input == 'q':
            break
        else:
            print('Неверная команда')


main()