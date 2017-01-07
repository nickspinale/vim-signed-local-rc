import os
import os.path
import shutil
from binascii import hexlify

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 
from Crypto.Hash import SHA256 

from slrc.config import get_trusted_dir
from slrc.crypto import read_key, sha256_file


def check_pub_key(pub_key_path):
    trusted_dir = get_trusted_dir()
    if not os.path.isdir(trusted_dir):
        return False
    hash = sha256_file(pub_key_path).digest()
    return hexlify(hash) in os.listdir(trusted_dir)


def trust_pub_key(pub_key_path):
    trusted_dir = get_trusted_dir()
    if not os.path.isdir(trusted_dir):
        os.makedirs(trusted_dir)
    hash = sha256_file(pub_key_path).digest()
    path = os.path.join(trusted_dir, hexlify(hash))
    open(path, 'a')


def untrust_pub_key(pub_key_path):
    trusted_dir = get_trusted_dir()
    if os.path.isdir(trusted_dir):
        hash = sha256_file(pub_key_path).digest()
        path = os.path.join(trusted_dir, hexlify(hash))
        if os.path.isfile(path):
            os.remove(path)
