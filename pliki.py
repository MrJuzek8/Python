#plik = open("plik.txt", "r" )
#r- read
#a - append
#w - write
#x - create


def kantor_dolary(*kwoty, kurs=4.20):
  przewalutowane_kwoty=[]
  for kwota in kwoty:
    przewalutowana_kwota = round(kwota/kurs,2)
    przewalutowane_kwoty.append(przewalutowana_kwota)
  return przewalutowane_kwoty

przewalutowane_kwoty = kantor_dolary(200,20,30)

plik = open("kwoty.txt", "w")
for kwota in przewalutowane_kwoty:
  plik.write(str(kwota) + "\n")

w_zł = open("w_zł.txt", "w")
for i in range(10,1001,10):
  w_zł.write(str(i)+"\n")

w_zł.close()
w_zł = open("w_zł.txt", "r")
print(w_zł.read())
w_zł.close()