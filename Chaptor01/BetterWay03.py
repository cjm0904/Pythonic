
a = b'h\x65llo'
print(list(a))
print(a)

b = 'a\u0300 propos'
print(list(b))
print(b)


# bytes나 str 인스턴스를 받아서 str로 반환
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


print(repr(to_str(b'foo')))
print(repr(to_str('bar')))
print(repr(to_str(b'\xed\x95\x9c')))


# bytes나 str 인스턴스를 받아서 bytes로 반환
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value


print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))
print(repr(to_bytes('한글')))


assert 'red' > 'blue'


print(b'foo' == 'foo')


print(b'red %s' % b'blue')
print('red %s' % 'blue')
# print(b'red %s' % 'blue') --> 동작 안함
print('red %s' % b'blue')
