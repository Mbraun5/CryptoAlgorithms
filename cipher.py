from ciphers import *
import argparse
import os


class Main():
    @classmethod
    def get_args(cls):
        cls.parser = argparse.ArgumentParser(
            description="Encrypt plaintext using various ciphers. Provides functionality for Playfair, \
                Row Transposition, Railfence, Vigenre, and Monoalphabetic Cipher."
        )
        cls.parser.add_argument("<CIPHER NAME>", help="Name of cipher to use. One of `PLF`, `RTS`, `RFC`, `VIG`, `CES`, `MAC`.")
        cls.parser.add_argument("<KEY>", help="The encryption/decryption key to use.")
        cls.parser.add_argument("<ENC/DEC>", help="One of `ENC` or `DEC`: whether to encrypt or decrypt, respectively.")
        cls.parser.add_argument("<INPUT FILE>", help="The file from which to read the input.")
        cls.parser.add_argument("<OUTPUT FILE>", help="The file to which the output should be written.")
        return vars(cls.parser.parse_args())
    
    @classmethod
    def process_args(cls):
        args = cls.get_args()
        cipher_name = args["<CIPHER NAME>"]
        if not os.path.isfile(args["<INPUT FILE>"]):
            cls.parser.error("Invalid input file. <INPUT FILE> must be a local file path.")
        cipher_arguments = {
            "key": args["<KEY>"],
            "ifil": args["<INPUT FILE>"],
            "ofil": args["<OUTPUT FILE>"],
        }
        ciphers = {
            "PLF": Playfair, 
            "RTS": 1, 
            "RFC": 2, 
            "VIG": 3, 
            "CES": 4, 
            "MAC": 5
        }
        try:
            return ciphers[cipher_name](**cipher_arguments)
        except KeyError:
            cls.parser.error("Invalid cipher name. <CIPHER NAME> must be one of `PLF`, `RTS`, `RFC`, `VIG`, `CES`, `MAC`.")

    @classmethod
    def main(cls):
        cipher = cls.process_args()
        # cipher.encrypt()
        # cipher.decrypt()



if __name__ == "__main__":
    Main.main()
