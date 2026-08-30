# Faça uma função contadora de vogais
<<<<<<< HEAD
def contar_vogais(texto):
=======
def contar_vogais(texto):
>>>>>>> 772683f869333f54861a0277289f22155d5477ca

    vogais = "aeiouAEIOU"

    conta_vogais = 0
    
    for char in texto:
        if char in vogais:
          conta_vogais += 1
    return conta_vogais

texto = input()

resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")
