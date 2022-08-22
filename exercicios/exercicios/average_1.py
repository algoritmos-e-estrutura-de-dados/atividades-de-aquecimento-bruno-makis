A=float(input("Digite a nota do primeiro aluno:"))
B=float(input("Digite a nota do segundo aluno:"))
MEDIA=((A*3.5)+(B*7.5))/(3.5+7.5)
if(A>10 and B>10):
    print("Notas invalidas")
else:
    print(f"A média é {MEDIA:.5f}")