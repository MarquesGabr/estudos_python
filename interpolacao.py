nome = "Gabriel"
idade = 21
profissao = "Auxiliar de Planejamento"
linguagem = "Python"
PI = 3.1416

print("Olá, me chamo %s. Eu tenho %d anos, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

print("Olá, me chamo {}. Eu tenho {} anos, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {0}. Eu tenho {1} anos, trabalho como {2} e estou matriculado no curso de {3}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {nome}. Eu tenho {idade} anos, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome = nome, idade = idade, profissao = profissao, linguagem = linguagem))

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

print(f"Valor de PI: {PI:.2f}")