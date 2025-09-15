
n= "008bde4ffd5351b23869f92394326d" +\
    "ff0768703ac905659e3ed762207fd4" +\
    "455ed0e5f17c2207d1ecec84696ee1" +\
    "59fa953d5a84338711c7f1e344ef8f" +\
    "6589d66ef3ad36a52cc1e34668c0ea" +\
    "dabad2661088323e4f6dd76454452e" +\
    "0210482e5ac247a6ce2949541387cf" +\
    "f1268e498cc0cf6d46c1d7a39d0484" +\
    "9697dab3c7902078bb748962630cdc" +\
    "71b231ed97056c93127f2661c277be" +\
    "5046a2a641de236beb7d248efc0e39" +\
    "fd18fb8a36c0fd055953d8259ddf70" +\
    "ed310d51bc463dd0a802b14b23a2ed" +\
    "33b44c41e5767ca7f614af397c9d8b" +\
    "14be32ec6e0290fe4c119c5ba24232" +\
    "c46738be8fc223ab0c9eafa2531121" +\
    "a95d43c041dd424bc95369ce546043" +\
    "9c69"


decimale= int(n, 16)

M="Forza fiore"

mi= int(M.encode("utf-8").hex(), 16)

print(mi)

e= 3
cifrato= pow(mi, e, decimale)

print(cifrato)


d=    "174fb7ff8de2f30966fedb435dbcff" +\
    "d6916809cc2b90efb523e5b0154e0b" +\
    "8fcd7ba83f5b014da77cc0bc3d258e" +\
    "ff18df8f16089682f6a8508b7d4290" +\
    "ec4e67d347891b8775a5e111757c79" +\
    "c9cdbbad6c085fb7e7a3e60e0b87ab" +\
    "02b6b26475b69bcd06e18e03414d52" +\
    "dbc261977577e78bcaf945ef80c0c3" +\
    "c3f9c8a142b0141efefb2ee80bbb2e" +\
    "ef628b638d29b6f13270cddcfea1d0" +\
    "4c1263e91854a351b968aee658c4da" +\
    "b9f86d8ad8ac98aae7bddfaf57fcf7" +\
    "621aff564474ef7fd0b73819cb116e" +\
    "5345aacd23a519bdf40b2cefa9a8be" +\
    "bf23a15c6cc1d637ac93693d306273" +\
    "b795d1e6e822ed2271d8b7ae6cd00d" +\
    "9c7b4e210fe34724c6a201caae7542" +\
    "c3" 


decimale= int(d, 16)

