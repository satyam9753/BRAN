import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#Changing 'user_password' will change the "key" 
user_password = 'password'
password = user_password.encode()

salt = b'\xc4\x97u\xe3\xdc]\xd5\x7f\xb4\x95%\xe7\x83\xf7\xaeW'

kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), 
                 length=32, salt=salt, 
                 iterations=100000, 
                 backend=default_backend()
                 )

key = base64.urlsafe_b64encode(kdf.derive(password))
print(key)