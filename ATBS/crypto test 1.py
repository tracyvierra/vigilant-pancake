#cryptography test 1 -- from webpage https://www.tutorialspoint.com/how-to-encrypt-and-decrypt-data-in-python
from cryptography.fernet import Fernet
key = Fernet.generate_key()
print("Key : ", key.decode())
f = Fernet(key)
encrypted_data = f.encrypt(b"This message is being encrypted and cannot be seen!")
print("After encryption : ", encrypted_data)
decrypted_data = f.decrypt(encrypted_data)
print(decrypted_data)
print("After decryption : ", decrypted_data.decode())
