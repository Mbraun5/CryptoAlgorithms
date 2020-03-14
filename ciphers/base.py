from abc import ABC, abstractmethod

class CipherException(Exception):
    def __init__(self, message="Base Exception"):
        self.message = message
        super().__init__(message)

class CipherInterface(ABC):
    def __init__(self, key=""):
        if not self.setKey(key):
            self.key_exception(key)

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
