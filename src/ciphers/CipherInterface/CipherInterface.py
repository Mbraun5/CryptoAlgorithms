from abc import ABC, abstractmethod

class CipherException(Exception):
    def __init__(self, message="Base Exception"):
        self.message = message
        super().__init__(message)

class CipherInterface(ABC):
    def __init__(self, key="", ifil="", ofil=""):
        if not self.setKey(key):
            self.key_exception(key)
        self.itxt = self.read_input(ifil)
        self.ofil = ofil
    
    def read_input(self, ifil):
        """
        Reads the input ciphertext or plaintext

        :param str ifil: Name of the input file.
        :return: Entire file text after removing whitespace and newlines.
        """
        try:
            with open(ifil, "r") as fp:
                return fp.read().strip().upper()
        except FileNotFoundError as exc:
            raise CipherException(
                "Input file `{}` deleted prior to file reading. <INPUT FILE> must be a local file path.".format(ifil)
            )

    def write_output(self):
        with open(self.ofil, "w") as fp:
            fp.write(self.otxt)

    @abstractmethod
    def setKey(self, key):
        """
        Sets the key to use for the cipher

        :param str key: The key to use
        :return: True if key is valid, False otherwise
        """
        pass
    
    @abstractmethod
    def encrypt(self, plaintext):
        """
        Encrypt the plaintext.

        :param str plaintext: The plaintext to encrypt
        :return: The ciphertext
        """
        pass

    @abstractmethod
    def decrypt(self, ciphertext):
        """
        Decrypt the ciphertext.

        :param str ciphertext: The ciphertext to decrypt
        :return: The plaintext
        """
        pass

    def key_exception(self):
        raise CipherException("Invalid key: {}".format(self.key))
