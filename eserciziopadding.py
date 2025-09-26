
import os

msg= b"A"

block_size= 32
missing= block_size - len(msg)
padding= os.urandom(missing)
msg_padded= msg + padding

print(f"Messaggio Originale: {msg}")
print(f"Lunghezza Finale:{len(msg_padded)}")
print(f"Messaggio con Padding: {msg_padded.hex()}")