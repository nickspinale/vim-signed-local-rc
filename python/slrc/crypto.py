from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 
from Crypto.Hash import SHA256 

from binascii import hexlify, unhexlify


def read_key(path):
    with open(path, 'r') as f:
        return RSA.importKey(f.read())


def read_sig(path):
    with open(path, 'r') as f:
        return unhexlify(f.read())


def write_sig(path, sig):
    with open(path, 'w') as f:
        f.write(hexlify(sig))


def sha256_file(path):
    with open(path, 'rb') as f:
        ctx = SHA256.new()
        for chunk in iter(lambda: f.read(4096), b''):
            ctx.update(chunk)
        return ctx


def sign(priv_key, data):
    return PKCS1_v1_5.new(priv_key).sign(data)


def verify(pub_key, data, sig):
    return PKCS1_v1_5.new(pub_key).verify(data, sig)


def sign_file(priv_key_path, file_path, sig_path_out):
    priv_key = read_key(priv_key_path)
    digest = sha256_file(file_path)
    sig = sign(priv_key, digest)
    write_sig(sig_path_out, sig)


def verify_file(pub_key_path, file_path, sig_path):
    pub_key = read_key(pub_key_path)
    digest = sha256_file(file_path)
    sig = read_sig(sig_path)
    return verify(pub_key, digest, sig)
