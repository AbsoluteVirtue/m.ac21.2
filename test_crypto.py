from utils import gen_hashlib as gen, enc_cryptography as crypt, misc


if __name__ == '__main__':
    key = crypt.Fernet.generate_key()
    passw = "qwerty1234"
    salt = misc.random_str(16).encode("utf-8")

    # 1. encrypt
    hash = gen.encrypt(passw, salt)

    hashed_salt = crypt.encrypt(key, salt)

    # 2. verify
    reversed_salt = crypt.decrypt(key, hashed_salt)

    print(gen.verify(passw, reversed_salt, hash))
