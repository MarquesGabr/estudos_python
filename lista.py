# Entender o funcionamento de lists

# Criação e acesso: 
# Listas podem armazenar de maneira sequencial qualquer tipo de objeto. Podemos criar listas com o constructor list, a função range ou colocando os valores separados por vírgula
# dentro de colchetes. Listas de objetos são mutáveis.

frutas = ["laranja", "maça", "uva"]

frutas = []

letras = list("python")

numeros = list(range(10))

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

# print(carro[0][3:6])

# print(letras[-1])

# print(letras[:6:2])

# Iterar em uma lista:

carros = ["uno", "golf", "impala"]

for carro in carros:
    print(carro)

# Espelhar e inverter
for carro in carros:
    print(carro[::-1])

# For com enumerate:

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# List comprehension:

# Versão 1:
nums = [1, 30, 21, 2, 9, 65, 34]
pares = []
quadrados = []

for num in nums:
    if num % 2 == 0:
        pares.append(num)

for num in nums:
    quadrados.append(num ** 2)

# Versão 2
# lista_a_ser_gerada = [retorno (como eu quero que os itens sejam adicionados na lista) iteração (for) condição > opcional (if)] 
pares = [nums for num in nums if num % 2 == 0]

quadrados = [num ** 2 for num in nums]