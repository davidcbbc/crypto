### 1. In a public-key system using RSA, you intercept the ciphertext C = 20 sent to a user whose public key is e = 13, n = 77. What is the plaintext M?

n = 7 * 11 = 77

Foi inicialmente calculado os fatores de n, p e q chegando a conclusão que estes são 7 e 11.

p = 7 q = 11

Após descobrir o valor de p e q é possível calcular o phi(n) usando a expressão ((p-1) * (q-1))

phi = 7-1 * 11-1  = 60

sabemos também que :

e = 13
d = e^-1 mod phi = 37

C = 20

M = C^d mod n = 48

Calculando outra vez o C para verificar se o M calculado é o correto

C = M^e mod n = 48^13 mod 77 = 20

Chegando assim a conclusão que M = 48

### 2. In a RSA system, the public key of a given user is e = 65, n = 2881. What is the private key of this user?

n = 2881

Como 43 * 67 = 2881 então p = 43 e q = 67

phi = ((p-1) * (q-1)) = (43-1) * (67-1) = 2772
e = 65
d = e^-1 mod phi = 65^-1 mod 2772 = 725

A chave privada é 725.

### 3. In the RSA public-key encryption scheme, each user has a public key e and a private key d. Suppose Bob leaks his private key. Rather than generating a new modus, he decides to generate a new public key e and a new private key d. Is this safe?

se a mesma mensagem for enviada novamente e o GCD do e antigo e o e novo for igual a um e o GCD da segunda mensagem com o modulus for igual a um também então é possível fazer o ataque conhecido como "common modulus attack"

### 4. Suppose Bob uses the RSA cryptosystem with a very large modulus n for which the factorisation cannot be found in a reasonable amount of time. Suppose Alice sends an enciphered message to Bob containing only her phone number: number^e (mod n). Is this safe?

se o atacante souber que a mensagem é um numero de telemovel então o mundo de mensagens possíveis é relativamente pequeno possibilitando que o atacante faça um ataque de força bruta.