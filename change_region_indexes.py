# coding=utf-8
# Python скрипт для загрузки данных из .csv файла в Pandas DataFrame и замены значений областей (ID)
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.replace.html
import pandas as pd

# загрузим файл .csv с помощью функции read_csv()
df = pd.read_csv('csv/export_data1.csv')

# df = df.replace(to_replace=r'10:', value='21')
df = df.replace('1:', '22')
df = df.replace('2:', '24')
df = df.replace('3:', '23')
df = df.replace('4:', '25')
df = df.replace('5:', '3')
df = df.replace('6:', '4')
df = df.replace('7:', '8')
df = df.replace('8:', '19')
df = df.replace('9:', '20')
df = df.replace('10:', '21')
df = df.replace('11:', '9')
df = df.replace('12:', '26')
df = df.replace('13:', '10')
df = df.replace('14:', '11')
df = df.replace('15:', '12')
df = df.replace('16:', '13')
df = df.replace('17:', '14')
df = df.replace('18:', '15')
df = df.replace('19:', '16')
df = df.replace('20:', '27')
df = df.replace('21:', '17')
df = df.replace('22:', '18')
df = df.replace('23:', '6')
df = df.replace('24:', '1')
df = df.replace('25:', '2')
df = df.replace('26:', '7')
df = df.replace('27:', '5')

# вывод имен столбцов
print list(df.columns.values)

# вывод даных для провепки
print df[(df['Unnamed: 0'] == 0)]

# экспорт даных с DataFrame в новый файл в папке csv
df[(df['Unnamed: 0'] == 0)].to_csv('csv/export_data2.csv')

# экспорт даных с DataFrame в новый файл в папке csv
df.to_csv('csv/export_data3.csv')
