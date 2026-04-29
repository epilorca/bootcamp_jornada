CONSTANTE_BONUS = 1000
# 1 - Solicita ao usuário que digite seu nome
nome = input("Digite o seu nome: ")

# 2 - Solicita ao usuário que digite o valor do salário 
# Converta o valor de entrada em ponto flutuante
salario = float(input("Digite o valor bruto do seu salário: "))

# 3 - Solicita ao usuário que digite o valor do bônus recebido 
# Converta o valor de entrada em ponto flutuante
bonus = float(input("Digite o valor do bônus recebido: "))

# 4 - Calcule o valor do bonus final
calc = CONSTANTE_BONUS + (salario * bonus)

# 5 - Imprima o cálculo do KPI para o usuário
print("Olá, ", nome,"O seu bônus foi de R$ ", calc)


