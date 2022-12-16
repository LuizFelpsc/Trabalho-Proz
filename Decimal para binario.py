num = int(input('Digite o número que deseja converter para binário: '))
nume = num
binario = ''

while num > 1:
    numero = num % 2
    num = num // 2
    binario += str(numero)
binario += str(num)


print(f'{nume} Convertido para binário é: {binario[::-1]}')