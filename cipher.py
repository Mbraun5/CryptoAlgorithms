from ciphers import *
import argparse

def set_arguments():
    pass

class Main():
    def __init__(self):
        self.set_arguments()

    def set_arguments(self):
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encrypt plaintext using various ciphers. Provides functionality\
                                        for Playfair, Row Transposition, Railfence, Vigenre, and Monoalphabetic Cipher.")
    parser.add_argument(
        "<CIPHER NAME>", 
        help="Name of the cipher to use. One of `PLF`, `RTS`, `RFC`, `VIG`, `CES`, `MAC`.",
    )
    parser.add_argument(
        "<KEY>", 
        help="The encryption/decryption key to use.",
    )
    parser.add_argument(
        "<ENC/DEC>", 
        help="One of `ENC` or `DEC`: whether to encrypt or decrypt, respectively.",
    )
    parser.add_argument(
        "<INPUT FILE>", 
        help="The file from which to read the input.",
    )
    parser.add_argument(
        "<OUTPUT FILE>", 
        help="The file to which the output should be written.",
    )
    args = vars(parser.parse_args())
    
    cipher_name = args["<CIPHER NAME>"]
    cipher_arguments = {
        "key": args["<KEY>"],
    }
    ciphers = {
        "PLF": Playfair(**cipher_arguments), 
        "RTS": 1, 
        "RFC": 2, 
        "VIG": 3, 
        "CES": 4, 
        "MAC": 5
    }

    try:
        cipher = ciphers[cipher_name]
    except KeyError:
        parser.error("Invalid cipher name. <CIPHER NAME> must be one of `PLF`, `RTS`, `RFC`, `VIG`, `CES`, `MAC`.")
