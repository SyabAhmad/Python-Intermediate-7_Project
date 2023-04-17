# ```#1 URL Shortener```
A command-line tool that shortens URLs to make them more manageable and easy to share. Users can input a long URL, and the program generates a short URL that redirects to the original URL.

## ```pyshorteners```
is a Python library that provides a simple and easy-to-use interface to various URL shortening services. It allows you to shorten URLs using popular services such as bit.ly, tinyurl.com, and many others.

To install ```pyshorteners```, you can use pip, the package manager for Python. Simply run the following command in your terminal:

## ```pip install pyshorteners```

Once installed, you can use pyshorteners in your Python code to shorten URLs. Here's an example:

```python runable
import pyshorteners

s = pyshorteners.Shortener()
short_url = s.tinyurl.short('https://www.example.com/some/long/url')
print(short_url)
```
This code creates a Shortener object and then uses the tinyurl service to shorten the URL https://www.example.com/some/long/url. The shortened URL is then printed to the console.

pyshorteners supports many other services as well, including bit.ly, is.gd, and t.co, among others.

You can use these services by simply replacing tinyurl with the service of your choice, like this:

```short_url = s.bitly.short('https://www.example.com/some/long/url')```

In addition to shortening URLs, pyshorteners also supports expanding shortened URLs, as well as other URL-related functionality such as checking if a URL is valid and extracting the domain name from a URL.

Overall, pyshorteners is a useful Python library for working with URLs and can save you time and effort when dealing with long URLs in your code.

# ```#2 Text Encryption and Decryption```
A command-line tool that allows users to encrypt and decrypt text messages using a variety of encryption algorithms, such as AES, RSA, or Blowfish. Users can input a message and a key, and the program encrypts or decrypts the message using the chosen algorithm.

This project aims to provide a simple implementation of encryption and decryption in Python using the hashlib and cryptography libraries.
It allows you to encrypt and decrypt data using various encryption algorithms and hash functions.

# ```Requirements```
To run this project, you will need the following Python packages:

hashlib

cryptography

You can install them using pip:

```pip install hashlib cryptography```

Usage
To use this project, you can import the encryption.py file into your Python project and use the functions provided.

```Hash Functions```

This project provides the following hash functions:

SHA-256

SHA-384

SHA-512

To use a hash function, simply call the hash_data function and pass in the data you want to hash and the hash function you want to use:

```python
import encryption

data = "Hello, World!"
hashed_data = encryption.hash_data(data, "sha256")
print(hashed_data)

```

# ```Encryption Algorithms```

This project provides the following encryption algorithms:

AES-128

AES-192

AES-256

To encrypt data, call the encrypt_data function and pass in the data you want to encrypt, the encryption key, and the encryption algorithm you want to use:

```python
import encryption

data = "Hello, World!"
key = "my_secret_key"
encrypted_data = encryption.encrypt_data(data, key, "aes256")
print(encrypted_data)

```

To decrypt data, call the decrypt_data function and pass in the encrypted data, the encryption key, and the encryption algorithm you used to encrypt the data:


```python
import encryption

encrypted_data = "encrypted data"
key = "my_secret_key"
decrypted_data = encryption.decrypt_data(encrypted_data, key, "aes256")
print(decrypted_data)

```










# ```#3 Password Manager```
A command-line tool that securely stores and manages user passwords. Users can add, delete, and retrieve passwords, and the program encrypts and decrypts the passwords using a chosen encryption algorithm.

# ```#4 Data Visualization```
A command-line tool that visualizes data in a variety of formats, such as bar charts, line charts, or scatter plots. Users can input data in a CSV or Excel file, and the program generates the corresponding visualization.

# ```#5 Currency Converter```
A command-line tool that converts between different currencies, using exchange rates fetched from an API. Users can input an amount in one currency, and the program converts it to another currency based on the current exchange rate.

# ```#6 Password Strength Checker```
A command-line tool that checks the strength of a password and provides feedback on how to make it stronger. Users can input a password, and the program evaluates its strength based on factors such as length, complexity, and usage of common patterns.

# ```#7 To-do List```
A command-line tool that allows users to manage a todo list, including adding, deleting, and updating tasks. Users can input tasks and deadlines, and the program displays the tasks in a user-friendly format. The todo list is stored in a database or file for persistence.