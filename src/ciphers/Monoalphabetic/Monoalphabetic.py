from CipherInterface.CipherInterface import CipherInterface, CipherException


class Monoalphabetic(CipherInterface):
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
        self.key = key.upper()
        sum = 0
        self.encdi = {}
        self.decdi = {}
        for index, char in enumerate(self.key):
            sum += (ord(char) - ord('A') + 1)
            self.encdi[chr(index + ord('A'))] = char
            self.decdi[char] = chr(index + ord('A'))
        return sum == (26 * 27) / 2

    def encrypt(self):
        """
        Encrypt the plaintext.
        """
        self.otxt = ""
        for char in self.itxt:
            self.otxt += self.encdi[char]

    def decrypt(self):
        """
        Decrypt the ciphertext.
        """
        self.otxt = ""
        for char in self.itxt:
            self.otxt += self.decdi[char]

    def key_exception(self, key):
        raise CipherException("Invalid key: {}. For the Monoalphabetic Cipher, the key must contain only alphabetic characters".format(key)\
                            + " and each character in the alphabet must be used exactly once. Letters in the alphabet are mapped to the key"\
                            + " based on position in the string. That is, a->index_0, b->index_1, ..., z->index_25.")