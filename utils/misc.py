import random


allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_*!@#$%^&*()+="


def random_str(length):
    return ''.join(random.choices(allowed_chars, k=length))
