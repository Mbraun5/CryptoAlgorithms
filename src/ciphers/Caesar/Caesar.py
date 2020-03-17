from CipherInterface.CipherInterface import CipherInterface, CipherException


class Caesar(CipherInterface):
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
        if not key.isdigit():
            return False
        self.key = int(key) % 26
        return True

    def encrypt(self):
        """
        Encrypt the plaintext.
        """
        self.otxt = ""
        for char in self.itxt:
            self.otxt += chr(((ord(char) - ord('A') + self.key) % 26) + ord('A'))

    def decrypt(self):
        """
        Decrypt the ciphertext.
        """
        self.otxt = ""
        for char in self.itxt:
            if ord(char) - ord('A') - self.key >= 0:
                self.otxt += chr(ord(char) - ord('A') - self.key + ord('A'))
            else:
                self.otxt += chr(ord(char) - ord('A') - self.key + ord('A') + 26)

    def key_exception(self, key):
        raise CipherException("Invalid key: {}. Caesar cipher key must be a single integer value such as `343`".format(key))