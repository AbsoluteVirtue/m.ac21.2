import hmac
from hashlib import blake2b

# It's advised against using blake2 for password security, should use Argon2 instead
# https://www.blake2.net/#qa
# https://github.com/p-h-c/phc-winner-argon2

def encrypt(plaintext, salt_bytes):
    h = blake2b(salt=salt_bytes)
    h.update(plaintext.encode("utf-8"))
    return h.hexdigest()


def verify(plaintext, stored_salt_bytes, stored_hash):
    return hmac.compare_digest(stored_hash, encrypt(plaintext, stored_salt_bytes))
