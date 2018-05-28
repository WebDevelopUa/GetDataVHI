# coding=utf-8
# Python скрипт для загрузки в Pandas DataFrame Средних данных по областям Украины: SMN, SMT, VCI, TCI, VHI
# pandas это высокоуровневая Python библиотека для анализа данных
import pandas as pd
# для указания директории c .csv используем модуль glob()
import glob

# процедура загружает данные с файлов папки csv-raw в DataFrame и выводит результат на консоль
path = r'csv-raw'
allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,
                     delimiter='\,\s+|\,|\s+',
                     engine='python',
                     index_col=False,
                     names=["year", "week", "SMN", "SMK", "VCI", "TCI", "VHI"]
                     )

    list_.append(df)

# создние списка областей Украины и г. Киева
frame = pd.concat(list_)

# экспорт даных с DataFrame в новый файл в папке csv
frame.to_csv('csv/export_data1.csv')

print list(frame)

# вывод всех таблиц всех областей Украины
#  map(), чтобы преобразовать каждый элемент списка в строку и join() присоединить к ним:
print '\n ---------------------------------------------------------- \n'.join(map(str, list_))
