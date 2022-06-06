from enum import Enum
from struct import unpack_from, calcsize


class Types(Enum):
    float = "f"
    double = "d"
    uint8 = "B"
    uint16 = "H"
    uint32 = "I"
    uint64 = "Q"
    int8 = "b"
    int16 = "h"
    int32 = "i"
    int64 = "q"
    char = "c"


class BinaryReader():
    def __init__(self, offset, buffer):
        self.offset = offset
        self.buffer = buffer

    def read(self, _pattern):
        pattern = '<' + _pattern.value
        result = unpack_from(pattern, self.buffer, self.offset)
        self.offset += calcsize(pattern)
        return result[0]

    def readWithSize(self, _pattern, size):
        res = []
        for i in range(0, size):
            pattern = '<' + _pattern.value
            result = unpack_from(pattern, self.buffer, self.offset)
            self.offset += calcsize(pattern)
            res.append(result[0])
        return res

    def copy(self, offset):
        return BinaryReader(offset, self.buffer)


def readB(reader):
    b1 = reader.read(Types.uint32)
    b2 = reader.read(Types.uint32)
    b3 = readC(BinaryReader(offset=reader.read(Types.uint32), buffer=reader.buffer))
    return dict(B1=b1, B2=b2, B3=b3)


def readC(reader):
    c1 = reader.read(Types.uint32)
    c2 = reader.read(Types.int16)
    return dict(C1=c1, C2=c2)


def readD(reader):
    d1 = reader.read(Types.int16)
    d2 = []
    for i in range(0, 2):
        d2.append(readE(reader))
    d3 = reader.read(Types.uint64)
    d4 = reader.readWithSize(Types.uint8, 3)
    d5 = reader.read(Types.uint16)
    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5)


def readE(reader):
    e1 = reader.readWithSize(Types.int32, 5)
    e2 = reader.read(Types.double)
    return dict(E1=e1, E2=e2)


def main(buffer):
    reader = BinaryReader(offset=4, buffer=buffer)
    a1 = reader.read(Types.int32)
    a2 = readB(BinaryReader(offset=reader.read(Types.uint16), buffer=reader.buffer))
    a3 = reader.read(Types.int8)
    a4 = readD(reader)
    a5 = reader.readWithSize(Types.float, 5)
    a6 = reader.read(Types.uint16)
    a7 = reader.read(Types.uint64)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7)

print(main(b"UBBE\x1aG_\x1ev\x00\xf2I\xee2\x9e\xea\x97\x16\x16k4H\xb6H\xf4'v."
 b'\x16\xd0t\xc6}\xc4\x0b@\xca\xfby\xe6?G\xf0\xbby\x0f\xb1\xbe\xbe\xcc"\xbf'
 b'\x04\xb3\xba\xc30\xaeM\xdc\x02\x98\x1b\x95\x05\xb6j\xef?\t\xear\xd4$\xb3\x97'
 b"\x05H\x1e\xa8\xfd\xb1h\x7f\xa8>\xf8\xd5:\xbf\xda\xbc\xf9>|'\x91>\xf6|"
 b'\x19?\xf1\xd3Q\x1c\xa1,mK\x97\xc5jy\xfb\x03\x95\x16\xd0\x19\x8b!r\xfe'
 b'\xf6\xbdp\x00\x00\x00'))