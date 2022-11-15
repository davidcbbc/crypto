from cryptography .hazmat. primitives .ciphers import Cipher , algorithms , modes
import os 
from binascii import hexlify

block_size = 16

def encrypt_aes_ctr(input: bytes, key: bytes, nonce: bytes):
    encryptor = Cipher(algorithms.AES(key), modes.CTR(nonce)).encryptor()
    update = encryptor.update(input)
    finish = encryptor.finalize()
    return update + finish

## Create AES key and Nonce
nonce = os.urandom(block_size)
aes_key = os.urandom(block_size)

message = "this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_"
message_in_bytes = message.encode()
print("Message lenght (byte): " + str(len(message_in_bytes)))

## Create padding
padding = (chr(block_size -len(message_in_bytes) % block_size) * (block_size -len(message_in_bytes) % block_size)).encode()

## Add padding to the message
message_with_padding = message_in_bytes + padding

## Encrypt message
cyphertext = encrypt_aes_ctr(message_in_bytes, aes_key, nonce)

print("AES Key: " + str(hexlify(aes_key)))
print("Nonce: " + str(hexlify(nonce)))

## Writting the ciphertext to file
cphFile = open("ciphertext_ctr.bin", "wb")
cphFile.write(cyphertext)

# openssl aes-128-ctr -d -in ciphertext_ctr.bin -K 047c29a4d10e99d43b427a40a6cf4db0 -iv c92ae8ca37737026cb50877a88d0e0a2