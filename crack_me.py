import hashlib

# flag: i don't have a life
FLAG_BYTES = b'91c194d23dce39941df75392fc8755b1ab47c5be'


def source_file_content_bytes() -> bytes:
    with open(__file__, 'r') as f:
        f.readline()
        f.readline()
        f.readline()
        f.readline()
        f.readline()
        return f.read().encode('utf-8')


def get_flag() -> bytes:
    return hashlib.sha256(source_file_content_bytes()).digest()


def xor_encrypt(flag: bytes, key: bytes) -> bytes:
    result = b''
    for i in range(len(flag)):
        result += bytes([flag[i] ^ key[i % len(key)]])
    return hashlib.sha1(result).hexdigest().encode('utf-8')


def check_flag(flag: bytes) -> bool:
    return flag == FLAG_BYTES


def main() -> None:
    flag = get_flag()
    key = input('Enter key: ').encode('utf-8')
    encrypted_flag = xor_encrypt(flag, key)
    if check_flag(encrypted_flag):
        print('Correct key!')
    else:
        print('Wrong key!')


if __name__ == '__main__':
    main()
