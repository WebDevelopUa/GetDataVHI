# coding=utf-8
# Python скрипт для загрузки в Pandas DataFrame Средних данных для г. Киева (ID=12): SMN, SMT, VCI, TCI, VHI
# и реализации процедур для формирования выборок (включая элементы анализа)
# pandas это высокоуровневая Python библиотека для анализа данных
# https://jeffdelaney.me/blog/useful-snippets-in-pandas/
import pandas as pd

# загрузим файл .csv с помощью функции read_csv() и отформатируем вывод данных
df = pd.read_csv('csv-raw/vhi_id_12_2018-05-27_14-33.csv',
                 engine='python',
                 delimiter='\,\s+|\,|\s+',
                 skiprows=1,
                 index_col=False,
                 names=["year", "week", "SMN", "SMT", "VCI", "TCI", "VHI"]
                 )

# вывод имен столбцов
print list(df.columns.values)

# вывод всей таблицы
# print df

# вывод даных с 1838 строки и до конца таблицы
# print df[1838:]

# вывод даных с таблицы для Киева, за 18-ю неделю 2000 года
print('\n вывод даных с таблицы для Киева, за 18-ю неделю 2000 года: \n')
print df[(df['year'] == '2000') & (df['week'] == 18)]

# вывод даных с таблицы для Киева, за 2018-й год со значениями VHI > 50
print('\n вывод даных с таблицы для Киева, за 2018-й год со значениями VHI > 50: \n')
print df[(df['year'] == '2018') & (df['VHI'] > 50)]

# вывод даных с таблицы для Киева, за все время со значениями 70 < VHI < 90
print('\n вывод даных с таблицы для Киева, за все время со значениями 70 < VHI < 90: \n')
print df[(df['VHI'] > 70) & (df['VHI'] < 90)]

# за все время (понедельно) VHI < 15 - засуха, интенсивность которой зависит от средней до чрезвычайной
print('\n за все время (понедельно) VHI < 15 - засуха, интенсивность которого зависит от средней до чрезвычайной: \n')
print df[(df['VHI'] < 15)]

# за все время (понедельно) VHI < 35 - засуха, интенсивность которой зависит от умеренной до чрезвычайной
print('\n за все время VHI (понедельно) < 35 - засуха, интенсивность которого зависит от умеренной до чрезвычайной: \n')
print df[(df['VHI'] < 35)]

# вывод даных с таблицы для Киева, за все время с максимальным значением VHI
print('\n вывод даных с таблицы для Киева, за все время с максимальным значением VHI: \n')
print df['VHI'].max()

# вывод даных с таблицы для Киева, за все время с максимальным значением VHI (по годам)
print('\n вывод даных с таблицы для Киева, за все время с максимальными значениями VHI (по годам): \n')
print df.groupby('year')['VHI'].max()

# вывод даных с таблицы для Киева, за 2018-й год с максимальным значением VHI
print('\n вывод даных с таблицы для Киева, за 2018-й год с максимальным значением VHI: \n')
print df.groupby(df['year'] == '2018')['VHI'].max()

# вывод даных с таблицы для Киева, за 2018-й год с минимальным значением VHI
print('\n вывод даных с таблицы для Киева, за 2018-й год с минимальным значением VHI: \n')
print df.groupby(df['year'] == '2018')['VHI'].min()
