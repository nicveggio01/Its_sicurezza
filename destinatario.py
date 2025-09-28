from Crypto.Cipher import AES
import base64

# --- Modulo RSA (uguale al mittente) ---
modulo = """00:d2:8f:3e:9c:c1:b8:23:5e:55:7b:c1:e0:c0:ac:
    17:a6:4e:43:7f:2e:a1:7c:d9:b0:58:d6:37:96:cc:
    74:33:88:9c:32:8e:8f:82:b7:9e:fb:e8:ab:b1:12:
    20:d0:e5:61:74:b0:84:60:91:d5:7d:89:3e:e7:39:
    ... (accorciato) ...
    26:55"""
modulo = modulo.replace(" ", "").replace(":", "").replace("\n", "")
modulo = int(modulo, 16)

# --- Esponente privato RSA (segreto di Domenico) ---
priv_exponent = """00:8c:5f:7f:13:2b:d0:17:94:38:fd:2b:eb:2b:1d:
    65:19:89:82:54:c9:c0:fd:e6:75:90:8e:cf:b9:dd:
    a2:cd:05:bd:77:09:b5:01:cf:bf:52:9b:1d:20:b6:
    ... (accorciato) ...
    20:f3"""
priv_exponent = priv_exponent.replace(" ", "").replace("\n", "").replace(":", "")
priv_exponent = int(priv_exponent, 16)

# --- AES: padding ---
def pad(text):
    while len(text) % 16 != 0:
        text += " "
    return text

# --- AES: decifratura ---
def decrypt(encrypted_text, key):
    cipher = AES.new(pad(key).encode("utf-8"), AES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode("utf-8").strip()
    return decrypted_text

# --- Chiave AES condivisa ---
key = "itscybersecurity"

# --- Ricevo (simulazione: leggo file) ---
with open("messaggio.txt", "r") as f:
    messaggio_cifrato_aes = f.read()

# --- 1) Decifra AES (ottengo messaggio RSA come intero in stringa) ---
messaggio_rsa = decrypt(messaggio_cifrato_aes, key)

# --- 2) Decifra RSA ---
messaggio_decifrato = pow(int(messaggio_rsa), priv_exponent, modulo)

# --- 3) Converte da intero a stringa ---
length = (messaggio_decifrato.bit_length() + 7) // 8
msg_bytes = messaggio_decifrato.to_bytes(length, "big")
plain_text = msg_bytes.decode("utf-8")

print("Domenico ha ricevuto:", plain_text)
