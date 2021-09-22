import pyAesCrypt

bufferSize = 64 * 1024
password = '12345qwerty'

pyAesCrypt.encryptFile('data', 'data.txt.aes', password, bufferSize)

