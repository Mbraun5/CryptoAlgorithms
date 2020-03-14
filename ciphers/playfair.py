from .base import CipherInterface, CipherException


class Playfair(CipherInterface):
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

    def encrypt(self):
        """
        Encrypt the plaintext. If there are duplicate letters that will be
        passed into the matrix together, append an `X` between them. If the
        duplicate character is a `X`, append a `Z` between them instead. The
        same result holds if the final length of the plaintext is odd.
        """
        i = 0
        while i < len(self.itxt) - 1:
            if self.itxt[i] == self.itxt[i + 1]:
                char = "X" if self.itxt[i + 1] != "X" else "Z"
                self.itxt = self.itxt[:i+1] + char + self.itxt[i+1:]
            i += 2
        if len(self.itxt) % 2 == 1:
            self.itxt += ("X" if self.itxt[-1] != "X" else "Z")
        
        self.otxt = ""
        for i in range(0, len(self.itxt), 2):
            frow = self.charmap[self.itxt[i]][0]
            srow = self.charmap[self.itxt[i+1]][0]
            fcol = self.charmap[self.itxt[i]][1]
            scol = self.charmap[self.itxt[i+1]][1]
            if frow == srow:
                self.otxt += self.matrix[frow][(fcol + 1) % 5]
                self.otxt += self.matrix[srow][(scol + 1) % 5]
            elif fcol == scol:
                self.otxt += self.matrix[(frow + 1) % 5][fcol]
                self.otxt += self.matrix[(srow + 1) % 5][scol]
            else:
                self.otxt += self.matrix[frow][scol]
                self.otxt += self.matrix[srow][fcol]

    def decrypt(self):
        """
        Decrypt the ciphertext.
        """
        self.otxt = ""
        for i in range(0, len(self.itxt), 2):
            frow = self.charmap[self.itxt[i]][0]
            srow = self.charmap[self.itxt[i+1]][0]
            fcol = self.charmap[self.itxt[i]][1]
            scol = self.charmap[self.itxt[i+1]][1]
            if frow == srow:
                self.otxt += self.matrix[frow][(fcol - 1) % 5]
                self.otxt += self.matrix[srow][(scol - 1) % 5]
            elif fcol == scol:
                self.otxt += self.matrix[(frow - 1) % 5][fcol]
                self.otxt += self.matrix[(srow - 1) % 5][scol]
            else:
                self.otxt += self.matrix[frow][scol]
                self.otxt += self.matrix[srow][fcol]

    def key_exception(self, key):
        raise CipherException("Invalid key: {}. Playfair cipher keys must only contain alphabetic characters.".format(key))