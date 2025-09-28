
modulo="""00:e6:c7:57:a0:37:5a:35:e7:90:16:4c:01:dc:43:
    20:bd:26:02:bd:a0:db:03:a0:eb:06:bb:1e:93:35:
    0f:f5:ed:97:7c:51:a4:f5:97:89:53:91:d3:ad:16:
    72:ff:fb:b4:15:3e:a2:82:1c:63:2f:d8:20:9f:ff:
    ce:f3:73:f6:39:ce:83:50:1a:34:29:a6:ad:5d:d2:
    8a:a9:c5:c7:ea:36:9b:4c:31:f7:15:c3:87:8c:3c:
    e3:47:10:51:4a:f9:0c:c1:21:63:5e:9e:26:85:b1:
    27:b7:f1:5f:3e:a9:06:19:35:e9:65:6a:b4:44:95:
    bf:bd:b4:c4:30:93:30:3a:c7:74:28:7f:92:2d:8d:
    6f:b6:fd:ba:4b:c0:76:b9:1c:66:89:1e:b5:39:1d:
    db:b7:fc:9a:42:68:8d:f8:27:31:c6:59:6f:c0:9b:
    8b:5d:0b:cb:27:8e:15:0b:fb:db:f3:36:33:fe:67:
    47:cb:ff:3d:de:f3:6b:86:2c:9a:4a:44:f6:78:ff:
    d4:b3:25:58:04:de:ab:f8:8e:b2:61:fa:cf:57:e4:
    cf:80:9b:a5:ef:97:02:0c:20:a0:45:a5:ae:36:1a:
    6e:9d:96:d6:1b:cc:0a:65:35:b2:6a:d7:d3:f4:30:
    30:01:82:d7:70:c9:f4:b7:fc:91:14:90:e9:1e:b8:
    39:85"""

e=3


modulo = modulo.replace(":", "").replace(" ", "").replace("\n", "")

modulo= int(modulo, 16)

plain_text= int("Forza Fiorentina".encode("utf-8").hex(), 16)

cifrato= pow(plain_text, e, modulo )

d= """00:99:da:3a:6a:cf:91:79:45:0a:b9:88:01:3d:82:
    15:d3:6e:ac:7e:6b:3c:ad:15:f2:04:7c:bf:0c:ce:
    0a:a3:f3:ba:52:e1:18:a3:ba:5b:8d:0b:e2:73:64:
    4c:aa:a7:cd:63:7f:17:01:68:42:1f:e5:6b:15:55:
    34:a2:4d:4e:d1:34:57:8a:bc:22:c6:6f:1e:3e:8c:
    5c:71:2e:85:46:cf:12:32:cb:fa:0e:82:5a:5d:7d:
    ec:da:0a:e0:dc:a6:08:80:c0:ec:e9:be:c4:59:20:
    c5:25:4b:94:d4:70:ae:bb:79:46:43:9c:78:2d:b9:
    2a:7e:78:82:cb:0c:ca:d1:d9:08:ed:57:b2:59:53:
    dc:6c:3f:e5:51:ea:c4:06:8f:52:37:f6:14:14:5c:
    ce:78:2b:2f:df:70:de:59:05:c8:24:cf:b7:0b:da:
    ae:29:55:82:27:bc:f3:f7:9b:7a:fd:80:60:e5:76:
    f2:ea:95:7e:f1:63:69:3e:c0:d5:51:82:6f:03:4f:
    42:63:6f:11:bd:75:21:8c:b1:81:60:4a:b6:dd:4c:
    85:d6:bb:b6:d9:41:40:ae:f2:f2:fd:e9:8c:8a:28:
    24:d1:bf:16:d5:2d:6f:b6:49:8a:c5:38:c8:44:5f:
    bc:3b:52:9f:b1:9d:2e:dc:76:76:17:8b:13:a9:fb:
    8e:f3"""

d= d.replace(" ", "").replace("\n", "").replace(":", "")
d_int= int(d, 16)
decifrato= pow(cifrato, d_int, modulo)

length = (decifrato.bit_length() + 7) // 8
msg_bytes = decifrato.to_bytes(length, "big")
plaintext = msg_bytes.decode("utf-8")
print(plaintext)


