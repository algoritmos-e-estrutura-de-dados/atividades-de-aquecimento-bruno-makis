A=float(input("Digite a nota do primeiro aluno:"))
B=float(input("Digite a nota do segundo aluno:"))
C=float(input("Digite a nota do terceiro aluno:"))


MEDIA=((A*2)+(B*3)+(C*5))/(10)
if(A>10 and B>10):
    print("Notas invalidas")
else:
    print(f"A média é {MEDIA:.1f}")