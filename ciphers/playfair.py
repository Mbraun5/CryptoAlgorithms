from .base import CipherInterface, CipherException


class Playfair(CipherInterface):
    def __init__(self, key="", ifil="", ofil=""):
        super().__init__(key=key, ifil=ifil, ofil=ofil)

    def setKey(self, key):
        """
        Sets the key to use for the cipher

        :param str key: The key to use
        :return: True if key is valid, False otherwise
        """

        self.key = key
        if len(key) < 0 or not key.isalpha():
            return False

        self.matrix = [[], [], [], [], []]
        i = 0
        j = 0
        self.charmap = {}
        for char in str.upper(self.key):
            if j == 5:
                j = 0
                i += 1
            if i == 5:
                break
            if char not in self.charmap:
                if char == "I":
                    self.charmap["J"] = (i, j)
                elif char == "J":
                    self.charmap["I"] = (i, j)
                self.matrix[i].append(char)
                self.charmap[char] = (i, j)
                j += 1
        
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for char in alphabet:
            if j == 5:
                j = 0
                i += 1
            if i == 5:
                break
            if char not in self.charmap:
                if char == "I":
                    self.charmap["J"] = (i, j)
                elif char == "J":
                    self.charmap["I"] = (i, j)
                self.matrix[i].append(char)
                self.charmap[char] = (i, j)
                j += 1
        """ Print for debugging matrix
        for item in self.matrix:
            print(item)
        """
        return True

    def encrypt(self, plaintext):
        """
        Encrypt the plaintext.

        :param str plaintext: The plaintext to encrypt
        :return: The ciphertext
        """
        

    def decrypt(self, ciphertext):
        """
        Decrypt the ciphertext.

        :param str ciphertext: The ciphertext to decrypt
        :return: The plaintext
        """
        pass

    def key_exception(self, key):
        raise CipherException("Invalid key: {}. Playfair cipher keys must only contain alphabetic characters.".format(key))