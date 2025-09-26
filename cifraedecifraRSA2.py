n = int(
    "00d47b12733c93e802f6598beb3466"
    "6488739bf60e82abb341dabd29810a"
    "84ce1393d46c0d53d1b92257a67c4b"
    "3c2d06a521384149007fb232e75959"
    "fb6293fa7b832c7f499dc63d6e5858"
    "0736bfe43bd328bbd7fe360c294f61"
    "bf9b67bed91aba5786e9bf27e9c828"
    "80ca19ee23a1dc516b10bbba065dcd"
    "b9770eef889138d71ae0d0dab80fd1"
    "f90b2a32dae74473cb9a4a52afca02"
    "bfa97e3988ae6fb783d1ce6cabb2d0"
    "645da87673cb29300e2a2ec082d1ba"
    "f80dfe9fbd5866d85f7874e85fc570"
    "a05619a4be30cc8ca1fb43830b683d"
    "42bdafaeef96836dac8e4c327aebf0"
    "ad6d88cef7a204687cf04c880c333a"
    "b28cb7643fc322f256da2557e465f3"
    "3f93", 16
)

e = 65537

M = "Ciao come va?"

# Codifica in int
mi = int(M.encode("utf-8").hex(), 16)

# Cifratura
cifrato = pow(mi, e, n)
print("Cifrato:", cifrato)

d = int(
    "37ed5503e3f40263953828adf612e5"
    "6f4d0ec60b37b5bdef1d8620c08866"
    "405fc2cf6cc96d408c7c4f99d0a974"
    "e35d1665d20acd0e468e3efbc9f6f7"
    "461131230579d6df279a205d44ff96"
    "968097b06f7a0f4760f014ef62a795"
    "e96fbb3a25e0da5cf6758c29eab74e"
    "7ee3a85cd4a3cb02655b2431bccb03"
    "8024fc4374060407e23b3c1940a143"
    "a5cef8edb63797407e4356638b10d8"
    "c40a27929ff769db8de9eda50c3961"
    "61da5f4fcba4bcf0141c9bfe871218"
    "7bf3c9f822e027f70dd5294ea4b23b"
    "e28581a8fd6a75a344bca6c1566646"
    "3b4bc0ec07f210ed5866cf6be7958c"
    "2a515b6dc0751ded56cf4f9d7d31b2"
    "45f91d2389f82777c6b055176f099f"
    "41", 16
)

# DECIFRATURA
decifrato = pow(cifrato, d, n)

# Lunghezza in byte del modulo
lunghezza = (n.bit_length() + 7) // 8

# Conversione dell'intero in bytes
msg_bytes = decifrato.to_bytes(lunghezza, "big")

# Rimuove eventuali zeri iniziali (se usi RSA raw senza padding)
msg_bytes = msg_bytes.lstrip(b'\x00')

# Decodifica in UTF-8
decoded = msg_bytes.decode("utf-8")
print("Decifrato:", decoded)


