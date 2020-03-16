from CipherInterface.CipherInterface import CipherInterface, CipherException
import math


class Railfence(CipherInterface):
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
        self.key = int(key)
        return True

    def encrypt(self):
        """
        Encrypt the plaintext.
        """
        ctl = [[] for _ in range(self.key)]
        for idx, char in enumerate(self.itxt):
            ctl[idx % self.key].append(char)
        self.otxt = "".join(["".join(li) for li in ctl])

    def decrypt(self):
        """
        Decrypt the ciphertext.
        """
        nchr = math.floor(len(self.itxt) / self.key)
        xtr = len(self.itxt) % self.key
        self.otxt = ""
        for idx in range(nchr):
            cnt = xtr
            for row in range(self.key):
                if row == 0:
                    self.otxt += self.itxt[idx]
                elif cnt > 0:
                    self.otxt += self.itxt[idx + (nchr + 1) * row]
                    cnt -= 1
                else:
                    self.otxt += self.itxt[idx + (nchr + 1) * xtr + nchr * (row - xtr)]
        if xtr > 0:
            for idx in range(xtr):
                self.otxt += self.itxt[(nchr + 1) * (idx + 1) - 1]

    def key_exception(self, key):
        raise CipherException("Invalid key: {}. Railfence cipher key must be a single integer such as `12`".format(key))