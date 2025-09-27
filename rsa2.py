
n="99348409501eddf1590684ccec3d327f8bb19af1bac72f67a9a33858b18d450d8c183313a0f7e9dd59f665f406e76742361a903e2cfe806a188e181d07b01725"

e= 65537

n_decimale=int(n, 16)
M= "ciao come va"
mi= int(M.encode("utf-8").hex(), 16)
cifrato= pow(mi, e, n_decimale)
print(cifrato)

d= "2B6D3F2190C46E9BDE175A09A33C7A4E5F19D1F7A8C4B67E2F0D39BFA2E9C351"

n="99348409501eddf1590684ccec3d327f8bb19af1bac72f67a9a33858b18d450d8c183313a0f7e9dd59f665f406e76742361a903e2cfe806a188e181d07b01725"

e= 65537

n_decimale=int(n, 16)
M= "ciao come va"
mi= int(M.encode("utf-8").hex(), 16)
cifrato= pow(mi, e, n_decimale)
print(cifrato)

d= "2B6D3F2190C46E9BDE175A09A33C7A4E5F19D1F7A8C4B67E2F0D39BFA2E9C351"

d_decimale= int(d, 16)
decifrato= pow(cifrato, d_decimale, n_decimale)

decifrato= format(decifrato, "x")

if len(decifrato) %2 !=0:
    decifrato= "0"+ decifrato


testo= bytes.fromhex(decifrato).decode("utf-8")
print(testo)




d_decimale= int(d, 16)
decifrato= pow(cifrato, d_decimale, n_decimale)

decifrato= format(decifrato, "x")

if len(decifrato) %2 !=0:
    decifrato= "0"+ decifrato


testo= bytes.fromhex(decifrato).decode("utf-8")
print(testo)



