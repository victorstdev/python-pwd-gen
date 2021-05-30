import os
import random
import string

chars = string.ascii_letters + string.digits + "!@#$%&*()"
seed = os.urandom(1024)
random.seed(seed)

passwords = [''.join(random.choice(chars) for i in range(12)) for j in range(50)]

print(passwords)