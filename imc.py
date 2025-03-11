import os

os.system("cls")

 
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = (peso / (altura * altura)) * 10000
    
if imc < 16:
    classificacao = ('Magreza grave.') 

elif imc < 17:
    classificacao = ('Magreza moderada.')

elif imc < 18.5:
    classificacao = ('Magreza leve.')

elif imc < 25:
    classificacao = ('Peso ideal.')

elif imc < 30:
    classificacao = ('Sobrepeso.')

elif imc < 35:
    classificacao = ('Obesidade Grau .')

elif imc < 41:
    classificacao = ('Obesidade Grau II.')

else :
    classificacao = ('Obesidade Grau III ou mórbida.')

os.system('cls')

print(f'Seu IMC é {imc} - {classificacao}')