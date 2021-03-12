import hashlib

BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def hash160(s):
    '''sha256 followed by ripemd160'''
    return hashlib.new('ripemd160', hashlib.sha256(s).digest()).digest()


def hash256(s):
    '''two rounds of sha256 : cf. birthday attack '''
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()

def encode_base58(s):
    #On détermine combien de bytes nuls on veut au début (b'\x00') de s
    count = 0
    for c in s:
        if c ==0:
            count +=1
        else:
            break
    #On convertit en un entier "big endian"
    num = int.from_bytes(s, 'big')
    prefix = '1' * count
    result = ''
    while num >0:
        num, mod = divmod(num, 58)
        result = BASE58_ALPHABET[mod] + result
    return prefix + result

def encode_base58_checksum(s):
    return encode_base58(s + hash256(s)[:4])

def decode_base58(s):
    num = 0
    for c in s:
        num *= 58
        num += BASE58_ALPHABET.index(c)
    combined = num.to_bytes(25, bytorder='big')
    checksum = combined[-4:]
    if hash256(combined[:-4])[:4] != checksum:
        raise ValueError('bad adress: {} {}'.format(checksum,hash256(combined[:-4])[:4]))
    return combined[1:-4]

def little_endian_to_int(b):
    """
    Expliquer ce que ça fait
    """
    return int.from_bytes(b, 'little')

def int_to_little_endian(n, length):
    """
    Expliquer ce que ça fait
    """
    return n.to_bytes(length, 'little')


def read_varint(s):
    '''read_varint reads a variable integer from a stream''' 
    i = s.read(1)[0]
    if i == 0xfd:
        # 0xfd means the next two bytes are the number
        return little_endian_to_int(s.read(2))
    elif i == 0xfe:
        # 0xfe means the next four bytes are the number
        return little_endian_to_int(s.read(4))
    elif i == 0xff:
        # 0xff means the next eight bytes are the number
        return little_endian_to_int(s.read(8))
    else:
        # anything else is just the integer
        return i


def encode_varint(i):
    '''encodes an integer as a varint''' 
    if i<0xfd:
        return bytes([i])
    elif i < 0x10000:
       return b'\xfd' + int_to_little_endian(i, 2)
    elif i < 0x100000000:
       return b'\xfe' + int_to_little_endian(i, 4)
    elif i < 0x10000000000000000:
       return b'\xff' + int_to_little_endian(i, 8)
    else:
        raise ValueError('integer too large: {}'.format(i))



#nb1 = b'7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d'
#nb2 = b'ff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c'
#nb3 = b'c7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6'

#print("encode")
#print(encode_base58(nb1))
#print(encode_base58(nb2))
#print(encode_base58(nb3))

