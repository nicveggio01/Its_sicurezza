
modulo="""00:bc:16:e6:fa:b1:bb:c4:55:02:d2:b0:fa:00:14:
    97:7d:c8:8f:44:a9:8a:63:cd:c0:3e:77:37:4c:c8:
    1c:9e:45:25:dd:dc:28:ad:b9:5c:9b:ca:f5:36:05:
    8d:74:62:08:8c:85:cb:c3:77:d7:84:a7:17:a4:86:
    20:e0:57:16:39:5d:f1:a3:75:62:d6:6c:98:d6:65:
    9d:59:00:c1:0d:25:34:86:2f:6a:fb:f3:5e:eb:51:
    d0:de:c3:58:c3:14:4b:38:97:57:ef:7e:78:e8:f7:
    26:ec:d0:c7:87:3f:23:bc:27:71:31:44:c7:40:3e:
    f9:04:2c:05:98:a9:7d:d3:f8:0f:4d:76:d4:a4:65:
    c0:c4:1b:74:2d:24:e8:34:16:20:ab:c7:12:b1:cc:
    7f:06:cb:8d:de:7f:1f:93:5e:2c:d1:9b:b3:5c:57:
    06:28:19:8c:2d:0b:a8:5e:b6:fd:39:45:ae:6c:b7:
    49:9e:99:7a:d8:23:6f:17:3e:b1:6d:5a:79:c0:8d:
    5b:46:e6:63:57:d2:95:0d:9a:20:c5:f9:f5:b2:a2:
    6c:be:e9:18:52:b9:2b:ac:3c:ab:88:05:c9:2c:76:
    ba:8e:db:d8:b7:62:0b:73:4b:37:e8:40:81:f1:fe:
    45:a0:c6:0c:37:af:1e:02:2a:b6:f6:95:48:d9:eb:
    f1:c5"""

modulo= modulo.replace(":", "").replace(" ", "").replace("\n", "")
modulo=int(modulo, 16)

priv_exponent="""7d:64:99:fc:76:7d:2d:8e:01:e1:cb:51:55:63:0f:
    a9:30:5f:83:1b:b1:97:de:80:29:a4:cf:88:85:68:
    69:83:6e:93:e8:1b:1e:7b:93:12:87:4e:24:03:b3:
    a2:ec:05:b3:03:dd:2c:fa:8f:ad:c4:ba:6d:ae:c0:
    95:8f:64:26:3e:a1:17:a3:97:39:9d:bb:39:99:13:
    90:ab:2b:5e:18:cd:ae:ca:47:52:a2:3f:47:8b:e0:
    94:82:3b:2c:b8:32:25:ba:3a:9f:a9:a5:f0:a4:c4:
    9d:e0:85:04:d4:c2:7d:6f:a0:cb:83:2f:80:29:fb:
    58:1d:59:10:70:fe:8d:4e:e3:70:09:3a:38:10:4b:
    4a:50:ea:e5:cc:79:32:33:9a:05:ff:da:7e:35:87:
    85:cb:63:35:d0:11:af:f8:14:0f:d3:3f:3c:a8:8d:
    e5:d7:a8:9a:4b:8d:3d:27:79:52:cc:41:67:dd:ff:
    08:e1:0e:55:78:4c:b7:36:e9:db:0b:10:ed:d4:b8:
    96:ed:25:2f:bd:63:b1:4d:0e:18:e1:55:a5:17:1f:
    7a:61:b4:2e:77:7e:10:90:91:d7:22:60:12:57:b1:
    3f:d9:c2:d8:38:70:b8:3b:5d:07:7d:ef:f4:be:53:
    57:d6:94:4b:2a:4c:29:9c:1a:a4:a0:54:58:8c:5c:
    6b"""

priv_exponent= priv_exponent.replace(":", "").replace(" ", "").replace("\n", "")
priv_exponent= int(priv_exponent, 16)
with open("mess5.txt", "r") as f:
    cifrato= f.read()
messaggio_decifrato= pow(int(cifrato), priv_exponent, modulo)

length= (messaggio_decifrato.bit_length()+7)//8
msg_bytes= messaggio_decifrato.to_bytes(length, "big")
plaintext= msg_bytes.decode("utf-8")

print(plaintext)

