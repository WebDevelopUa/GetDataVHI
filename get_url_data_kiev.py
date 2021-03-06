# coding=utf-8
# Python скрипт для скачивания Средних данных для Киевской области (ID=11): SMN, SMT, VCI, TCI, VHI
# с сайта https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/vh_browseByCountry.php

# urllib2 это модуль Python для работы с URL-адресом
import urllib2
# datetime - модуль для работы с датой и временем
import datetime

# URL-адрес Киевской области (ID=11)
url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID=11&year1=1981&year2=2018&type=Mean"

print "Данные загружаются с сайта ... Примерное время ожидания - до 5 минут"

# функция urlopen() способна извлечь URL-адрес с помощью различных протоколов (HTTP, FTP)
vhi_url = urllib2.urlopen(url)

# откроем файл на запись (со скачиванием бинарного файла 'b') для Киевской обласи (ID=11) + дата и время
dt = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
out = open('csv-raw/vhi_id_11_{}.csv'.format(dt), 'wb')

# читаем URL и записываем в локальный файл
out.write(vhi_url.read())
out.close()

print "Данные загружены в папку csv-raw с текущей датой и временем:  " + dt
