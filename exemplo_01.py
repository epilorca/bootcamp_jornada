# Crie um programa que o usuário digita o nome e retorna o número de caracteres digitados

print(len(input("Digite seu nome: ")))

# Crie um programa onde o usuário digita 2 valores e apareça o resultado da soma
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
result = valor1 + valor2
print(result)

# Refatore o exercício 1 atribuindo variáveis

nome = input("Digite seu nome: ")
quant_caracter = len(nome)
print("A quantidade de caracteres do seu nome é: ", quant_caracter) 