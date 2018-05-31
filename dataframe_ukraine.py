# coding=utf-8
# Python скрипт для загрузки в Pandas DataFrame Средних данных по областям Украины: SMN, SMT, VCI, TCI, VHI
# pandas это высокоуровневая Python библиотека для анализа данных
import pandas as pd


# функция загружает данные в DataFrame и выводит результат на консоль
def dataframe_upload(file_upload):
    # загрузим файл .csv с помощью функции read_csv() и отформатируем вывод данных
    # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
    # https://www.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html
    df = pd.read_csv(
        file_upload,
        delimiter='\,\s+|\,|\s+',
        engine='python',
        index_col=False,
        names=["year", "week", "SMN", "SMT", "VCI", "TCI", "VHI"]
    )
    print list(df.columns.values)

    return df


# вывод всей таблицы для указанного файла .csv
# print dataframe_upload('csv-raw/vhi_id_12_2018-05-27_14-33.csv')

# альтернативно присвоить имена файлов переменным
cherkasy_csv = 'csv-raw/vhi_id_1_2018-05-27_14-33.csv'
chernihiv_csv = 'csv-raw/vhi_id_2_2018-05-27_14-33.csv'
chernivtsi_csv = 'csv-raw/vhi_id_3_2018-05-27_14-33.csv'
crimea_csv = 'csv-raw/vhi_id_4_2018-05-27_14-33.csv'
dnipropetrovsk_csv = 'csv-raw/vhi_id_5_2018-05-27_14-33.csv'
donetsk_csv = 'csv-raw/vhi_id_6_2018-05-27_14-33.csv'
ivano_frankivsk_csv = 'csv-raw/vhi_id_7_2018-05-27_14-33.csv'
kharkiv_csv = 'csv-raw/vhi_id_8_2018-05-27_14-33.csv'
kherson_csv = 'csv-raw/vhi_id_9_2018-05-27_14-33.csv'
khmelnytskyy_csv = 'csv-raw/vhi_id_10_2018-05-27_14-33.csv'
kiev_csv = 'csv-raw/vhi_id_11_2018-05-27_14-33.csv'
kiev_city_csv = 'csv-raw/vhi_id_12_2018-05-27_14-33.csv'
kirovohrad_csv = 'csv-raw/vhi_id_13_2018-05-27_14-33.csv'
luhansk_csv = 'csv-raw/vhi_id_14_2018-05-27_14-33.csv'
lviv_csv = 'csv-raw/vhi_id_15_2018-05-27_14-33.csv'
mykolayiv_csv = 'csv-raw/vhi_id_16_2018-05-27_14-33.csv'
odessa_csv = 'csv-raw/vhi_id_17_2018-05-27_14-33.csv'
poltava_csv = 'csv-raw/vhi_id_18_2018-05-27_14-33.csv'
rivne_csv = 'csv-raw/vhi_id_19_2018-05-27_14-33.csv'
sevastopol_city_csv = 'csv-raw/vhi_id_20_2018-05-27_14-33.csv'
sumy_csv = 'csv-raw/vhi_id_21_2018-05-27_14-33.csv'
ternopil_csv = 'csv-raw/vhi_id_22_2018-05-27_14-33.csv'
transcarpathia_csv = 'csv-raw/vhi_id_23_2018-05-27_14-33.csv'
vinnytsya_csv = 'csv-raw/vhi_id_24_2018-05-27_14-33.csv'
volyn_csv = 'csv-raw/vhi_id_25_2018-05-27_14-33.csv'
zaporizhzhya_csv = 'csv-raw/vhi_id_26_2018-05-27_14-33.csv'
zhytomyr_csv = 'csv-raw/vhi_id_27_2018-05-27_14-33.csv'

# создние списка областей Украины и г. Киева
ukraine_csv = [cherkasy_csv,
               chernihiv_csv,
               chernivtsi_csv,
               crimea_csv,
               dnipropetrovsk_csv,
               donetsk_csv,
               ivano_frankivsk_csv,
               kharkiv_csv,
               kherson_csv,
               khmelnytskyy_csv,
               kiev_csv,
               kiev_city_csv,
               kirovohrad_csv,
               luhansk_csv,
               lviv_csv,
               mykolayiv_csv,
               odessa_csv,
               poltava_csv,
               rivne_csv,
               sevastopol_city_csv,
               sumy_csv,
               ternopil_csv,
               transcarpathia_csv,
               vinnytsya_csv,
               volyn_csv,
               zaporizhzhya_csv,
               zhytomyr_csv
               ]

# вывод списка файлов всех областей Украины
for x in ukraine_csv:
    print x

# вывод всех таблиц всех областей из списка файлов (указанного выше)
for x in ukraine_csv:
    print dataframe_upload(x)
