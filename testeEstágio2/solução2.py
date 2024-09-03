num1 = 0
num2 = 1
numAlvo = int(input('Qual número deseja verificar? '))
num3 = num1 + num2
lista = [num1, num2, num3]
while numAlvo > num3:
    num1 = num2
    num2 = num3
    num3 = num1 + num2
    lista.append(num3)

if not numAlvo in lista:
    print(f'Número {numAlvo} não incluso na sequência')
    exit()

print(f'Número {numAlvo} incluso na sequência')