from .base import CipherInterface, CipherException


class Vigenere(CipherInterface):
    def __init__(self, key="", ifil="", ofil="", mode=""):
        super().__init__(key=key, ifil=ifil, ofil=ofil)
        self.encrypt() if mode=="ENC" else self.decrypt()
        self.write_output()

    def setKey(self, key):
        """
        Sets the key to use for the cipher

        :param str key: The key to use
        :return: True if key is valid, False otherwise
        """
        pass

    def encrypt(self):
        """
        Encrypt the plaintext.
        """
        pass

    def decrypt(self):
        """
        Decrypt the ciphertext.
        """
        pass

    def key_exception(self, key):
        # Add custom exception.
        # raise CipherException("")
        pass