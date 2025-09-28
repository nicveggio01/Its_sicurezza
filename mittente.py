
from Crypto.Cipher import AES
import base64

# --- Modulo RSA (pubblico di Domenico) ---
modulo = """00:d2:8f:3e:9c:c1:b8:23:5e:55:7b:c1:e0:c0:ac:
    17:a6:4e:43:7f:2e:a1:7c:d9:b0:58:d6:37:96:cc:
    74:33:88:9c:32:8e:8f:82:b7:9e:fb:e8:ab:b1:12:
    20:d0:e5:61:74:b0:84:60:91:d5:7d:89:3e:e7:39:
    ... (accorciato) ...
    26:55"""
modulo = modulo.replace(" ", "").replace(":", "").replace("\n", "")
modulo = int(modulo, 16)

# --- Esponente pubblico RSA (fissato a 3) ---
e = 3

# --- Messaggio da cifrare ---
plain_text = int("daje roma daje".encode("utf-8").hex(), 16)

# --- Cifro con RSA ---
messaggio_cifrato_rsa = pow(plain_text, e, modulo)

# --- AES: padding ---
def pad(text):
    while len(text) % 16 != 0:
        text += " "
    return text

# --- AES: cifratura ---
def encrypt(plain_text, key):
    cipher = AES.new(pad(key).encode("utf-8"), AES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad(plain_text).encode("utf-8"))
    return base64.b64encode(encrypted_text).decode("utf-8")

# --- Chiave AES condivisa (uguale per te e Domenico) ---
key = "itscybersecurity"  # 16 caratteri

# --- Cifro il messaggio RSA con AES ---
messaggio_cifrato_aes = encrypt(str(messaggio_cifrato_rsa), key)

# --- Invio (simulazione: salvo su file) ---
with open("messaggio.txt", "w") as f:
    f.write(messaggio_cifrato_aes)

print("Mittente: messaggio cifrato con RSA+AES e inviato a Domenico")
