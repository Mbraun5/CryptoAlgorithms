import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from src.main.cipher import Main
import filecmp  


class TestAlgorithms(unittest.TestCase):
    def test_playfair(self):
        testdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Playfair")
        for file in os.listdir(testdir):
            with self.subTest(file=file):
                if file.startswith("dec_"):
                    continue
                elif file.startswith("enc_"):
                    continue
                else:
                    Main.test_integration("PLF", file[:len(file)-4], "{}/{}".format(testdir, file), "test_enc.txt", "ENC")
                    Main.test_integration("PLF", file[:len(file)-4], "{}/{}".format(testdir, file), "test_dec.txt", "DEC")
                self.assertTrue(filecmp.cmp("{}/enc_{}".format(testdir, file), "test_enc.txt", shallow=False))
                self.assertTrue(filecmp.cmp("{}/dec_{}".format(testdir, file), "test_dec.txt", shallow=False))
                os.remove("test_enc.txt")
                os.remove("test_dec.txt")
    
    def test_row_transposition(self):
        testdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "RowTransposition")
        for file in os.listdir(testdir):
            with self.subTest(file=file):
                if file.startswith("dec_"):
                    continue
                elif file.startswith("enc_"):
                    continue
                else:
                    Main.test_integration("RTS", file[:len(file)-4], "{}/{}".format(testdir, file), "test_enc.txt", "ENC")
                    Main.test_integration("RTS", file[:len(file)-4], "test_enc.txt", "test_dec.txt", "DEC")
                    self.assertTrue(filecmp.cmp("{}/enc_{}".format(testdir, file), "test_enc.txt", shallow=False))
                    self.assertTrue(filecmp.cmp("{}/dec_{}".format(testdir, file), "test_dec.txt", shallow=False))
                    os.remove("test_enc.txt")
                    os.remove("test_dec.txt")

    def test_railfence(self):
        testdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Railfence")
        for file in os.listdir(testdir):
            with self.subTest(file=file):
                if file.startswith("dec_"):
                    continue
                elif file.startswith("enc_"):
                    continue
                else:
                    Main.test_integration("RFC", file[:len(file)-4], "{}/{}".format(testdir, file), "test_enc.txt", "ENC")
                    Main.test_integration("RFC", file[:len(file)-4], "test_enc.txt", "test_dec.txt", "DEC")
                    self.assertTrue(filecmp.cmp("{}/enc_{}".format(testdir, file), "test_enc.txt", shallow=False))
                    self.assertTrue(filecmp.cmp("{}/dec_{}".format(testdir, file), "test_dec.txt", shallow=False))
                    os.remove("test_enc.txt")
                    os.remove("test_dec.txt")

    def test_vigenere(self):
        testdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Vigenere")
        for file in os.listdir(testdir):
            with self.subTest(file=file):
                if file.startswith("dec_"):
                    continue
                elif file.startswith("enc_"):
                    continue
                else:
                    Main.test_integration("VIG", file[:len(file)-4], "{}/{}".format(testdir, file), "test_enc.txt", "ENC")
                    Main.test_integration("VIG", file[:len(file)-4], "test_enc.txt", "test_dec.txt", "DEC")
                    self.assertTrue(filecmp.cmp("{}/enc_{}".format(testdir, file), "test_enc.txt", shallow=False))
                    self.assertTrue(filecmp.cmp("{}/dec_{}".format(testdir, file), "test_dec.txt", shallow=False))
                    os.remove("test_enc.txt")
                    os.remove("test_dec.txt")

    def test_caesar(self):
        testdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Caesar")
        for file in os.listdir(testdir):
            with self.subTest(file=file):
                if file.startswith("dec_"):
                    continue
                elif file.startswith("enc_"):
                    continue
                else:
                    Main.test_integration("CES", file[:len(file)-4], "{}/{}".format(testdir, file), "test_enc.txt", "ENC")
                    Main.test_integration("CES", file[:len(file)-4], "test_enc.txt", "test_dec.txt", "DEC")
                    self.assertTrue(filecmp.cmp("{}/enc_{}".format(testdir, file), "test_enc.txt", shallow=False))
                    self.assertTrue(filecmp.cmp("{}/dec_{}".format(testdir, file), "test_dec.txt", shallow=False))
                    os.remove("test_enc.txt")
                    os.remove("test_dec.txt")


if __name__ == "__main__":
    unittest.main()