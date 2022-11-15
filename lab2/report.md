## Entropia e Aleatoriedade

1) Considere o conjunto de números entre o intervalo [0..250] e o número primo p=251. Produza um valor b aleatório uniforme (8-bit) e calcule o seu módulo (b (mod(p))). Repita o mesmo para o valor w (64-bit)
Calcule a probabilidade destes valores pertencerem ao intervalo [0..250] e comente se as distribuições são uniformes:Utilizando o Python, definimos a função distribuicao, que permite calcular a probabilidade de cada valor no intervalo [0…250] ocorrer, calculando o valor resto.