# coding=utf-8
# Python скрипт для загрузки в Pandas DataFrame Средних данных для г. Киева (ID=12): SMN, SMT, VCI, TCI, VHI
# pandas это высокоуровневая Python библиотека для анализа данных
import pandas as pd

# загрузим файл .csv с помощью функции read_csv() и отформатируем вывод данных
df = pd.read_csv('csv-raw/vhi_id_12_2018-05-27_14-33.csv',
                 engine='python',
                 delimiter='\,\s+|\,|\s+',
                 skiprows=1,
                 index_col=False,
                 names=["year", "week", "SMN", "SMK", "VCI", "TCI", "VHI"]
                 )

# вывод имен столбцов
print list(df.columns.values)

# вывод всей таблицы
print df

# вывод даных с 1838 строки и до конца таблицы
# print df[1838:]

# вывод даных с таблицы для Киева, за 2000-й год и 18-я неделя
print df[(df['year'] == '2000') & (df['week'] == '18')]

# print df[(df['week'] == '10') & (df['VHI'] < '90') & (df['year'] == '2018')]

# print df[(df['VHI'] > '80') & (df['VHI'] < '90')]

# print df[(df['year'] > '2017') & (df['year'] < '2019')]
