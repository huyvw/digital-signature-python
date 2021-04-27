import hashlib
import hmac


class DigitalSignature:
    __data: bytes
    __secret: bytes
    __encode: str

    def __init__(self,
                 data: str,
                 secret: str,
                 encode='utf-8'):
        self.__encode = encode
        self.__data = bytes(data, self.__encode)
        self.__secret = bytes(secret, self.__encode)

    def get_signature(self):
        signature = self.__calculate_hmac(secret=self.__secret,
                                          data=self.__data)

        return signature.hexdigest()

    @staticmethod
    def __calculate_hmac(secret: bytes,
                         data: bytes,
                         algorithm=hashlib.sha256):
        return hmac.new(secret, data, algorithm)
