from cryptography.fernet import Fernet

#---------------GENERATING KEY-------------------
# key = Fernet.generate_key()
# print(key)

# file = open('key.key', 'wb')
# file.write(key) #key is of type 'bytes'
# file.close()

#---------------RETRIEVING KEY--------------------
file = open('key.key', 'rb')
key = file.read() #key is of type 'bytes'
file.close()
#print(key)

#---------------ENCODING MESSAGE------------------
message = "This is my secret message :)"
encoded = message.encode()

#---------------ENCRYPTING MESSAGE----------------
f = Fernet(key)
encrypted = f.encrypt(encoded)
#print(encrypted)


#----------GETTING THE STORED 'KEY' BACK----------
file = open('key.key', 'rb')
key_new = file.read()
file.close()

#----------------DECRYPTING MESSAGE----------------
f2 = Fernet(key_new)
decrypted = decrypted = f2.decrypt((encrypted)) #This line is valid and we need to do "decrypted = " only once
actual_message = decrypted.decode()
print(actual_message)


