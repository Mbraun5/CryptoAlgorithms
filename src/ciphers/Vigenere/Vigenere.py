from CipherInterface.CipherInterface import CipherInterface, CipherException


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
        if not key.isalpha():
            return False
        while len(key) < len(self.itxt):
            key += key
        self.key = key[:len(self.itxt)].upper()
        return True

    def encrypt(self):
        """
        Encrypt the plaintext.
        """
        self.otxt = ""
        for idx, char in enumerate(self.itxt):
            if ord(char) + ord(self.key[idx]) - ord('A') > ord('Z'):
                self.otxt += chr(ord(self.key[idx]) - (ord('Z') - ord(char)) - 1)
            else:
                self.otxt += chr(ord(char) + ord(self.key[idx]) - ord('A'))

    def decrypt(self):
        """
        Decrypt the ciphertext.
        """
        pass

    def key_exception(self, key):
        raise CipherException("Invalid key: {}. Vigenere cipher key must be a string only containing characters".format(key))