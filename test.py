import random
import string

def generate_random_id(length=16):
    characters = string.ascii_letters + string.digits
    random_id = ''.join(random.choice(characters) for i in range(length))
    return random_id

random_id2 = generate_random_id()
print(random_id2)