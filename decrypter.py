import os
import pyaes
import sys


## open encrypted file

file_name = 'test.txt.ransomware'
file = open(file_name,'rb')
file_data = file.read()
file.close()

## decrypted key

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remove the encrypted file\
os.remove(file_name)

## create new decrypted file

new_file = 'test.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close()
