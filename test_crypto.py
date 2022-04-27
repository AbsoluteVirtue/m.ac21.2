import os
from utils import gen_hashlib as gen, enc_cryptography as crypt


if __name__ == '__main__':

    passw = "qwerty1234"
    salt = os.urandom(16)

    # 1. encrypt
    hash = gen.encrypt(passw, salt)
    hashed_salt_bytes = crypt.encrypt(salt)

    # 2. verify
    reversed_salt = crypt.decrypt(hashed_salt_bytes)
    print(gen.verify(passw, reversed_salt, hash))
