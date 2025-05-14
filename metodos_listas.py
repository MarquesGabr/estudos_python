# .append() adiciona um item no final da lista

lista = []
lista.append(23)
lista.append("Gabriel")
lista.append([11,23,69,"rsrs"])

print(lista)

# .clear() é utilizado para limpar os dados da lista

lista.clear()

# .copy() retorna uma lista com os mesmo itens da lista referenciada, 
# porém com outra instância

lista.append([11,23,69,"rsrs"])

lista2 = lista.copy()

print(id(lista2), id(lista))

# .count() conta quantas vezes um determinado objeto apareceu na lista

animal = ["cachorro", "gato", "aranha","gato"]
print(animal.count("gato"))

texto = "Hamlet fala sobre um cara chato. Hamlet não sei o que."
print(texto.count("Hamlet"))

# .extend() passa uma lista como parâmetro, podendo fazer a junção de uma lista de objetos ao invés de usar append para incluir um item por vez
# não elimina valores duplicados 

linguagens_naturais = ["Português", "Inglês", "Espanhol", "Espanhol"]

linguagens_programacao = ["Java", "C", "Python"]

linguagens_naturais.extend(linguagens_programacao)

print(linguagens_naturais)

# .index() retorna o indice da primeira ocorrência de um objeto

print(linguagens_naturais.index("Java"))

# .pop() retira o último item adicionado na lista (conceito de pilha)
# também funciona passar o índice do objeto a ser removido como parâmetro
linguagens_naturais.pop() # retira Python
print(linguagens_naturais)

# .remove() remove da lista a primeira ocorrência do objeto que foi passado como parâmetro
# podemos descobrir quantos objetos existem com count e executar o remove em um loop

# Exemplo de uso único: linguagens_naturais.remove("Espanhol")
# *verificar se também funciona com string

for espanhol in range(linguagens_naturais.count("Espanhol")):
    linguagens_naturais.remove("Espanhol")

print(linguagens_naturais)

# .reverse() faz a transposição da lista (inverte a posição dos objetos)

linguagens_naturais.reverse()

# .sort() ordena a lista (pode ser default[alfabética ou númerica] ou condicionada [usando lambda {função anônima}])

linguagens_naturais.sort() # ordena alfabeticamente

linguagens_naturais.sort(reverse=True) # ordena alfabeticamente de trás para frente

linguagens_naturais.sort(key=lambda x: len(x)) # ordena conforme o tamanho (len) do objeto

linguagens_naturais.sort(key=lambda x: len(x), reverse=True) # ordena conforme o tamanho do objeto (do menor para o maior)

# .len() retorna o tamanho de uma lista ou de um objeto dentro da lista

print(len(linguagens_naturais))

# .sorted() similar ao sort, mas chamado como função e não como método

print(sorted(linguagens_naturais))

print(sorted(linguagens_naturais, key=lambda x: len(x)))

print(sorted(linguagens_naturais, key=lambda x: len(x), reverse=True))