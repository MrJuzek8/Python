lista1 = [1,2,3,4,5]
lista2= lista1[::2]
lista3= lista1[1:-1]
print(lista2)


los = 13
moje = [1,4,5,12,10,3]
print(los not in moje)
#print(los in moje)
#zbiór to unikalne wartości
zbiór = {2,3,4,5,6,21,2,4,12,4,5,8,7,9,5,1}
# unikalne_liczby = []
# for liczba in lista4:
#   if liczba not in unikalne_liczby:
#     unikalne_liczby.append(liczba)
# print(unikalne_liczby)
print(zbiór)

zbiór2 = set()
zbiór2.add(1)
zbiór2.add("tak")
zbiór2.add("nie")
zbiór2.remove("tak")
print(zbiór2)

zbiór1 = {1,3,4,8}
zbiór3=  {1,3,4,5}

zbiór4 = zbiór1.union(zbiór3)
print("zbiór 4:", zbiór4)
zbiór41 = zbiór1.intersection(zbiór3)
print("zbiór 41:", zbiór41)

zbiór8 = zbiór1.difference(zbiór3)
print("zbiór 8:", zbiór8)
#operacje takie jak na listach


for element in zbiór2:
  print(element)
zbiór9 = {1,2,3}
lista2 = [4,5,6]
lista2.extend(zbiór9)

for element in lista2:
  print(element)