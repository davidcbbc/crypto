# Python Module ciphersuite
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import collections
import itertools

# Use crypto random generation to get a key with length n
def gen(): 
	rkey = bytearray(os.urandom(16))
	print(rkey)
	for i in range(16): rkey[i] = rkey[i] & 1
	return bytes(rkey)

# Bitwise XOR operation.
def enc(key, message):
	cipher = Cipher(algorithms.AES(key), modes.ECB())
	encryptor = cipher.encryptor()
	cph = b""
	for character in message:
		print(character*16)
		cph += encryptor.update((character*16).encode())
		print(cph)
	cph += encryptor.finalize()
	return cph


# Reverse operation
def dec(k, c):
	assert len(c) % 16 == 0
	cipher = Cipher(algorithms.AES(k), modes.ECB())
	decryptor = cipher.decryptor()
	blocks = len(c)//16
	msg = b""
	for i in range(0,(blocks)):
		msg+=decryptor.update(c[i*16:(i+1)*16])
		msg=msg[:-15]
	msg += decryptor.finalize()
	return msg


def dec_first_block(key):
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()
    msg = decryptor.update(b'7eefe424722500f4')
    msg=msg[:-15]
    msg += decryptor.finalize()
    return msg
    

def replace_with(array, old, new):
    new_array = []
    for obj in array:
        if obj == old: obj = new
        new_array.append(obj)
    return new_array

### main



#key = gen()
#print(key)
#exit()

cipher_text = open("group_6.txt", "r")
#print(cipher_text.readline())

cipher = cipher_text.readline().encode()


print(cipher[:16])
#exit()
lst = list(itertools.product([0, 1], repeat=16))

print(len(lst))

#print(dec(bytes(lst[2]),cipher).decode("utf-8"))

#exit()
#print(bytes(lst[2]))

for i in range(0 , len(lst)):
	msg = dec(bytes(lst[i]), cipher)
	try:
		new_msg = msg.decode("utf-8")
		print(new_msg)
		break
	except:
		continue
     

exit()

blocks = len(cipher)//16
array_block = []
for i in range(0,(blocks)):
    block = cipher[i*16:(i+1)*16]
    array_block.append(block)

elements_count = collections.Counter(array_block)
for key, value in elements_count.items():
       print(f"{key}: {value}")

new = replace_with(array_block, b'6fe00971a3a03bba', "e")
new = replace_with(new, b'6adaddc981b00242', "e")
new = replace_with(new, b'b84141b129bd1282', "a")
new = replace_with(new, b'07c1f47c65f8029c', "a")
new = replace_with(new, b'39ca6c8d6d2b9db4', "o")
new = replace_with(new, b'81511b387a848fa6', "o")
new = replace_with(new, b'b06e97a635494be2', "s")
new = replace_with(new, b'0074e6eb3a5705dd', "s")
new = replace_with(new, b'54afcfaf3c186af3', "r")
new = replace_with(new, b'bdff870e31d61747', "r")
new = replace_with(new, b'573d6a4c425845ae', "i")
new = replace_with(new, b'82dbacccaf1897e1', "i")

new = replace_with(new, b'19eec2737f1a4e89', "m")
new = replace_with(new, b'53039ace9082a027', "m") #51

#new = replace_with(new, b'81511b387a848fa6', "o")
#new = replace_with(new, b'81511b387a848fa6', "o")
#new = replace_with(new, b'81511b387a848fa6', "o")
#new = replace_with(new, b'81511b387a848fa6', "o")

#new = replace_with(new, b'6adaddc981b00242', "m")
print(new)

#print(len(array_block)/16)
#key = gen()

#cipher = enc(key, "ola")

#print(cipher)