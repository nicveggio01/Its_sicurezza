"""Premessa: nell'RSA, per calcolare con python l'esponente privato nota la chave pubblica e noti i due numeri primi p e q, si utilizza la sequente funzione
d = inverse(e, phi) dove ph = (p-1)*(q-1).

Sia dato n (pari a p*q) = 51151902024533551
e siano
e (esponente pubblico) = 3
C=10002041662569686 il messaggio cifrato (l'originale è una parola di sette caratteri alfanumerici)
Decifrare il messaggio
NB: un attacco forza bruta su 7 caratteri ha un costo computazionale pari a 62^6 = 56.800.235.584 (infattibile in python)
NB: ma n=p*q e quindi se riuscissi a trovare i due numeri primi che fattorizzano n, allora potrei applicare euclide inverso (la funzione inverse) per trovare la chiave privata..."""





def factor(n:int):

   # matematicamente provo i divisori fino a n---> intervallo 2, n

    for i in range(2, n):
        if n%i==0:
            p=i
            q=n//i
            print("P e Q che fattorizzano n sono rispettivamente", p, q)
            return p, q
    
    return None

n= 151902024533551
e=3
c=10002041662569686 


#Applico la funzione Factor al mio modulo n per ricavare p e q


p, q= factor(n)

if p and q:
    print("Valori trovati----> p:", p, "q:", q)

#Applico la funzione data in consegna


ph= (p-1)*(q-1)

#Applico la funzione inversa

exp_priv= pow(e, -1, n)
#Ho ottenuto esponente privato per decifrare

decifrato= pow(c, exp_priv, n)
print("Decifrato:", decifrato)

#Ho ottenuto un intero per cui adesso devo convertire prima in byte e poi in testo leggbile

length=(decifrato.bit_length()+7)//8 
msg_bytes= decifrato.to_bytes(length, "big")
plain_text= msg_bytes.decode("utf-8")

print(f"Messaggio decrptato: {plain_text}")

















