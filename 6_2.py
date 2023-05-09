from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b'O cheie oarecare'
data = b'testtesttesttesttesttesttesttesttesttesttesttest'

cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(data)
print(ciphertext)

key = b'O cheie oarecare'
data = b'test'
padded_data = pad(data, 16)

cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(padded_data)
print(ciphertext)

key = b'O cheie oarecare'
data = b'testtesttesttesttesttesttesttesttesttesttesttest'

cipher = AES.new(key, AES.MODE_CBC)
ciphertext = cipher.encrypt(data)
print(ciphertext)
