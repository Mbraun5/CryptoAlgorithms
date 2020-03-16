from CipherInterface.CipherInterface import CipherInterface, CipherException
import math


class RowTransposition(CipherInterface):
    def __init__(self, key="", ifil="", ofil="", mode=""):
        super().__init__(key=key, ifil=ifil, ofil=ofil)
        self.encrypt() if mode=="ENC" else self.decrypt()
        self.write_output()

    def check_nums(self):
        res = 0
        for digit in self.key:
            res += digit
        return res == int(len(self.key) * (len(self.key)+1) / 2)

    def setKey(self, key):
        """
        Sets the key to use for the cipher

        :param str key: The key to use
        :return: True if key is valid, False otherwise
        """
        if " " in key:
            self.key = key.split(" ")
            for digit in self.key:
                if not digit.isdigit():
                    return False
            self.key = [int(c) for c in self.key]
            return self.check_nums()
        elif not key.isdigit():
            return False
        self.key = [int(c) for c in key]
        return self.check_nums()

    def encrypt(self):
        """
        Encrypt the plaintext.
        """
        siz = len(self.key)
        matrix = []
        for _ in range(siz):
            matrix.append("")
        for idx, char in enumerate(self.itxt):
            matrix[idx % siz] += char
        if idx % siz != 0:
            for col in range(idx % siz+1, siz):
                matrix[col] += "X"
        encr_matrix = []
        for row in self.key:
            encr_matrix.append(matrix[row-1])
        self.otxt = "".join(encr_matrix)

    def decrypt(self):
        """
        Decrypt the ciphertext.
        """
        siz = len(self.key)
        txt_siz = len(self.itxt)
        num_rows = txt_siz / siz
        if not num_rows.is_integer():
            """ raise exception """
            pass
        num_rows = int(num_rows)
        matrix = []
        for i in range(siz):
            matrix.append([])
        for i in range(siz):
            matrix[i] = self.itxt[(i*num_rows):((i+1)*num_rows)]
        decr_matrix = []
        for i in range(siz):
            decr_matrix.append([])
        for index, row in enumerate(self.key):
            decr_matrix[row-1] = matrix[index]
        self.otxt = ""
        for elem in zip(*decr_matrix):
            self.otxt += "".join(elem)

    def key_exception(self, key):
        raise CipherException("Invalid key: {}. Row Transposition cipher key must be a string of integers ".format(key)\
            + "such as '145236' or '1 4 5 2 3 6', where each value indicates the row transpositions. Also, the key must"\
            + " contain all integer values from 1-n, where n is the largest integer in the string with no duplicates.")
