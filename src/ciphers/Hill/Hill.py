from CipherInterface.CipherInterface import CipherInterface, CipherException
from math import sqrt


class MatrixCalc:
    """ Needs Work
    @staticmethod
    def getTransMatrix(matrix):
        return list(map(list, zip(*matrix)))

    @staticmethod
    def getMatrixMinor(m,i,j):
        return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

    @staticmethod
    def getMatrixDeterminant(matrix):
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        determinant = 0
        for col in range(len(matrix)):
            determinant += ((-1)**col) * matrix[0][col] * MatrixCalc.getMatrixDeterminant(MatrixCalc.getMatrixMinor(matrix,0,col))
        return determinant

    @staticmethod
    def getMatrixInverse(matrix):
        determinant = MatrixCalc.getMatrixDeterminant(matrix)
        if len(matrix) == 2:
            return [[matrix[1][1] / determinant, -1 * matrix[0][1] / determinant],
                    [-1 * matrix[1][0] / determinant, matrix[0][0] / determinant]]

        cofactors = []
        for row in range(len(matrix)):
            cofactorRow = []
            for col in range(len(matrix)):
                minor = MatrixCalc.getMatrixMinor(matrix,row,col)
                cofactorRow.append(((-1)**(row + col)) * MatrixCalc.getMatrixDeterminant(minor))
            cofactors.append(cofactorRow)
        cofactors = MatrixCalc.getTransMatrix(cofactors)
        for row in range(len(cofactors)):
            for col in range(len(cofactors)):
                cofactors[row][col] = (cofactors[row][col] / determinant) % 26
        return cofactors
    """
    
    @staticmethod
    def multiplyMatrixVector(matrix, vector):
        res = []
        for row in matrix:
            val = 0
            for idx, elem in enumerate(vector):
                val += elem * row[idx]
            res.append(val % 26)
        return res


class Hill(CipherInterface):
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
        parsed_key = key.split(" ")
        mat_len = sqrt(len(parsed_key))
        if mat_len - int(mat_len) != 0:
            return False

        self.key = []
        for idx, num in enumerate(parsed_key):
            if not num.isdigit():
                return False
            if idx % mat_len == 0:
                self.key.append([])
            self.key[-1].append(int(num) % 26)
        return True

    def encrypt(self):
        """
        Encrypt the plaintext.
        """
        self.otxt = ""
        nums = len(self.key)
        while len(self.itxt) % nums != 0:
            self.itxt += 'X'
        for i in range(0, len(self.itxt), nums):
            new_mat = [ord(self.itxt[j]) - ord('A') for j in range(i, i + nums)]
            encr_mat = MatrixCalc.multiplyMatrixVector(self.key, new_mat)
            new_mat = [chr(val % 26 + ord('A')) for val in encr_mat]
            self.otxt += "".join(new_mat)

    def decrypt(self):
        """
        Decrypt the ciphertext.
        """
        """ Needs Work
        self.key = MatrixCalc.getMatrixInverse(self.key)
        self.otxt = ""
        nums = len(self.key)
        while len(self.itxt) % nums != 0:
            self.itxt += 'X'
        for i in range(0, len(self.itxt), nums):
            new_mat = [ord(self.itxt[j]) - ord('A') for j in range(i, i + nums)]
            encr_mat = MatrixCalc.multiplyMatrixVector(self.key, new_mat)
            new_mat = [chr(round(val) % 26 + ord('A')) for val in encr_mat]
            self.otxt += "".join(new_mat)
        """

    def key_exception(self, key):
        raise CipherException("Invalid key: {}. Hill cipher key must be a list of single integer values such as `12 34 10 4`".format(key)\
                            + "and the number of integers in the list must be a perfect square. The positions in the matrix are filled"
                            + " from top left to bottom right by filling in numbers along each row in the order they are given.")