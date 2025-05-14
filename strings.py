# métodos para alterar o case de uma string: .lower .upper e .titleS

# Eliminar espaços em branco: .strip (lstrip - esquerda e rstrip - direita)

curso = "     Python   "

print(curso.strip())
print(curso.lstrip())
print(curso.rstrip())

# Join e center

teste = "Python"

print(teste.center(10,"#")) # centraliza uma string em um número de casas, podendo escolher o caractere das casas em branco

print(".".join(teste)) # insire um determinado caractere entre cada letra da string

