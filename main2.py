
# wiek = int(input("wiek: "))
# if wiek >=21:
#   print("mozesz kupic piwo w USA i Polsce")
# elif wiek >=18:
#   print("mozesz kupic piwo w Polsce")
# else: 
#   print("nie mozesz kupic piwa")


#pętle
# n=1
# while n <= 10:
#   print(n)
#   n+=1

# for i in range(2,19,3):
#   print(i)

#listy
lista = [2,8,455,444]
lista.append(1)


print(lista)
lista.insert(1, 3)
print(lista)
print(lista[2])
for i in range(len(lista)):
  print(lista[i])


for element in lista:
  print("*",element)

lista.pop(2) #kasujemy - ujemne indexy od konca kasuje
print(lista)

# lista.clear() # kasuje cala liste


lista2 = [ 1, 2,3,4,5,6,7,8,9,10]
lista3 = lista + lista2
print(lista3)

lista3.sort(reverse = True)
print(lista3)