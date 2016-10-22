#!/usr/bin/python3
import codecs
import base64
class PassThru(codecs.Codec):
    def decode(text):
        return (text, len(text))
    def encode(text):
        return (text, len(text))

class ROT13(codecs.Codec):
    def encode(text):
        return (codecs.encode(text, "rot13"), len(text))
    def decode(text):
        return self.encode(text)

class SwapCase(codecs.Codec):
    def encode(text):
        return (text.swapcase(), len(text))
    def decode(text):
        return self.encode(text)

class Base85(codecs.Codec):
    def encode(text):
        return (str(base64.a85encode(text))[2:-1], len(text))
    def decode(text):
        return (str(base64.a85decode(text))[2:-1], len(text))

class Base64(codecs.Codec):
    def encode(text):
        return (str(base64.b64encode(text))[2:-1], len(text))
    def decode(text):
        return (str(base64.b64decode(text))[2:-1], len(text))

class Base32(codecs.Codec):
    def encode(text):
        return (str(base64.b32encode(text))[2:-1], len(text))
    def decode(text):
        return (str(base64.b32decode(text))[2:-1], len(text))

class Base16(codecs.Codec):
    def encode(text):
        return (str(base64.b16encode(text))[2:-1], len(text))
    def decode(text):
        return (str(base64.b16decode(text))[2:-1], len(text))

global __encoders__
__encoders__  = [PassThru, SwapCase, ROT13, Base16, Base32, Base64]

def obfs(text, proto):
    global __encoders__
    return __encoders__[proto].encode(text)[0]


def deobfs(text, proto):
    global __encoders__
    return __encoders__[proto].decode(text)[0]


def get_proto_count():
    global __encoders__
    return len(__encoders__)
