Password Manager
This is a simple password manager program that allows you to store and retrieve passwords encrypted using Fernet symmetric encryption.

Features
Add new passwords
View existing passwords
Encryption using Fernet with a master password-derived key
Passwords stored in plaintext password.txt file
Usage
Run the python script
Enter a master password when prompted
Choose to 'add' or 'view' passwords
To add, enter a name and password to store
To view, existing names and decrypted passwords are shown
Enter 'q' to quit
Installation
Requires Python 3 and the following dependency:


Copy code
pip install cryptography
Security
This program demonstrates a basic password manager but lacks adequate security for real usage. Passwords are encrypted but the key derivation is weak and storage is insecure.

Do not use this as your actual password manager.

Improvements
Some ways this can be improved include:

More secure key derivation
Encrypted database storage
Input validation
Delete passwords
Backup/export passwords
Exception handling
License
This project is open source and licensed under the MIT license.

Contact
Let me know if you have any questions or suggestions to improve this password manager demo!
