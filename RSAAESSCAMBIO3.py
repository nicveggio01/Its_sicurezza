from Crypto.Cipher import AES
import base64



modulo= """00:ab:24:bb:3c:41:94:3a:a9:66:1d:4d:18:0b:ff:
    30:53:45:3a:81:87:4d:a9:4a:08:80:26:ce:f0:a2:
    ac:3c:09:5f:0e:0d:59:b7:ce:4e:a3:ba:5f:03:90:
    9c:2b:82:0d:2c:27:a2:27:3e:2c:1a:6c:9d:a5:b5:
    d2:29:93:0c:55:a3:57:98:3b:7f:53:35:18:3b:9a:
    ab:fa:ac:f1:c5:08:25:60:0c:e7:b9:e0:49:f7:9b:
    56:4d:33:30:fd:ed:8e:ad:57:86:e3:f4:31:e6:37:
    11:b0:21:89:5e:26:ef:3b:97:83:a4:44:20:1b:d3:
    32:2a:38:ee:01:52:a5:4e:8d:48:6b:4d:02:a9:d3:
    68:fa:2b:e7:f0:6a:a6:6d:18:38:14:36:bc:74:e6:
    48:c8:b3:3c:f7:89:f0:1c:e2:fc:c3:39:40:79:a1:
    9b:09:e0:80:fa:e3:7e:7d:5c:86:bf:94:88:5f:da:
    b9:88:b4:29:90:53:71:34:b5:e0:9a:3c:03:f8:fd:
    39:79:be:7c:f5:78:6c:bb:83:d8:e4:4f:34:28:a3:
    0b:60:80:82:dc:36:a8:7d:ff:f8:f6:c6:a8:ac:9e:
    0f:a7:0a:8c:f8:4e:b8:02:17:ae:74:01:45:98:24:
    19:a0:70:4f:82:20:7c:82:1a:a3:94:75:91:70:af:
    27:e3"""

modulo= modulo.replace(":", "").replace(" ", "").replace("\n", "")

modulo= int(modulo, 16)

e= 3

plain_text= int("M.e. è un porco o no?".encode("utf-8").hex(), 16)

messaggio_cifrato_rsa= pow(plain_text, e, modulo)

def pad(text):
    while len(text) % 16 != 0:
        text += " "
    return text

def encrypt(plain_text, key):
    cipher= AES.new(pad(key).encode("utf-8"), AES.MODE_ECB)
    encrypted_text=cipher.encrypt(pad(plain_text).encode("utf-8"))
    return base64.b64encode(encrypted_text).decode("utf-8")

key= "niccodomeits0501"

messaggio_cifrato_aes= encrypt(str(messaggio_cifrato_rsa), key)

with open("mess3.txt", "w") as f:
    f.write(messaggio_cifrato_aes)

    print("Messaggio inviato correttamente a domenico")
