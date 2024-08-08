def rot13(string):
    lista = list(map(chr, range(97, 123)))
    puntctuation = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
    word = []
    for i in string:
        if i.isalpha() and i.islower():
            x = lista.index(i)
            print(i)
            nx = (x + 13)
            if nx >= 26:
                nx = nx - 26
            word.append(lista[nx])
        elif i.isupper():
            y = i.lower()
            x = lista.index(y)
            nx = (x + 13)
            if nx >= 26:
                nx = nx - 26
            word.append(lista[nx].upper())
        elif i.isspace():
            word.append(' ')
        elif i.isnumeric():
            word.append(i)
        elif i in puntctuation:
            y = puntctuation.index(i)
            word.append(puntctuation[y])
    
    return ''.join(word)
        


print(rot13('aA bB zZ 1234 *!?%'))
# puntctuation = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
# def alpha(a):
#     y = a.isupper()
#     return y 
        

# print(alpha('A'))




