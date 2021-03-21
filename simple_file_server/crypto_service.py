from __future__ import unicode_literals
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

_algo = AES
_mode = AES.MODE_EAX
_key = get_random_bytes(16)
_test_key = "0123456789ABCDEF"


def set_key(key):
    global _key
    _key = key


def set_algo(algo, mode):
    global _algo, _mode
    _algo = algo
    _mode = mode


def init(algo, mode, key):
    set_algo(algo, mode)
    set_key(key)


def make_hash(content):
    hl = hashlib.md5()
    hl.update(content)
    hl.update(_key)
    return hl.digest()


def encrypt_data(content):
    """
    @param content:
    @return: Cortege of cipher.nonce, cipher tag, cipher text
    >>> set_key(_test_key); encrypt_data("some text")
    ... #doctest:+ELLIPSIS
    ('...', '...', '...')
    """
    cipher = AES.new(_key, _mode)
    ciphertext, tag = cipher.encrypt_and_digest(content)
    return cipher.nonce, tag, ciphertext
    # file_out = open("encrypted.bin", "wb")
    # [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
    # file_out.close()


def decrypt_data(nonce, tag, ciphertext):
    """
    @return: decrypted text
    >>> set_key(_test_key); \
        decrypt_data('D6\xc8\xcd\xb1b\xf0\xb8s?\xc9[\xea\xf1\x9e=', \
        'U9\xb1;Bez\xa9\xa6\xfdW$\xed\x8e\xccY', '\xd5F~7x\x0b\x08\x06[')
    'some text'
    """
    # nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]
    cipher = _algo.new(_key, _mode, nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)

