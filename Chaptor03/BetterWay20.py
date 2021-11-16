# Better Way 20
# 예외처리 없이 넘어가야 하는 경우도 있음

from Chaptor03 import make_crc as crc
import struct
import socket


def process(msg):
    crc.makecrctable()
    msgCrc = crc.crc16(msg, msg.__len__())
    quotient = int(msgCrc / 256)
    msgCrcTuple = quotient, msgCrc - (256 * quotient)
    msg += msgCrcTuple
    return msg


def hex2float(num1, num2, num3, num4):
    a = (str(hex((num1 << 8) + num2)))[2:]
    b = (str(hex((num3 << 8) + num4)))[2:]
    try:
        result = struct.unpack('f', struct.pack('i', int(a + b, 16)))[0]
        return round(result, 4)
    except struct.error as e:
        return 0


def gathering(deviceNo):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    s.connect(('localhost', 9999))
    buff = 1024

    msg = [deviceNo, 0x03, 0x2b, 0x05, 0x00, 0x30]
    msg = process(msg)
    s.send(bytes(msg))
    data = s.recv(buff)

    I_R = hex2float(data[0], data[1], data[2], data[3])



# Better Way 21
# https://github.com/ziumdev/apiServer/blob/master/personInOutCheckConnection/connection.py
# 49번째 줄