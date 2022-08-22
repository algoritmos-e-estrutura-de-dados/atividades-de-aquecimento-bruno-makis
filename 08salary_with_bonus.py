A=str(input("Digite o nome do vendedor: "))
B=float(input("Digite o salário fixo do mes: "))
C=float(input("Digite o total de vendas efetuadas no mês(em dinheiro): "))
D = C*0.15
E = B + D
print(f"O salário total é: R$ {E:.2F}")