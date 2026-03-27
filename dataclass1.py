#YANGI MASALALAR
#04.03.2026-YIL

##1-masala:
# from dataclasses import dataclass
#
# @dataclass
# class Talaba:
#     ism: str
#     yosh: int
#     kurs:int
#
# talaba_baxosi = Talaba("Munojat",20,3)
#
# print(talaba_baxosi)

##2-Masala;
# from dataclasses import dataclass
#
# @dataclass
# class Kitob:
#     nomi:str
#     muallif:str
#     sahifa_soni:int
#
# binafsha_shulasi = Kitob("Binafsha shulasi","Usoma Muslim",383)
# print(binafsha_shulasi)
#

##3-masala:
# from dataclasses import dataclass
#
# @dataclass
# class Telefon:
#     brand:str
#     model:str
#     narx:int
#
# telefon=Telefon("Iphone","Iphone17",17_000_000)
# print(telefon)

##4-Masala:
# from dataclasses import dataclass
#
# @dataclass
# class Avtamobil:
#     marka:str
#     rang:str
#     yil:int
#
# avtamobil = Avtamobil('Gentra','Qora',2025)
# print(avtamobil)

##5-Masala:
# from dataclasses import dataclass
#
# @dataclass
# class Shahar:
#     nomi:str
#     davlat:str
#     aholi:int
#
# shahar = Shahar('Tokyo','Yaponiya',17_000_000)
# print(shahar)

##6-Masala:
# from dataclasses import dataclass
#
# @dataclass
# class Kompyuter:
#     protsessor:str
#     ram:int
#     xotira:int
#
# kompyuter = Kompyuter('core i7',64,216)
# print(kompyuter)

##7-Masala:
# from dataclasses import dataclass
#
# @dataclass
# class Film:
#     nomi:str
#     janr:str
#     yil:int
#
# film = Film('Pinkhouse','drama',2019)
# print(film)

##8-Masala:
# from dataclasses import dataclass
#
# @dataclass
# class Hisob:
#    ism:str
#    hisob_raqam:int
#    balans:int
#
# hisob=Hisob("Marjona",1342573849767657,2_50_000)
# print(hisob)

##9-Masala:
# from dataclasses import dataclass
#
# @dataclass
# class Oqtuvchi:
#     ism:str
#     fan:str
#     tajriba_yili:int
#
# oqtuvchi = Oqtuvchi('Sharofat','Geometriya',12)
# print(oqtuvchi)

##10-Masala:
# from dataclasses import dataclass
#
# @dataclass
# class Mahsulot:
#     nomi:str
#     narx:int
#     miqdor:int
#
# mahsulot = Mahsulot("Shakar",15_000,6)
# print(mahsulot)


#----------------------------------------------------------
##1-Masala:
# from dataclasses import dataclass
#
# @dataclass
# class Tortburchak:
#     eni: float
#     boyi:float
#
# shakl = Tortburchak(7,9)
# print(shakl.eni * shakl.boyi)

##2-Masala:
# from dataclasses import dataclass
# from math import pi
#
# @dataclass
# class Doira:
#     radyus: float
#
#     def yuzasi(self)->float:
#         return self.radyus * self.radyus * pi
#
# d = Doira(radyus=9)
# print(d.yuzasi())


##3-Masala:
# from dataclasses import dataclass
#
# @dataclass
# class Talaba:
#     ism: str
#     baho: int
#
# talaba_baxosi = Talaba("Munojat",5)
#
# print(talaba_baxosi)

##4-Masala:
# from dataclasses import dataclass
#
# @dataclass
# class Tortbuchak:
#     eni:float
#     boyi:float
#
# eni = float(5)
# boyi = float(9)
#
# perimetr = 2 * (eni + boyi)
# print(perimetr)

##5-Masala:
# from dataclasses import dataclass
# from math import pi
#
# @dataclass
# class Doira:
#     radyus: float
#
#     def uzunlik(self)->float:
#         return 2 * pi*self.radyus
#
# d = Doira(radyus= 6)
# print(f'Radius = {d.radyus}->Uzunlik = {d.uzunlik():.2f}')

##6-Masala:
# from dataclasses import dataclass
#
# @dataclass
# class Moshina:
#     model:str
#     narx:float
#
# mashina = Moshina(model='Matiz', narx=18_000_000)
# print(mashina)

##7-Masala:
# from dataclasses import dataclass
#
# @dataclass
# class Kitobsahifa:
#     nomi : str
#     sahifalar_soni: int
#
# kitob = Kitobsahifa("Qozichoqlar sukunati",500)
# print(kitob.sahifalar_soni)

##8-Masala:
# from dataclasses import dataclass
# from math import sqrt
#
# @dataclass
# class Tortburchak:
#     eni: float
#     boyi:float
#
#     def hisobla(self)->float:
#         return sqrt(self.eni**2 + self.boyi**2)
#
# tortburchak = Tortburchak(6,8)
# print(tortburchak.hisobla())

##9-Masala:
# from dataclasses import dataclass
#
# @dataclass
# class Talaba:
#     ism:str
#     yosh:int
#
# talaba = Talaba("Mushtariy",16)
# print(talaba)

##10-Masala:
# from dataclasses import dataclass
#
# @dataclass
# class UchburchakYuzasi:
#     asos:int
#     balandlig:int
#
# def  hisobla(self):
#     return self.asos * self.balandlig / 2
#
# ucburchak_yuzasi = UchburchakYuzasi(7,9)
# print(hisobla(ucburchak_yuzasi))

for son in range(2,10,3):
    print("Son:",son)