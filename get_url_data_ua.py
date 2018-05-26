# coding=utf-8
# Python скрипт для скачивания Средних данных по областям Украины: SMN, SMT, VCI, TCI, VHI
# с сайта https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/vh_browseByCountry.php

import urllib2
import datetime


def download_vhi():
    for obj_id in range(1, 28):
        # URL-адрес областей Украины (ID={})
        url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID={}&year1=1981&year2=2018&type=Mean".format(
            obj_id)

        print "Данные загружаются с сайта ... Примерное время ожидания - до 5 минут"

        # функция urlopen() способна извлечь URL-адрес с помощью различных протоколов (HTTP, FTP)
        vhi_url = urllib2.urlopen(url).read()

        # откроем файл на запись (со скачиванием бинарного файла 'b') для Областей Украины (ID={}) + дата и время
        dt = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        out = open('csv-raw/vhi_id_{}_{}.csv'.format(obj_id, dt), 'wb')

        # читаем URL и записываем в локальный файл
        out.write(vhi_url)
        out.close()

        print "Данные загружены в папку csv-raw, объект c ID: " + str(obj_id) + " с текущей датой и временем:  " + dt


download_vhi()
