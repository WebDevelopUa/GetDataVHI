# coding=utf-8
# Python скрипт для загрузки данных из .csv файла в Pandas DataFrame и сортировки по значению областей (ID)
# https://devpractice.ru/python-lessons/
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.drop.html
# https://chrisalbon.com/python/data_wrangling/pandas_dropping_column_and_rows/
import pandas as pd

# загрузим файл .csv с помощью функции read_csv()
df = pd.read_csv('csv/export_data2.csv')

# вывод начальных (входных) данных
print df

# выбор необходимых для работы колонок таблицы, переименование заголовков, сортировка по номеру области
col_list = ['TCI', 'VHI']
df = df[col_list].sort_values(by='TCI').rename({'TCI': '№ области', 'VHI': 'Название'}, axis='columns')

# удалить строку по индексу (г. Киев и Севастопль)
df = df.drop(df.index[[25, 26]])

# вывод данных для провепки
print df

# экспорт даных с DataFrame в новый файл в папке csv
df.to_csv('csv/export_data2sort.csv')
