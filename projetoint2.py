#PROJETO INTERDISCIPLINAR - GIOVANNA DE ANDRADE GONÇALVES (33394075) E NICOLE FELIX RODRIGUES(33711208)#

input("Bem vindo! Pressione 'enter' para ver as opções disponiveis!")
print('1(decimal/binário)')
print('2(decimal/hexadecimal)')
print('3(decimal/octadecimal)')
option = int(input("Digite a opção de conversão desejada: "))
#resto da divisão até o quociente dar zero# #dig = '0123456789ABCDEF'#
#BASE 16: A = 10 B = 11 C = 12 D = 13 E = 14 F = 15# #BASE 8: 01234567#
if option == 1:
    valor1 = int(input('Digite o valor decimal: '))
    binario = ""
    while valor1!=0:
        r = valor1%2
        binario = str(r) + binario
        valor1 = valor1//2
        print(binario)

elif option == 2:
    valor2 = int(input('Digite o valor decimal: '))
    hexadecimal = ""
    dig = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    while valor2!=0:
        r = valor2%16
        hexadecimal = dig[r] + hexadecimal
        valor2 = valor2//16
        print(hexadecimal)

elif option == 3:
    valor3 = int(input('Digite o valor decimal: '))
    octadecimal = ""
    while valor3!=0:
        r = valor3%8
        octadecimal = str(r) + octadecimal
        valor3 = valor3//8
        print(octadecimal)

else:
    print("Opção invalida!")
