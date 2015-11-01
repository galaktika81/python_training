import string
import random

def random_string(prefix, maxlen):
    # symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])