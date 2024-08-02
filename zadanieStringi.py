tekst = input("Podaj tekst:")
tekst = tekst.lower()
tekst = list(tekst)
tekst.sort()
słownik = {}
for znak in tekst:
  if znak.isalpha() and znak not in słownik:
    słownik[znak] = tekst.count(znak)

  

for znak, ilosc in słownik.items():
  print(znak, ilosc, sep=" -> ")

