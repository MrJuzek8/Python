krotka = (1,2,3,4)
print(krotka[0])
print(1 in krotka)
print(5 not in krotka)
print(krotka.count(1))
print(krotka[1:-1])

for i in krotka:
  print(i)



#Słownik

słownik = {"jan": "jan@gmail.com",
          "Robert": "robert@gmail.com"}


słownik["jan"] = "kam.jan@gmail.com"

print(słownik["jan"])

for klucz in słownik.keys():
  print(słownik[klucz])

for wartosc in słownik.values():
  print(wartosc)

for klucz, wartosc in słownik.items():
  print(klucz + ":" + wartosc)


słownik.get("Robert")
print(słownik.pop("Robert"))

słownik["Andrzej"]="andrzej@gmail.com"


słownik.update({"Marcin": "m@gmail.com"})
print(słownik)