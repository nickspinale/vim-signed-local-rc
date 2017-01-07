from slrc.test.util import from_here
from slrc.persist import check_pub_key, untrust_pub_key, trust_pub_key


def test():
    untrust_pub_key(from_here('pub.pem'))
    assert not check_pub_key(from_here('pub.pem'))
    trust_pub_key(from_here('pub.pem'))
    assert check_pub_key(from_here('pub.pem'))
    untrust_pub_key(from_here('pub.pem'))
    assert not check_pub_key(from_here('pub.pem'))
    trust_pub_key(from_here('pub.pem'))
    assert check_pub_key(from_here('pub.pem'))
    print 'pass'


if __name__ == '__main__':
    test()
