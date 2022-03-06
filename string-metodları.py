#String Metodları

gel_yaz ="gelecegi_yazanlar "

a = 9
b=10

a*b
#len uzunluğu verir
len(gel_yaz)

#upper() ve lower()

print(gel_yaz)
gel_yaz.upper()
gel_yaz.lower()

B =gel_yaz.lower()

B.islower()


#replace() değiştirme metodu

gel_yaz.replace("e","a")

gel_yaz.replace("a","i")


#strip() istenmeyin karakterleri kırmpar

#♣gel_yaz=" *Gelecegi_yazanlar* "
gel_yaz.strip() 

#boş ise boşlukları siler
#fonksiyon boş ise ön tanımlı değerlere göre ayarlar

gel_yaz.strip("*")

# dir() metodu ne metodlar olduğunu listler
dir(gel_yaz)
dir(5)
gel_yaz.capitalize()


#SUBSTRINGLER

gel_yaz[0]
gel_yaz[10]

gel_yaz[0:3]


#♥DEGİSKENLER
X = 99999
Y="ali_uzaya_git"

c = X*2

#type_Donusumleri

sayi1=input()
sayi2=input()


print(sayi1 + sayi2)

int(sayi1)+int(sayi2)

int(11.6)
float(11)
str(120)
type(str(120))


#print

print("gelecegi","yazanlar")
print("gelecegi","yazanlar",sep="-") 
#fonksiyonların genel amaçlarını biçimlendirmek için kullanılan alt görev belireçlerine argüman den,r.


print

"10"+ 2

sakla=9
yeni_sakla=sakla*9

a="bu uzun bir metindir"
a[8]

len(a)
