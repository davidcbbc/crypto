from cryptography .hazmat. primitives .ciphers import Cipher , algorithms , modes
import os 
from binascii import hexlify
block_size= 16

def encrypt_aes_cbc(input: bytes, key: bytes, iv: bytes):
    encryptor = Cipher(algorithms.AES(key), modes.CBC(iv)).encryptor()
    update = encryptor.update(input)
    finish = encryptor.finalize()
    return update + finish

## Create key and Initialization Vector
iv = os.urandom(block_size)
aes_key = os.urandom(block_size)

message = "this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_"
message_in_bytes = message.encode()
print("Message lenght (byte): " + str(len(message_in_bytes)))

## Create padding
padding = (chr(block_size -len(message_in_bytes) % block_size) * (block_size -len(message_in_bytes) % block_size)).encode()

## Add padding to the message
message_with_padding = message_in_bytes + padding

## Encrypt message
cyphertext = encrypt_aes_cbc(message_with_padding,aes_key,iv)

print("AES Key: " + str(hexlify(aes_key)))
print("Init Vector: " + str(hexlify(iv)))

## Writting the ciphertext to file
cphFile = open("ciphertext.bin", "wb")
cphFile.write(cyphertext)

#openssl aes-128-cbc -d -in ciphertext.bin -K e50a62b9cc458afd76eb017645bc95bb -iv b8cbfe1376c064b99a45cb585940bf3b