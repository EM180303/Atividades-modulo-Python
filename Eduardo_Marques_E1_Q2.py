valor = float(input('Qual o valor? '))
taxa = float(input('Qual a taxa (procrntagem de juros)? '))
tempo = int(input('Qual o tempo, em meses? '))
prestacao = valor + (valor * (taxa / 100) * tempo)
print('A prestação é: ', prestacao)
