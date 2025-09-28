

modulo="""00:be:db:77:39:0c:49:1a:0e:7c:42:b1:7d:98:68:
    4d:43:ac:07:50:da:99:41:97:db:06:3d:ce:e3:bb:
    b8:2c:c6:0a:87:3f:23:09:1c:86:32:a7:a7:69:f7:
    6d:69:c5:8b:36:bd:b9:d6:fc:ff:c6:66:3b:a0:b3:
    78:2a:9d:dd:3f:28:85:25:8e:7a:6c:d5:75:fd:fc:
    a5:04:a5:7e:78:71:e9:a1:f6:53:68:d5:a9:37:74:
    d2:85:64:59:f7:3d:7d:39:c7:cf:dd:9c:18:fc:23:
    c0:31:53:12:d7:a5:d8:cc:93:3e:e4:ad:df:80:b3:
    b1:75:1d:68:bb:8d:13:67:30:ba:0e:97:19:c7:d1:
    37:f4:c6:cc:cc:4f:13:dc:82:82:6e:93:94:c5:7e:
    72:98:c1:d8:72:4f:44:f2:95:6b:93:01:bc:99:52:
    52:eb:85:80:54:ee:2d:34:bd:63:84:08:c1:5e:f9:
    86:77:4a:28:e0:ad:98:1d:b2:bb:a6:81:2d:84:60:
    97:10:57:65:dc:50:6d:87:33:a5:40:0c:7a:a8:5b:
    84:2e:02:69:b3:c3:1e:47:d0:9c:ec:f8:8a:07:94:
    d1:06:52:a9:fb:d1:69:f8:3f:9d:41:31:df:9e:80:
    ee:22:c6:5b:63:f4:e0:5f:03:0c:c2:1c:d9:4a:f6:
    73:cf"""

modulo= modulo.replace(":", "").replace(" ", "").replace("\n", "")
modulo= int(modulo, 16)

e= 3
plain_text= int("operazione bomba su prato fiorito".encode("utf-8").hex(), 16)
cifrato= pow(plain_text, e, modulo)

with open("mess4.txt", "w") as f:
    f.write(str(cifrato))
    print("Messaggio correttamente inviato a domenico")
