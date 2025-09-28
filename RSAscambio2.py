
modulo = """00:a9:b7:3f:a8:47:39:9e:96:87:1a:dc:ab:2f:43:
    52:41:bf:04:b1:fb:c6:c2:1e:35:89:05:50:b9:bb:
    68:12:0e:54:4d:fe:69:e8:ca:4a:ae:53:3c:86:64:
    60:29:70:6a:41:59:73:c2:dd:1f:fb:10:e2:fa:a7:
    f2:35:78:41:c4:17:e5:c8:f5:9f:96:73:8b:aa:24:
    1e:98:07:44:a9:7d:4d:93:8b:79:99:f0:70:e2:9f:
    3f:2b:dc:68:c4:4c:3e:c8:19:e6:03:4c:f8:48:3a:
    fa:9c:a8:e8:6e:3b:81:05:c7:31:db:87:a0:96:dc:
    42:1e:b6:23:15:08:f8:51:37:ee:07:f0:d4:16:6b:
    4d:ca:c8:7f:f5:66:44:1f:e4:d8:2a:3a:2f:0e:4b:
    0a:f2:d1:d3:80:35:b3:f0:2e:ba:c3:c7:5a:de:fc:
    68:57:8f:7a:38:aa:63:a9:9d:35:ea:9c:1b:e6:2f:
    d5:55:b8:8c:fc:c7:a3:37:07:c1:2c:88:f1:ef:f5:
    79:a5:5a:e9:4d:a7:b1:45:97:e6:54:2b:59:32:ac:
    cf:5a:a8:16:12:f4:a5:40:aa:c8:9f:a0:33:a3:88:
    89:20:9e:35:d1:e1:ab:00:e3:18:24:b6:35:8c:bb:
    37:85:f5:6c:96:52:dc:cc:a5:7a:5c:a6:9c:b1:2e:
    3f:a7"""

modulo= modulo.replace(":", "").replace(" ", "").replace("\n", "")

modulo= int(modulo, 16)

private_exponent = """71:24:d5:1a:da:26:69:b9:af:67:3d:c7:74:d7:8c:
    2b:d4:ad:cb:fd:2f:2c:14:23:b0:ae:35:d1:27:9a:
    b6:b4:38:33:fe:f1:45:dc:31:c9:8c:d3:04:42:ea:
    c6:4a:f1:80:e6:4d:2c:93:6a:a7:60:97:51:c5:4c:
    23:a5:81:2d:65:43:db:4e:6a:64:4d:07:c6:c2:bf:
    10:04:d8:70:fe:33:b7:b2:51:11:4a:f5:ec:6a:2a:
    1d:3d:9b:2d:88:29:da:bb:ee:ac:dd:fa:da:d1:fc:
    68:70:9a:f4:27:ab:59:2f:76:92:5a:6b:0f:3d:81:
    69:ce:c2:0e:05:fa:e0:ce:de:10:e8:ca:2c:49:42:
    0a:1e:c5:56:dd:dd:bc:b3:c1:c0:7c:2b:af:e1:0e:
    5a:db:b9:43:58:fb:39:7e:c0:bd:06:18:cb:8d:51:
    77:83:d4:a3:94:d5:2d:b0:f7:3e:55:ce:64:d7:a4:
    60:2d:e1:e4:dd:8a:47:03:2a:6b:3f:13:af:9a:78:
    13:e6:0d:0a:70:26:5b:35:16:0e:e6:1a:1b:c3:35:
    c9:e0:7f:be:1e:8c:81:0b:87:34:3c:5f:01:fa:3b:
    3c:5d:17:a6:65:f5:f2:db:d6:56:6c:18:89:d6:32:
    9d:53:ee:1c:a2:36:01:ee:09:10:5c:87:00:90:29:
    bb"""

private_exponent= private_exponent.replace(":", "").replace(" ", "").replace("\n", "")
private_exponent= int(private_exponent, 16)

cifrato= 15107637446876664646532941147774825358051495290673742975345427910129094842542898572250778846258056282051338405063864371008040839931576469690591069095171959364474742051085591578279825281884362841401414889061730331441414771856369615562589860398625

decifrato= pow(int(cifrato), private_exponent, modulo)

length = (decifrato.bit_length() + 7) // 8
msg_bytes = decifrato.to_bytes(length, "big")
plaintext = msg_bytes.decode("utf-8")
print(plaintext)