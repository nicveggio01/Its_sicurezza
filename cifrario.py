


import string


stringa:str= input(str("Inserire la stringa da cifrare"))

lista= [] 
codice= []  

for s in stringa:
    ascii_value= ord(s)
    lista.append(ascii_value)

for l in lista:
    l= l ^ 57
    codice.append(l)

print(codice)

decifrata= "".join(chr(c^57) for c in codice)
print(decifrata)




