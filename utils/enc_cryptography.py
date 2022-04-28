from cryptography.fernet import Fernet


_key =b'qGw52Hd9-klQ-5jx45azTIBkk9IvSc20skDTPRTgRmg='


def encrypt(plainbytes):
    return Fernet(_key).encrypt(plainbytes)


def decrypt(hashbytes):
    return Fernet(_key).decrypt(hashbytes)
