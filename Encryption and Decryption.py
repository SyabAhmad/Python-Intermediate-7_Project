print("Encryption and Decryption")
import hashlib

textToEncode = 'we are developer because we develop things'

encodingText = hashlib.sha256(textToEncode.encode())

hashHex = encodingText.hexdigest()

print(f"Before Encryption Text\n{textToEncode}")
print(f"After Encryption Text\n{hashHex}")

# this is just the hash version of the text above

#------------------------------------------------------#

from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Create a Fernet object with the key
textKey = Fernet(key)

# Convert the message to bytes before encrypting it
textToEncode1 = "we are developer because we develop things".encode()

# Encrypt the message
afterEncryption = textKey.encrypt(textToEncode1)

# Convert the encrypted message to a string before storing or transmitting it
encryptedMessage = afterEncryption.decode()

# Print the encrypted message
print(encryptedMessage)

# Decrypt the message
afterDecryption = textKey.decrypt(afterEncryption)

# Convert the decrypted message to a string
decryptedMessage = afterDecryption.decode()

# Print the decrypted message
print(decryptedMessage)