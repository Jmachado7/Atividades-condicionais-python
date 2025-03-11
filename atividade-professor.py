import os

os.system("cls")

print("Escola aprender\n")
nome = input("Escreva o nome do professor: ")
aulas = float(input("Digite a quantidade de hora/aulas: "))
nivel = int(input("Digite seu nível (1, 2 ou 3): "))

if nivel == 1: 
    salario = aulas * 12
elif nivel == 2:
    salario = aulas * 17
elif nivel == 3:
    salario = aulas * 25
else:
    print("Digite um nível válido.")

os.system("cls")

print("---Escola Aprender---\n")
print(f"Nome do professor: {nome}")
print(f"Nível do professor: {nivel}")
print(f"Salário final : R${salario}")
