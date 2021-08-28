from cryptography.fernet import Fernet

key=Fernet.generate_key()

fernet= Fernet(key)
message='root'

encmessage=fernet.encrypt(message.encode())

decmessage=fernet.decrypt(encmessage).decode()
print(key)
print(key.decode())
print(message)
print(encmessage)
print(encmessage.decode())
print(decmessage)