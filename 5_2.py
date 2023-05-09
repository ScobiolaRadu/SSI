#a
import secrets
import string

alphabet = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabet) for i in range(10))
print(password)

#b
alphabet = string.ascii_letters + string.digits + '-_'
url = ''.join(secrets.choice(alphabet) for i in range(32))
print(url)

#c
alphabet = string.hexdigits
token = ''.join(secrets.choice(alphabet) for i in range(32))
print(token)

#d
print(secrets.compare_digest('abc', 'abc'))
print(secrets.compare_digest('abdsadasdfafc', 'absadasfgadfaasfscd'))

#e
key = secrets.token_bytes(32)
print(key)

#f
import bcrypt

password = b"password"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)



