import argparse
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from ciphers import *

class Main():
    @classmethod
    def get_args(cls):
        cls.parser = argparse.ArgumentParser(
            description="Encrypt plaintext using various ciphers. Provides functionality for Playfair, \
                Row Transposition, Railfence, Vigenere, and Monoalphabetic Cipher."
        )
        cls.parser.add_argument("<CIPHER NAME>", help="Name of cipher to use. One of `PLF`, `RTS`, `RFC`, `VIG`, `CES`, `MAC`, `HIL`.", type=str)
        cls.parser.add_argument("<KEY>", help="The encryption/decryption key to use.", type=str)
        cls.parser.add_argument("<ENC/DEC>", help="One of `ENC` or `DEC`: whether to encrypt or decrypt, respectively.", type=str)
        cls.parser.add_argument("<INPUT FILE>", help="The file from which to read the input.", type=str)
        cls.parser.add_argument("<OUTPUT FILE>", help="The file to which the output should be written.", type=str)
        return vars(cls.parser.parse_args())
        
    @classmethod
    def process_args(cls):
        args = cls.get_args()
        cipher_name = args["<CIPHER NAME>"]
        if not os.path.isfile(args["<INPUT FILE>"]):
            cls.parser.error("Invalid input file. <INPUT FILE> must be a local file path.")
        if args["<ENC/DEC>"] != "ENC" and args["<ENC/DEC>"] != "DEC":
            cls.parser.error("Invalid process command. <ENC/DEC> must be one of `ENC` or `DEC`, \
                whether to encrypt or decrypt, respectively")
        cipher_arguments = {
            "key": args["<KEY>"],
            "ifil": args["<INPUT FILE>"],
            "ofil": args["<OUTPUT FILE>"],
            "mode": args["<ENC/DEC>"],
        }
        ciphers = {
            "PLF": Playfair, 
            "RTS": RowTransposition, 
            "RFC": Railfence, 
            "VIG": Vigenere, 
            "CES": Caesar, 
            "MAC": Monoalphabetic,
            "HIL": Hill,
        }
        try:
            return ciphers[cipher_name](**cipher_arguments)
        except KeyError:
            cls.parser.error("Invalid cipher name. <CIPHER NAME> must be one of `PLF`, `RTS`, `RFC`, `VIG`, `CES`, `MAC`, `HIL`.")

    @classmethod
    def test_integration(cls, cipher_name, key, ifil, ofil, mode):
        ciphers = {
            "PLF": Playfair, 
            "RTS": RowTransposition, 
            "RFC": Railfence, 
            "VIG": Vigenere, 
            "CES": Caesar, 
            "MAC": Monoalphabetic,
            "HIL": Hill,
        }
        return ciphers[cipher_name](key=key, ifil=ifil, ofil=ofil, mode=mode)

    @classmethod
    def main(cls):
        cipher = cls.process_args()


if __name__ == "__main__":
    Main.main()
