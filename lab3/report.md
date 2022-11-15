

# Tutorial #3

### **1 - Use Python to encrypt a file in CBC mode**

The python code is as follows:

```
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
```
Output:
```
Message lenght (byte): 625
AES Key: b'4f28a5536c4a1aa26c81c9bef4e533e3'
Init Vector: b'bc61168c09870ecbfa0d8a33fad3732f'
```
### **2 - Decrypt the file with OpenSSL and check for success**

```
openssl aes-128-cbc -d -in ciphertext.bin -K 4f28a5536c4a1aa26c81c9bef4e533e3 -iv bc61168c09870ecbfa0d8a33fad3732f
```

Output:

```
this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_
```

### **3 - Edit the file to change the value of (but not delete!) one byte and decrypt again.**

After altering one byte with the tool Hex Fiend , this was the output:

```
this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_messagP
���T۬�q����Ge _message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_
```

**What happened?**

* With CBC cipher , tampering one byte will corrupt not only the current block but also the one after that that needs the first to decrypt. The rest of the blocks didn't depended on the affected block.


**Could you recover a file encrypted with CBC if the IV and the first ciphertext block were corrupted or lost?**
* Not fully, the first two blocks won't be recoverable, altough the remaining blocks can still be decrypted.

**Could you recover it if during a satellite transmission one bit of the ciphertext is not delivered?**
* Maybe not, because it will cause the padding to be inconsistent, therefore CBC won't work.

**Could you modify a byte in the middle of a CBC encrypted file without fully re-encrypting it?**
* That outcome will be the same as the one in the first question, it will change 2 blocks.


### 4 - Repeat the exercise with CTR mode. What are the differences?

The python code is as follows

```
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
```

Output:

```
Message lenght (byte): 625
AES Key: b'047c29a4d10e99d43b427a40a6cf4db0'
Nonce: b'c92ae8ca37737026cb50877a88d0e0a2'
```

Now, altering one byte will result on the following:

```
this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_messJge_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_this_is_a_secret_message_
```
(Notice the "J" on the middle) .

The difference between CTR and CBC is that CTR XORs the encrypted value of (NONCE + COUNTER) with the plaintext which means that , modyfing a byte will only modify that byte encryption and not the entire block as CBC.

### 5 - Download the ciphertext corresponding to your group number and find the plaintext.

Given the hint I assume it's ECB cipher.