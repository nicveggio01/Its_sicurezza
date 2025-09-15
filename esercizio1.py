# Da testo a esadecimale

m = "Hello"
hex_result = m.encode("utf-8").hex()
print(hex_result)

# Funzione inversa


hex_string = "48656c6c6f"
text = bytes.fromhex(hex_string).decode('utf-8')
print(text)

