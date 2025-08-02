linha = ('-=' * 30)
while True:
    pergunta = input('Sou sua calculadora simples, vamos começar? [S/N] ').strip().upper()
    while pergunta.upper() not in ['S','N']:
        pergunta = input('Não consegui entender sua resposta. Você deseja calcular? [S/N] >>> ').strip().upper()
    if pergunta.upper() in ['S', 's']:
        print('Ok, vamos nessa...')
        operador = str(input('Qual o operação você deseja fazer >>>> ADÇÃO [+], SUBTRAÇÃO [-], MULT.[*] OU DIV[/]? >>> '.strip().upper()))
    elif pergunta.upper() in ['N', 'n']:
        break
    while operador.upper() not in['+','-','*','/']: #verifica se os operadores são validos retornando uma mensagem de erro se invalidos
        print('Erro! Responda ADÇÃO [+], SUBTRAÇÃO [-], MULT.[*] OU DIV[/] >>> ')
        operador = input('Quer continuar? [S/N] >>> '.strip().upper())
    if operador == '+':
        print(f'Ok!!! Então vamos somar [{operador}]...')
        n1 = float(input('Digite o primeiro valor >>> ').replace(',','.'))
        n2 = float(input('Digite o segundo valor soma >>> ').replace(',','.'))
        soma = n1+n2
        print(f'A soma entre {n1} e {n2} é igual a {soma:.2f}')
        print(linha)
    elif operador == '-':
        print(f'Ok!!! Vamos subtrair [{operador}]')
        n1 = float(input('Qual o primeiro valor da subtração >>> ').replace(',','.'))
        n2 = float(input('Qual o segundo valor da subtração >>> ').replace(',','.'))
        sub = n1 - n2
        print(f'A subtração de {n1} e {n2} é igual a {sub:.2f}')
        print(linha)
    elif operador == '*':
        print(f'Ok!!! Vamos multiplicar [{operador}]')
        n1 = float(input('Qual o primeiro valor da multiplicação >>> ').replace(',','.'))
        n2 = float(input('Qual o segundo valor da multiplicação >>> ').replace(',','.'))
        mult = n1 * n2
        print(f'A multiplicação de {n1} e {n2} é igual a {mult:.2f}')
        print(linha)
    elif operador == '/':
        print(f'Ok!!! Vamos divisão [{operador}]')
        n1 = float(input('Qual o primeiro valor da divisão >>> ').replace(',','.'))
        n2 = float(input('Qual o segundo valor da divisão >>> ').replace(',','.'))
        divis = n1 / n2
        print(f'A divisão de {n1} e {n2} é igual a {divis:.2f}')
        print(linha)

print(linha)


print('Tudo bem até a proxima')




