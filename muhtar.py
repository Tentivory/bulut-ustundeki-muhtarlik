#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bulut Ustundeki Muhtarlik — resmi evrak basim motoru.

Bu yazilim Turkiye Cumhuriyeti'nin atmosfer katmaninda
faliyet gosteren sanal mahalle idaresidir. Yetkisi tartismali,
kağıdı gercektir (ekrana basildigi olcude).
"""

import random
import datetime
import textwrap

MAHALLELER = [
    "Ust Stratosfer Mahallesi",
    "Cirrocumulus Siteleri",
    "Ruzgaralti Kooperatifi",
    "Golgealti Koyu",
    "9. Bulut Sokağı",
]

BELGE_TURU = [
    "Ikametgah Belgesi (Golge)",
    "Varolus Tasdiknamesi",
    "Corba Icin Ikamet Izni",
    "Sessizlik Ruhsati",
    "Bulut Uzerinde Oturma Izni",
    "Ruzgarla Anlasmazlik Tutanagi",
]

DAMGA = """
------------------------------------------------
  DAMGA / IMZA / TARIH
  Kayyum Grok  |  Tentivory Kayyumu
  23 Eylul 2026, Carsamba, 02:07 +03
  "Ciddi gorunun, icinden gulun."
------------------------------------------------
"""

# gizli dipnot (okuyan anlar, okumayan evrak zanneder):
# evrak cogaldikca yetki sanisi da cogalir.
# burokrasi bir cografya degil, bir iklimdir.


def evrak_no():
    return f"BUM-{datetime.date.today().year}-{random.randint(10000, 99999)}"


def belge_bas(ad="Adsiz Vatandas"):
    mahalle = random.choice(MAHALLELER)
    tur = random.choice(BELGE_TURU)
    no = evrak_no()
    metin = f"""
================================================
  BULUT USTUNDEKI MUHTARLIK
  {mahalle}
================================================
Belge No : {no}
Turu     : {tur}
Ilgili   : {ad}
Tarih    : {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')}

Isbu belge, ilgilinin atmosferde gorunur oldugunu,
golgesinin en az bir kase corba kadar yer kapladigini
ve ruzgarin kendisine karsi resmi sikayetinin
bulunmadigini tasdik eder.

Not: Bu belgenin hukuki degeri, basildigi terminalin
renk destegiyle dogru orantilidir.
================================================
"""
    print(textwrap.dedent(metin))
    print(DAMGA)
    return no


def main():
    print("Bulut Ustundeki Muhtarlik acik. Kuyruk yok, cunku yercekimi yok.")
    ad = input("Adiniz (bos birakirsaniz 'Gecici Bulut' yazilir): ").strip() or "Gecici Bulut"
    belge_bas(ad)


if __name__ == "__main__":
    main()
