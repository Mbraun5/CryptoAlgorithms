import unittest
import os
from cipher import Main
import filecmp


class TestAlgorithms(unittest.TestCase):
    def test_playfair(self):
        for file in os.listdir("./Playfair"):
            with self.subtest(file=file):
                if file.startswith("dec_"):
                    pass
                elif file.startswith("enc_"):
                    pass
                else:
                    Main.test_integration("PLF", file[:3], "./Playfair/{}".format(file), "test_enc.txt", "ENC")
                    Main.test_integration("PLF", file[:3], "./Playfair/{}".format(file), "test_dec.txt", "DEC")
                self.assertTrue(filecmp.cmp("./Playfair/enc_{}".format(file), "test_enc.txt", shallow=False))
                self.assertTrue(filecmp.cmp("./Playfair/dec_{}".format(file), "test_dec.txt", shallow=False))
                os.remove("test_enc.txt")
                os.remove("test_dec.txt")


if __name__ == "__main__":
    unittest.main()