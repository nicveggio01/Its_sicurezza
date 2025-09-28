
e= 3

modulo=  """00:b7:8b:2e:11:aa:bc:91:b3:ca:3d:61:94:c6:67:
    5b:bc:e1:36:14:35:0c:b8:34:29:7e:b9:55:0b:96:
    ba:b9:f4:f3:ec:d4:cb:d1:25:dd:ea:5d:86:2d:b5:
    1a:6e:31:b2:aa:c9:34:ee:11:26:0d:06:86:61:7c:
    32:b2:35:f0:c4:fa:cf:c3:3c:26:fb:bb:fb:21:78:
    63:9e:dc:75:9a:52:a9:3e:a2:2d:7b:23:3a:8f:a8:
    fc:d5:fa:a2:0b:b1:b6:58:c5:16:4f:5b:99:04:90:
    fc:2f:76:60:7c:9e:50:81:6e:b0:d1:71:ee:7b:5e:
    dc:f8:9d:d8:cb:00:02:48:da:a4:94:14:36:41:88:
    82:60:7f:02:54:6d:f2:d9:59:a9:1e:29:8d:61:73:
    9e:52:c3:85:bc:d0:fb:2d:8a:14:da:90:4b:c4:b3:
    2e:24:9e:9c:ee:30:43:2d:12:82:0e:bf:e4:b4:8a:
    18:8b:ab:35:f8:d1:5d:83:f2:33:cd:e3:aa:ab:3f:
    a5:a7:4b:c3:ab:ce:b8:55:c7:19:f1:37:9a:4f:2b:
    3c:05:71:d1:33:4f:f0:72:bb:39:f2:56:d3:fd:ac:
    d6:44:96:92:c7:54:12:a9:c3:b4:cb:39:e3:38:8f:
    ce:04:0b:ba:18:66:a5:36:ca:1d:2d:dc:98:8f:9d:
    25:bb"""

modulo= modulo.replace(":", "").replace(" ", "").replace("\n", "")

modulo= int(modulo, 16)

plain_text= int("sergio è gay".encode("utf-8").hex(), 16)

cifrato= pow(plain_text, e, modulo)

print(cifrato)

private_exponent = "7a5cc9611c7db677dc28ebb88444e7" +\
    "d340ceb8235dd022c6547b8e07b9d1" +\
    "d14df7f33887e0c3e946e9041e78bc" +\
    "4976771c86234960c408af0440fd77" +\
    "21794b2dfc8a822819fd27fcc0faed" +\
    "1492f9118c70d46c1e52177c5fc5fd" +\
    "e3fc6c07cbcee5d8b98a3d10adb5fd" +\
    "74f995a8698b00f475e0f69efce9e8" +\
    "a5be90875556db3b4beee1eca694fb" +\
    "664fe2680b118a553a6c795a5a7c46" +\
    "e32564e4e837aed846e83dbab37b8e" +\
    "2b8da5412bccd542cef3d1908567e3" +\
    "7192a3f142c2174bbb38ad9739c031" +\
    "601bee332532262ebcc8f065682ef1" +\
    "b3e361a5c9c025d69182b4fc81a1af" +\
    "dcc4167e5d216b4ac353552b4a5cbd" +\
    "4b4af1a075fec3364e15cccdbef3d5" +\
    "fb"

private_exponent= int(private_exponent, 16)

decifrato= pow(cifrato, )