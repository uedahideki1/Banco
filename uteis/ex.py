from uteis import numeros

num = int(input('Digite o preço: '))
print(f'A metade de {num} é {numeros.metade(num)}R$')
print(f'o dobro de {num} é {numeros.dobro(num)}R$')
print(f'aumentando 10%, temos {numeros.aumento(num)}R$')