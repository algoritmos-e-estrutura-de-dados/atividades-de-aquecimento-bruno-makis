A=int(input("Digite o código do produto: "))
B=int(input("Digite a quantidade de produto: "))
C=float(input("Digite o valor do produto: "))

D=int(input("Digite o código para um segundo produto: "))
E=int(input("Digite a quantidade do segundo produto: "))
F=float(input("Digite o valor para o segundo produto: "))

valor = ((B*C) + (E*F))
print(f"Valor a pagar: R$ {valor:.2F}")