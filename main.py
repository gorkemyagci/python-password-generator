import random
import string

numbers = string.digits
symbols = string.punctuation
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
all_characters = [numbers, symbols, lowercase, uppercase]

password = ""

for i in range(15):
    random_characters = random.choice(random.choice(all_characters))
    password += random_characters
    
password = list(password)
random.shuffle(password)
password = ''.join(password)

print(password) # Example: 9!bR8#3z7!2z7#3
