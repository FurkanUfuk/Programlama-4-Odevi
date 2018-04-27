Soru 1)
from odevler1 import ciro
*************************
gelirler=x
giderler=y
toplamCiro=z
toplamCalisanSayisi=t
class hesapla:
    def __init__(self,x,y,z,t):
        self.x=x
        self.y=y
        self.z=z
        self.t=t
    def isletmeKari(self):
        isletmeKari=self.x-self.y
        return isletmeKari
    def adambasiCiro(self):
        adambasiCiro=self.z/self.t
        return adambasiCiro
Soru 2)
from odevler2 import bilanco
*****************************
kasaHesabi=a
alinanCeklerHesabi=b
bankalarHesabi=c
alicakSenetelerHesabi=d
ticariMallarHesabi=e
binalarHesabi=f
tasitlarHesabi=g
demirbaslarHesabi=h
bankaKredileriKisa=i
saticilarHesabi=j
bankaKredileriUzun=k
borcSenetleri=l
sermayeHesabi=m
class donenVarliklar:
    a=20000
    b=10000
    c=5000
    d=28000
    e=65000
class duranVarliklar:
    f=150000
    g=25000
    h=8000
class kvyk:
    i=42000
    j=60000
class uvyk:
    k=35000
    l=115000
class ozKaynaklar:
    m=59000
class hesap():
    def __init__(self,a,b,c,d,e,f,g,h,i,j,k,l,m):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
        self.g=g
        self.h=h
        self.i=i
        self.j=j
        self.k=k
        self.l=l
        self.m=m
    def aktif(self):
        aktif=self.a+self.b+self.c+self.d+self.e+self.f+self.g+self.h
        return aktif
    def pasif(self):
        pasif=self.i+self.j+self.k+self.l+self.m
        return pasif
    if (aktif==pasif):
        print("Tebrikler!Kapanış Bilançocu Doğru Hesaplandı.")
    else:
        print("Üzgünüm!Kapanış Bilançosu Yanlış Hesaplandı.")
        
 Soru 3)
 from odeler3 import facebook
 ****************************
a=begenenSayisi
b=yorumSayisi
c=paylasimSayisi
d=icerikSayisi
e=takipciSayisi
class ybs1:
    a=365000
    b=65000
    c=870
    d=500
    e=1125000
class etkilesim1:
    def __init__(self,a,b,c,d,e):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
    def etkilesim1(self):
        etkilesim1=(((self.a+self.b+self.c)/d)/e)*100
        return etkilesim1
class ybs2:
    a=450000
    b=25000
    c=380
    d=100
    e=1450000
class etkilesim2:
    def __init__(self,a,b,c,d,e):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
    def etkilesim2(self):
         etkilesim2=(((self.a+self.b+self.c)/d)/e)*100
         return etkilesim2
class ybs3:
    a=582000
    b=52000
    c=1200
    d=6590
    e=2000000
class etkilesim3:
    def __init__(self,a,b,c,d,e):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
    def etkilesim3(self):
        etkilesim3=(((self.a+self.b+self.c)/d)/e)*100
        return etkilesim3
