# Fatiamento de strings é uma técnica utilizada para retornar substrings (partes da string original), 
# informando inicio (start), fim (stop) e passo (step): [start: stop[, step]]. 


nome = "Gabriel Fabiano Marques"

print(nome[0]) # >>> "G" 

print(nome[:8]) # >>> "Gabriel" 

print(nome[8:]) # >>> "Fabiano Marques" 

print(nome[8:15]) # >>> "Fabiano" 

print(nome[9:15:2]) # >>> "ain" 

print(nome[:]) # >>> "Gabriel Fabiano Marques" 

print(nome[::-1]) # >>> "seuqraM onaibaF leirbaG" 