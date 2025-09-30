"""Sia dato il messaggio cifrato (convertito in numero intero in base 10): 
204751668535
Il messaggio cifrato è stato ottenuto cifrando il messaggio originale con algoritmo RSA senza padding con n=514948966453 e esponente pubblico (e) pari a 3
Provare a decifrare il messaggio cifrato
NB: il messaggio originale è una parola di cinque lettere maiuscole e minuscole.
NB: Quando il problema sembra arduo, allora un approccio brutale potrebbe essere quello vincente."""



messaggio_cifrato=204751668535

modulo=514948966453
e=3


seen= False

for p1 in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
    if seen:
        break

    for p2 in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
        if seen:
            break
    
        for p3 in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            if seen:
                break
        
            for p4 in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
                if seen:
                    break
            
                for p5 in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
                    
                    testo= p1+p2+p3+p4+p5 

                    try:
                        messaggio= int(testo.encode("utf-8").hex(), 16)  
                    
                    except Exception as ex:
                        print("Errore conversione", ex)
                        raise

                    try:
                    
                        c= pow(messaggio, e, modulo)
                    
                    except Exception as ex:
                        print("Errore:", ex)
                        raise
                    

                    if c== messaggio_cifrato:
                        print("Trovato:", testo, "---> int:", messaggio)
                        seen= True
                        break












                
                        




                            

                        


                    
                    
































