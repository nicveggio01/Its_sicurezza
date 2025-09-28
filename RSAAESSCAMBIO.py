from Crypto.Cipher import AES
import base64

# --- Modulo RSA (pubblico di Domenico) ---

modulo="""00:c1:c5:a4:c4:e6:f6:7a:d5:3e:b6:4a:3c:c2:77:
    be:33:8a:87:ea:70:08:c4:92:df:12:37:ba:5c:73:
    e5:66:ef:25:2a:26:f1:9d:b2:32:c8:f5:a7:87:0f:
    7f:b3:17:66:ec:29:37:ff:11:98:6f:a9:9f:90:8d:
    93:57:3d:15:fb:86:34:19:b1:b6:21:47:8b:d6:c9:
    0c:58:ae:44:e3:82:ad:af:a3:37:1a:2a:a9:ef:b3:
    b6:e3:06:b1:26:d1:c1:fc:f0:1d:bf:55:ff:8d:a3:
    41:5a:e5:80:82:c5:aa:2c:17:a8:66:b2:63:2e:fe:
    74:fa:4f:8c:4d:45:66:43:35:af:ba:14:06:46:47:
    b9:75:27:e4:ca:86:e8:db:a3:b9:13:84:06:5d:f7:
    3c:66:e3:77:26:12:76:aa:c1:1c:54:65:25:cd:de:
    db:2b:59:7a:98:74:e8:c0:d7:0e:cf:1d:03:74:bf:
    86:37:88:95:53:a2:34:a4:86:35:20:28:47:18:ff:
    c9:01:51:bb:ff:78:0e:f2:0d:bf:43:27:97:05:d2:
    ff:48:d9:bd:e4:a2:ea:d0:4f:a5:c9:d4:55:f5:76:
    2f:03:2d:c4:8d:4e:da:52:37:8e:6f:70:a7:11:da:
    ec:84:05:01:78:c2:06:2c:d6:81:ee:ec:e1:dc:c2:
    8a:af"""




modulo = modulo.replace(":", "").replace("\n", "").replace(" ", "")
modulo = int(modulo, 16)

# --- Esponente pubblico RSA ---
e = 3

# --- Messaggio in chiaro ---
plain_text = int("bomba sull'allianz stadium".encode("utf-8").hex(), 16)

# --- Cifratura RSA ---
cifrato_rsa = pow(plain_text, e, modulo)

# --- Funzione di padding per AES ---
def pad(text):
    while len(text) % 16 != 0:
        text += " "
    return text

# --- Funzione AES ENCRYPT ---
def encrypt(plain_text, key):
    cipher = AES.new(pad(key).encode("utf-8"), AES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad(plain_text).encode("utf-8"))
    return base64.b64encode(encrypted_text).decode("utf-8")

# --- Chiave AES condivisa ---
key = "niccodomeits0501"  # 16 caratteri

# --- Cifro il risultato RSA con AES ---
cifrato_aes = encrypt(str(cifrato_rsa), key)

with open("mess.txt", "w") as f:
    f.write(cifrato_aes)

print(f" Messaggio inviato correttamente a Domenico:\n{cifrato_aes}")


priv_exponent = """
00:81:2e:6d:d8:99:f9:a7:38:d4:79:86:d3:2c:4f:
    d4:22:5c:5a:9c:4a:b0:83:0c:94:b6:cf:d1:92:f7:
    ee:44:9f:6e:1c:19:f6:69:21:77:30:a3:c5:04:b4:
    ff:cc:ba:44:9d:70:cf:ff:61:10:4a:71:15:0b:09:
    0c:e4:d3:63:fd:04:22:bb:cb:ce:c0:da:5d:39:db:
    5d:90:74:2d:ed:01:c9:1f:c2:24:bc:1c:71:4a:77:
    cf:42:04:76:19:e1:2b:fd:f5:69:2a:39:55:09:17:
    80:e7:43:ab:01:d9:1c:1d:65:1a:ef:21:97:74:a9:
    a3:51:8a:5d:88:d8:ee:d7:77:f5:b8:7b:c5:1e:86:
    98:19:db:f4:5e:7c:d9:9c:78:dd:69:10:62:c0:41:
    94:9f:fe:64:a2:86:01:0a:10:d5:47:56:8d:36:0f:
    f6:09:d2:be:98:7f:31:e9:33:3b:20:5a:7f:df:bd:
    1b:a2:fb:49:5b:13:67:2b:72:76:03:d5:61:d3:9f:
    33:d6:43:e9:ca:20:2b:b3:de:b1:e3:5b:7c:83:5a:
    d8:0c:9f:c6:87:bb:64:88:d8:e1:8c:1f:10:b1:a2:
    6d:c8:67:d1:42:c2:cc:75:74:01:54:de:a4:7c:73:
    12:9a:86:ad:d2:d9:06:a9:67:14:6c:8a:b9:65:b1:
    35:db"""



priv_exponent = priv_exponent.replace(" ", "").replace(":", "").replace("\n", "")

def pad(text):

    while len(text) % 16 != 0:
        text += " "
    return text

def decrypt(encrypted_text, key):

    cipher = AES.new(pad(key).encode("utf-8"), AES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode("utf-8").strip()
    return decrypted_text

key = "niccodomeits0501"

with open("mess.txt", "r") as f:
    messaggio_cifrato_aes = f.read()

messaggio_rsa = decrypt(messaggio_cifrato_aes, key)
priv_exponent= int(priv_exponent, 16)

messaggio_decifrato = pow(int(messaggio_rsa), priv_exponent, modulo)

legnth = (messaggio_decifrato.bit_length() + 7) // 8
msg_bytes = messaggio_decifrato.to_bytes(legnth, "big")
plaintext = msg_bytes.decode("utf-8")

print(plaintext)