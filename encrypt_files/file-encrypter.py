from cryptography.fernet import Fernet

#---------------RETRIEVING KEY--------------------
file = open('key.key', 'rb')
key = file.read() #key is of type 'bytes'
file.close()

# #open file to encrypt
# with open('test.txt', 'rb') as f:
#     data = f.read()

# fernet = Fernet(key)
# encrypted = fernet.encrypt(data)

# #Write encrypted file
# with open('test.txt.encrypted', 'wb') as f:
#     f.write(encrypted)


#---------------DECRYPTER----------------
with open('test.txt.encrypted', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

#Write encrypted file
with open('test.txt.decrypted', 'wb') as f:
    f.write(encrypted)
