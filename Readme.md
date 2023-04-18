#List Of Projects
## ```1 URL Shortener```

## ```2 Text Encryption and Decryption```

## ```3 Password Manage```

## ```4 Data Visualization```

## ```5 Currency Converter```

## ```6 Password Strength Checker```

## ```7 To-do List```

 
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

The program provides a simple menu for the user to choose from:

###```➡ Add Password```

###```➡ View Database```

###```➡ Search by Account Name```


##```➡ Add Password```

This option allows the user to enter an account name and password, which are then saved to the text file. The program will append the new account name and password to the end of the file.

##```➡ View Database```

This option allows the user to view all the account names and passwords saved in the text file.

##```➡ Search by Account Name```

This option allows the user to search for a specific account by name. If the account is found, the program will display the account name and password. If the account is not found, the program will display a message indicating that the account does not exist.

The program uses exception handling to catch any errors that may occur during file input/output operations.

To run this program, the user needs to have Python installed on their computer. The required packages for this program are already included in Python standard library, so no additional package installation is required.






# ```#4 Data Visualization```
A command-line tool that visualizes data in a variety of formats, such as bar charts, line charts, or scatter plots. Users can input data in a CSV or Excel file, and the program generates the corresponding visualization.

This repository provides examples of how to visualize data using Python's popular data visualization libraries, including Matplotlib and Pandas. The examples cover various types of plots such as line plots, scatter plots, histograms, and box plots.

## ```Installation```

To run the examples, you will need to install the following Python libraries:

➡ pandas

➡ numpy

➡ matplotlib

➡ openpyxl

You can install these libraries using pip, the Python package manager. For example:

```python
pip install pandas numpy matplotlib openpyxl

```
## ```Usage```

To run the examples, simply run the Python scripts provided in the repository. Each script contains example code for a specific type of plot.

## ```Contributing```

Contributions are welcome! If you have a new example to add or want to improve an existing one, please open a pull request.

# ```#5 Currency Converter```

A command-line tool that converts between different currencies, using exchange rates fetched from an API. 

Users can input an amount in one currency, and the program converts it to another currency based on the current exchange rate.

This Python program allows you to convert a given amount from one currency to another using the ```apilayer.net``` API. 

The program prompts the user to enter the base currency, target currency, and amount to convert. It then sends a ```request``` to the API to get the exchange rate between the two currencies and uses it to calculate the converted amount. The result is then printed on the console.

To use this program, you will need an ```API key``` from apilayer.net. Once you have obtained the key, replace the "Your API Key Here" placeholder in the code with your actual key.



# ```#6 Password Strength Checker```
A command-line tool that checks the strength of a password and provides feedback on how to make it stronger. Users can input a password, and the program evaluates its strength based on factors such as length, complexity, and usage of common patterns.

This is a Python program that checks the strength of a given password based on a set of criteria. The program calculates a score for the given password and returns the strength level based on that score. The strength levels are: Very Weak, Weak, Moderate, Strong, and Very Strong.

Criteria Used for Password Strength Calculation

➡ Length of the password

➡ Presence of uppercase letters

➡ Presence of lowercase letters

➡ Presence of digits

➡ Presence of special characters

##```How to Use```

Clone this repository or download the Password Strength Checker.py file.

Open the file in your Python editor.

Run the program.

Enter the password you want to check the strength for.

The program will return the strength level of the given password.

```python
print(check_password_strength("password")) # Very Weak
print(check_password_strength("WeakPassword")) # Weak
print(check_password_strength("Password123")) # Moderate
print(check_password_strength("StrongPass123!")) # Very Strong

```


# ```#7 To-do List```
A command-line tool that allows users to manage a todo list, including adding, deleting, and updating tasks. Users can input tasks and deadlines, and the program displays the tasks in a user-friendly format. The todo list is stored in a database or file for persistence.

The code provided implements a command-line program that manages a to-do list. The program allows the user to add, remove, display, mark as completed, and sort tasks in the list.

The main() function is the entry point of the program and presents the user with a menu of options to choose from. The function uses a while loop to keep the program running until the user chooses to quit.

The add_task() function prompts the user to enter a new task and adds it to the tasks list. The remove_task() function prompts the user to enter a task to remove and removes it from the tasks list if it exists. The display_tasks() function displays the current list of tasks to the user. The complete_task() function prompts the user to enter a task to mark as completed and updates the corresponding task string with a checkbox. The sort_tasks() function sorts the tasks list in ascending order.

To run the program, simply run the script in a terminal or command prompt window. The program will display the main menu and prompt the user to choose an option. The user can enter a number corresponding to the desired option and the program will execute the corresponding function. The program will continue to display the main menu until the user chooses to quit by entering option 6.


if you have any query please feel free to contact me or pull request

Thank you and Happy Coding!!