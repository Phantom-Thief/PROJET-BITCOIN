import hashlib
def hash160(s):
    '''sha256 followed by ripemd160'''
    return hashlib.new('ripemd160', hashlib.sha256(s).digest()).digest()


def hash256(s):
    '''two rounds of sha256 : cf. birthday attack '''
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()