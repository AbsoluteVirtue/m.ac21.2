from cryptography.fernet import Fernet


_KEY = Fernet.generate_key()


def encrypt(plainbytes):
    return Fernet(_KEY).encrypt(plainbytes)


def decrypt(hashbytes):
    return Fernet(_KEY).decrypt(hashbytes)
