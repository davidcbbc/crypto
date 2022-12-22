### 1 - Use openSSL to generate Diffie-Hellman parameters at 128-bit security (4096-bit modulus) using option dhparam. Do not activate option -dsaparam.

Para gerar parametros Diffie-Hellman com 128-bit de segurança o comando que deve ser utilizado é :

openssl dhparam "<BIT_SIZE>" -out <OUTPUT_FILE> 

onde <BIT_SIZE> corresponde ao tamanho dos val e <OUTPUT_FILE> é o ficheiro onde são guardados os valores produzidos. O comando executado foi :

time openssl dhparam 4096 -out dh_4096_without_dsaparam

esta operação demorou 167 segundos

### 2 - Repeat the exercise activating option -dsaparam.

Neste exercicio foi então repetido o comando anterior mas desta vez usando -dsaparam sendo este o seguinte : 

time openssl dhparam 4096 -out dh_4096_with_dsaparam -dsaparam

esta operação demorou 20 segundos.

### 3 - Why does the first approach take so much longer? Use Sage to check that the produced primes have the structure you describe in your answer.

Durante a geração de números primos para o algoritmo Diffie-Hellman "obriga" a que os primos sejam primos seguros (safe prime) para um primo p ser considerado seguro (p-1 / 2) tem que ser primo de igual forma, isto é feito para evitar que existam grupos com subgrupos pequenos para que seja difícil quebrar este algoritmo. O segundo modo não se preocupa en gerar estes primos seguros sendo mais rápido o calculo.

Podemos verificar estes primos com o comando :

openssl dhparam -in <OUTPUT_FILE> -check -text

quando executamos este comando com o ficheiro "dh_4096_without_dsaparam" obtemos a informação "DH parameters appear to be ok." enquato que para o ficheiro "dh_4096_with_dsaparam" obtemos a informação "p value is not a safe prime".

### 5  - Alice and Bob agree to use the prime p = 1373 and the base g = 2 for a Diffie–Hellman key exchange. Alice sends Bob the value X = 974. Bob asks your assistance, so you tell him to use the secret exponent y = 871. What value Y should Bob send to Alice, and what is their secret shared value? Can you figure out Alice’s secret exponent?

p = 1373
g = 2
x = ? 
y = 871
X = g^x mod p = 2^x mod 1373 = 974
Y = g^y mod p = 2^871 mod 1373 = 805

secret = X^y mod p = Y^x mod p = (X^y mod p = 974^871 mod 1373) = 397

fazendo um sistemas de equações

( 2^x mod 1373 = 974, 805^x mod 1373 = 397 ) = 1372n + 587 ( calculado em https://www.wolframalpha.com/ ) escolhendo n = 1 , x = 1372 + 587 = 1959

usando este valor para calcular o secret obtemos
secret = Y^x mod p = 805^1959 mod 1373 = 397


### 6 - Prove that an algorithm that solves the Computational Diffie–Hellman problem can be used to solve the Decisional Diffie–Hellman problem.

O problema Computacional Diffie-Hellman diz que se um atacante adquirindo g^a e g^b sem acesso aos valos a e b é impossível conseguir computar g^ab ou seja não consegue computar a chave secreta. Por outro lado o problema de Decisão do Diffie-Hellman diz que tendo o atacante acesso a g^a e g^b se este adquirir g^ab e g^c onde g^ab é a chave secreta e g^c é o valor g elevado a um valor random o atacante não é capaz de decidir qual é a chave secreta entre estes dois ultimos valores. Agora se pensarmos que é descoberto um algoritmo que é capaz de resolver o problema computacional, ou seja, se existir um algoritmo que adquirindo g^a e g^b consegue computar g^ab então este também resolve o problema de decisão pois se este é capaz de calcular g^ab consegue perceber qual dos dois valores adquiridos após obter g^a e g^b é a chave secreta e qual é o valor g^c resolvendo assim o problema de decisão.