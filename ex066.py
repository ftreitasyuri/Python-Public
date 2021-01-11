cont = soma = 0

while True:
    num = int(input('Digite um número ou [999 para parar]: ').strip())
    if num == 999:
        break # daqui para baixo não conta o flag
    cont += 1
    soma += num
print(f'Fora digitados {cont} e soma dos valores digitador é de {soma}')
