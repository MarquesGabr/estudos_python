# Faça uma função contadora de vogais
def contar_vogais(texto):

    vogais = "aeiouAEIOU"

    conta_vogais = 0
    
    for char in texto:
        if char in vogais:
          conta_vogais += 1
    return conta_vogais

texto = input()

resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")