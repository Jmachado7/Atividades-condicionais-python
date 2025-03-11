import os

os.system('cls')

print('Calculadora\n')

def multiplicacao():
    numero_1 = int(input('Digite o primeiro número: '))
    numero_2 = int(input('Digite o segundo número: '))
    resultado = numero_1 * numero_2
    os.system('cls')
    print(f'O resultado da multiplicação é: {resultado}')
def divisao():
    numero_1 = int(input('Digite o primeiro número: '))
    numero_2 = int(input('Digite o segundo número: '))
    resultado = numero_1 / numero_2
    os.system('cls')
    print(f'O resultado da divisão é: {resultado}')
def soma():
    numero_1 = int(input('Digite o primeiro número: '))
    numero_2 = int(input('Digite o segundo número: '))
    resultado = numero_1 + numero_2
    os.system('cls')
    print(f'O resultado sa soma é: {resultado}')
def subtracao():
    numero_1 = int(input('Digite o primeiro número: '))
    numero_2 = int(input('Digite o segundo número: '))
    resultado = numero_1 - numero_2
    os.system('cls')
    print(f'O resultado subtração é: {resultado}')

opcao = int(input("""Selecione a operação: 
1. Soma
2. Subtração
3. Multiplicação
4. Divisão
Operação: """))

if opcao == 1:
    soma()
elif opcao == 2:
    subtracao()
elif opcao == 3:
    multiplicacao()
else:
    divisao()
