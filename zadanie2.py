lista = []
size = int(input("ile liczb chcesz wpisac: "))
for i in range(size):
  lista.append(int(input(f"podaj liczbe {i+1}: ")))
y = 0
for x in range(len(lista)):
  y+=lista[x]
srednia = y/len(lista)

if srednia > 4.75:
  print(f"Twoja srednia to: {srednia} masz pasek a oceny to {lista}")
else:
  print(f"Twoja srednia to: {srednia} work harder, oceny to {lista}")