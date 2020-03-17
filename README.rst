==============================================
CryptoAlgorithms
==============================================

CryptoAlgorithms is a python package that incorporates some of the most common entry-level ciphers. This package
only works using any version of **Python 3**

* `Github Repo <https://github.com/Mbraun5/CryptoAlgorithms>`_: The repository where the most up to date version
  of this code lives.

|docs| |travis| |license|

.. |docs| image:: https://img.shields.io/badge/docs-latest-success.svg
    :target: https://github.com/Mbraun5/CryptoAlgorithms/blob/master/README.rst
    :alt: Latest Docs
.. |travis| image:: https://travis-ci.com/Mbraun5/CryptoAlgorithms.svg?token=RMkgUwFNoBVqHzT8NcEc&branch=master
    :target: https://travis-ci.com/Mbraun5/CryptoAlgorithms
    :alt: Build Status
.. |license| image:: https://img.shields.io/badge/license-GPL3-blue.svg
    :target: https://github.com/Mbraun5/CryptoAlgorithms/blob/master/LICENSE
    :alt: GPL V3 License

Executing Main Program
======================
Using Makefile/Bash Script
--------------------------
Prerequisite: The desired input file must be in the **root** directory. ``Default: CryptoAlgorithms/``

Execute::

$ make bin
$ ./cipher.sh *<CIPHER TAG> <KEY> <ENC/DEC> <INPUT FILE> <OUTPUT FILE>*

Further instructions for the Cipher tags and corresponding keys is included below. `ENC` if you would like to encrypt
the input file. `DEC` if you would like to decrypt the input file.

Executing Directly Using Python3
--------------------------------
Prerequisite: The desired input file must be in the **src/main** directory.

First, navigate to the ``src/main`` directory.

Execute:
    python cipher.py *<CIPHER TAG> <KEY> <ENC/DEC> <INPUT FILE> <OUTPUT FILE>*

Further instructions for the Cipher tags and corresponding keys is included below. `ENC` if you would like to encrypt
the input file. `DEC` if you would like to decrypt the input file.

Caesar
------
*<CIPHER TAG>* - **CES**

*<KEY>* - A single integer value indicating the desired alphabetic offset for encryption.
For convenience, any nonnegative integer key is allowed, but there are only 25 unique encryption
keys modulo 26.

Sample command: 
    python cipher.py *CIG 17 ENC ./input.txt ./output.txt*

This command maps:

::

    PT      CT
    A  <->  R
    B  <->  S
    C  <->  T
    . . . . .
    I  <->  Z
    J  <->  A
    K  <->  B
    L  <->  C
    . . . . .
    Y  <->  P
    Z  <->  Q


Monoalphabetic
--------------
*<CIPHER TAG>* - **MAC**

*<KEY>* - A string that contains every character of the English alphabet exactly once. That is, no non-alphabetic character
is permitted, and no duplicate characters are permitted.

Sample command: 
    python cipher.py *MAC RMUTOECGVXZKJFWLPDHYIANQBS ENC ./input.txt ./output.txt*

This command maps:

::

    PT      CT
    A  <->  R
    B  <->  M
    C  <->  U
    . . . . . 
    X  <->  Q
    Y  <->  B
    Z  <->  S

Playfair
--------
*<CIPHER TAG>* - **PLF**

*<KEY>* - A string that only contains alphabetic characters. Duplicate characters are permitted, but will be ignored when setting
the key matrix.

Sample command:
    python cipher.py *PLF occurrence ENC ./input.txt ./output.txt*

This results in the Playfair Matrix:

=====  =====  ======  =====  ======
  O      C      U       R       E
  N      A      B       D       F
  G      H     I/J      K       L
  M      P      Q       S       T
  V      W      X       Y       Z
=====  =====  ======  =====  ======

Railfence
---------
*<CIPHER TAG>* - **RFC**

*<KEY>* - A single integer value (or string containing one integer) denoting the number of rows desired for the railfence cipher.

Sample command:
    python cipher.py *RFC 3 ENC ./input.txt ./output.txt*

With three rows, this text becomes:

::

    W  H  R  R  S  I  E  B  O  S
     I  T  E  O  T  S  X  E  M
      T  H  E  W  H  T  T  C  E

RowTransposition
----------------
*<CIPHER TAG>* - **RTS**

*<KEY>* - A string of integer values, either separated by spaces or in a continuous block (only if largest value is less than 10).
The key denotes the row transpositions desired, and as such must contain every single integer from 1 - N, where N is the largest
integer value in the string.

Sample command:
    python cipher.py *RTS 153264 ENC ./input.txt ./output.txt*

Alternate command:
    python cipher.py *RTS "1 5 3 2 6 4" ENC ./input.txt ./output.txt*

=====  =====  ======  =====  ======  ======
ROWS
-------------------------------------------
  1      2      3       4       5       6
=====  =====  ======  =====  ======  ======
  S      A      M       P       L       E
  P      L      A       I       N       T
  E      X      T       I       N       S
  I      D      E       F       I       L
  E      X      X       X       X       X
=====  =====  ======  =====  ======  ======

|

=====  =====  ======  =====  ======  ======
TRANSPOSED ROWS
-------------------------------------------
  1      5      3       2       6       4
=====  =====  ======  =====  ======  ======
  S      L      M       A      E       P
  P      N      A       L      T       I
  E      N      T       X      S       I
  I      I      E       D      L       F
  E      X      X       X      X       X
=====  =====  ======  =====  ======  ======

Vigenere
--------
*<CIPHER TAG>* - **VIG**

*<KEY>* - A string containing only alphabetic characters. The string will be duplicated until it "covers" the entire plaintext.

Sample command:
    python cipher.py *VIG AEIQZADXCJABC ENC ./input.txt ./output.txt*

| 

Plaintext:
    Heythereletsgooutside

Key:
    AEIQZADXCJABC

Key Becomes:
    AEIQZADXCJABCAEIQZADX