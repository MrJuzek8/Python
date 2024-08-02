# imie = "Marcin"
# nazwisko ="Kowalski"

# print(imie, nazwisko)
# print(imie, nazwisko, sep=" * ", end="**")
# print("jan" "\nkowalski")

# dni_tygodnia = "poniedziałek wtorek środa"
# dni_tygodnia = dni_tygodnia.split(" ")
# print(dni_tygodnia)

# imie2 = input("podaj imie:")

# print(imie2.capitalize())
# print(imie2.title())
# print(imie2.upper())
# print(imie2.lower())

# # .startswith()
# if imie2.endswith("a"):
#   print("baba")
# else:
#   print("not baba")



nr_tel= input("Podaj numer telefonu:")

if "-" in nr_tel:
  nr_tel = nr_tel.replace("-", " ")

nr_tel = nr_tel.lstrip()
print(nr_tel)


#litery alfabetu
print("abc".isalpha()) #-> True
print("a12".isalpha()) #-> False

#znaki alfanumeryczne

print("a12".isalnum()) #-> False
print("a12.".isalnum()) #-> True
#cyfry
print("123".isnumeric()) #-> True
print("-123,45".isnumeric()) #-> Fallse

#spacje
print(" ".isspace())#->True
print(" . ".isspace()) #->False
