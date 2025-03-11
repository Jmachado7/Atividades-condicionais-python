import os

os.system("cls")

print("Mercado\n")
produto = input("Escreva o produto: \n")
valor = float(input("Escreva o valor unitário do produto: \n"))
quant = int(input("digite a quantidade que deseja: \n"))

preco = valor * quant

if quant <= 5:
    desconto = preco * 0.02
    preco2 = preco - (preco * desconto)
elif quant <= 10 :
    desconto = preco * 0.03
    preco2 = preco - (preco * desconto)
else: 
    desconto = preco * 0.05
    preco2 = preco -(preco * desconto)

os.system("cls")

print("---Mercado---\n")
print(f"Produto : {produto}\n")
print(f"Total a pagar (sem desconto): {preco}")
print(f"Total a pagar (com desconto): {preco2})")
print(f"Desconto: {desconto}")