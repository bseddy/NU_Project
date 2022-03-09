# Import regular expression module

import re

# Print password criteria for a strong password

print('A strong password consists of:')
print('At least 8 total characters')
print('At least 2 capital letters')
print('At least 2 lowercase letters')
print('At least 2 numbers')
print('At least 2 special characters')

# Ask user to input their password and set user_password variable to their input

user_password = input('Enter your password to verify its strength: ')

pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+]).*$"
if re.fullmatch(r'[A-Za-z0-9!@#$%^&*()_+]{8,}', user_password):
    print('Strong')
else:
    print('Weak')
