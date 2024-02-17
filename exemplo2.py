nome = str(input("Digite o nome do aluno: "))
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
 
media = (nota1 + nota2) / 2

if media >=6:
    print("O aluno(a)" , nome , "foi aprovado com media:" , media)
else:
    print("O aluno(a)" , nome , "foi reprovado com media:" , media)
