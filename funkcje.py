# def funkcja(napis):
#   print(napis)

# funkcja('xD')

# def dodaj(a,b):
#   print(a+b)

# dodaj(1,2)

# def dodajwiele(*args):
#   suma = 0
#   for i in args:
#     suma +=i
#   print(suma)

# dodajwiele(1,2,3,4,5)


# def wyswietl_dane(imie, rok_urodzenia):
#   print(imie)
#   print(2024 - rok_urodzenia)

# wyswietl_dane("Jan", 2001)


# # **kwargs
# def rodzina(**członkowie):
#   for typ, imie in członkowie.items():
#     print(typ, "->", imie)
# rodzina(mama="Grażyna", tata="Jan", siostra="Ala")


# def przywitanie(imie="Jan"):
#   print("Cześć", imie)

# przywitanie("Kuba")

# def wyswietl_sume(liczby):
#   suma=0
#   for liczba in liczby:
#     suma += liczba
#   #print(suma)
#   return suma

# suma = wyswietl_sume([1,2,3,4,5,6,7])
# print(suma/2)



## Zadanie na dolary


def kantor_dolary(*kwoty, kurs=4.20):
    przewalutowane_kwoty=[]
    for kwota in kwoty:
      przewalutowana_kwota = round(kwota/kurs,2)
      przewalutowane_kwoty.append(przewalutowana_kwota)
    return przewalutowane_kwoty

hajs = kantor_dolary(10,12,15)
for kwota in hajs:
  print(kwota)
  
  

