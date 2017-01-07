import os.path
from slrc.test.util import from_here
from slrc.crypto import sign_file, verify_file, read_sig


def test():
    try:
        assert verify_file(from_here('pub.pem'), from_here('foo.txt'), from_here('foo.sig'))
        sign_file(from_here('priv.pem'), from_here('foo.txt'), 'test.sig')
        assert read_sig(from_here('foo.sig')) == read_sig('test.sig')
        print 'pass'
    finally:
        os.remove('test.sig')


if __name__ == '__main__':
    test()
