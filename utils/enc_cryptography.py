from cryptography.fernet import Fernet


_KEY = Fernet.generate_key()


def encrypt(plainbytes):
    return Fernet(_KEY).encrypt(plainbytes)


def decrypt(hash):
    return Fernet(_KEY).decrypt(hash).decode("utf-8")
