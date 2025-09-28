from Crypto.Cipher import AES
import base64

modulo = """00:dc:29:f2:f6:3a:73:6a:77:1d:f2:de:d0:e3:84:
    9a:e7:02:ab:51:ea:74:0f:ca:33:78:63:78:3f:5a:
    06:52:81:68:37:4b:8b:68:c5:af:59:4d:bc:ab:69:
    cb:b3:cb:97:ae:a5:78:75:94:4a:a1:be:38:f2:3f:
    db:56:b7:c2:9c:70:a1:f7:11:35:99:60:7c:55:b1:
    e6:87:15:13:83:f0:4e:16:c6:2c:94:0b:4e:d3:ac:
    40:11:de:94:ab:db:b0:10:79:66:2e:b0:3b:9e:eb:
    a8:6f:48:50:f0:25:7b:f6:4e:a6:94:6a:95:d9:01:
    ea:92:0e:db:0c:09:a9:a2:b5:fe:10:ba:1b:15:87:
    ad:51:d7:68:8b:52:74:89:c4:7e:06:3a:a1:9f:6e:
    e0:a2:5d:8a:c3:2c:d7:a2:e7:bb:f3:85:b4:0d:b8:
    72:03:6d:d2:9f:83:42:88:46:5a:11:b1:c0:35:3d:
    80:e5:cc:b6:eb:f2:82:33:db:3e:a8:85:24:1c:9b:
    45:3b:ec:81:b6:9f:a5:97:f8:74:8f:07:53:cf:d1:
    04:d5:9b:5f:4b:bd:b0:0c:2c:d3:76:69:33:7d:97:
    25:ce:56:6d:8f:6c:8e:1b:be:ca:66:9d:3b:9c:5e:
    04:53:b7:ef:35:36:c3:35:56:9c:19:db:90:00:5d:
    c5:33"""

modulo= modulo.replace(" ", "").replace(":", "").replace("\n", "")
modulo= int(modulo, 16)

priv_exponent = """00:92:c6:a1:f9:7c:4c:f1:a4:be:a1:e9:e0:97:ad:
    bc:9a:01:c7:8b:f1:a2:b5:31:77:a5:97:a5:7f:91:
    59:8c:56:45:7a:32:5c:f0:83:ca:3b:89:28:72:46:
    87:cd:32:65:1f:18:fa:f9:0d:87:16:7e:d0:a1:7f:
    e7:8f:25:2c:68:4b:16:a4:b6:23:bb:95:a8:39:21:
    44:5a:0e:0d:02:a0:34:0f:2e:c8:62:b2:34:8d:1d:
    80:0b:e9:b8:72:92:75:60:50:ee:c9:ca:d2:69:f2:
    70:4a:30:35:f5:6e:52:a4:34:6f:0d:9c:63:e6:01:
    47:0c:09:e7:5d:5b:c6:6c:78:17:43:a6:f9:32:34:
    1d:31:7d:e2:bd:ae:7e:89:ee:4f:fa:8d:aa:dc:5e:
    18:66:f1:6a:be:28:f8:32:2c:6e:3a:08:e0:fd:7e:
    d3:58:f9:0c:43:55:a6:fa:b5:ae:d5:1b:8f:60:8a:
    91:a1:36:09:c9:0e:0d:c7:e0:ff:10:1f:6d:4e:80:
    75:2e:a2:02:33:e0:88:ff:1d:53:84:88:c8:c0:d2:
    03:e8:f7:d9:62:bc:1f:1f:7c:f2:b3:48:d4:44:4f:
    89:4f:54:30:7b:e3:17:18:52:0a:b0:fe:77:41:da:
    66:fd:ba:c9:07:d9:1e:e4:f4:28:a2:5e:28:af:4f:
    1f:db"""

priv_exponent= priv_exponent.replace(" ", "").replace(":", "").replace("\n", "")
priv_exponent= int(priv_exponent, 16)

def pad(text):
    while len(text) % 16 !=0:
        text += " "
    return text

def decrypt(encrypted_text, key):
    cipher = AES.new(pad(key).encode("utf-8"), AES.MODE_ECB)
    decrypted_text = (
        cipher.decrypt(base64.b64decode(encrypted_text)).decode("utf-8").strip()
    )
    return decrypted_text

key= "niccodomeits0501"

with open("mess2.txt", "r") as f:
    messaggio_cifrato_aes= f.read()

messaggio_rsa= decrypt(messaggio_cifrato_aes, key)
messaggio_decifrato= pow(int(messaggio_rsa), priv_exponent, modulo)

length=(messaggio_decifrato.bit_length()+7)//8
msg_bytes= messaggio_decifrato.to_bytes(length, "big")
plain_text= msg_bytes.decode("utf-8")

print(f"Messaggio decrptato: {plain_text}")
