frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1,2,3,4])

pais = ("Brasil",)

# acessar itens em uma tuplas
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

matriz[0] # (1, "a", 2)
matriz[0][0] # 1
matriz [0][-1] # 2
matriz [-1][-1] # c

# métodos da tupla:
# .count() conta quantos elementos tem na tupla
# .idex() verifica a posição de um item na tupla e retorna o índice
# .len() retorna a quantidade de itens na tupla
# .sum() soma os elementos da tupla