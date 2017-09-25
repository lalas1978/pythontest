from Crypto.Cipher import AES
import hashlib
from cryptography.fernet import Fernet
from base64 import b64encode


import os

my_string =3 * "HALLO MEIN NAME IST MIKE"

IV = 16 * '\x00'           # Initialization vector
BLOCK_SIZE = 32
KEY_SIZE = 256  #either 128 or 256

inputfile = "test.txt"




# create a key by using the given password
def create_key(keysize):

    if keysize == 128:
        rnd = os.urandom(100)
        rnd_base64 = b64encode(rnd).decode('utf-8')
        return rnd_base64[:16]

    else:
        rnd = os.urandom(200)
        rnd_base64 = b64encode(rnd).decode('utf-8')
        return rnd_base64[:32]


# padding will refactor the string to a multiple of 8 bytes (by filling it with space-chars
def padding(text):
    while len(text) % BLOCK_SIZE !=0:
        text +=' '
    return text

def unpadding(text):
    return text.rstrip(' ')


def enc_string(text, key):

    encryption_suite = AES.new(key, AES.MODE_CBC, IV)
    encrypted_string = encryption_suite.encrypt(padding(text))

    return encrypted_string.decode('latin1')


def dec_string(enc_text, key):

    decryption_suite = AES.new(key, AES.MODE_CBC, IV)
    plain_text = decryption_suite.decrypt(enc_text.encode('latin1'))



    return unpadding(plain_text.decode('latin1'))



def enc_file(in_file):

    chunk_size = 32

    while True:
        data = in_file.read(chunk_size)
        if not data:
            break
        yield data










key = create_key(KEY_SIZE)

f = open(inputfile, "rb")

count = 1
for piece in enc_file(f):





