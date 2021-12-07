nome = str(input('Informe o seu nome: '))
nasc = int(input('{} informe o seu ano de nascimento: '.format(nome)))

result = (2021-nasc)

if result <= 9:
    print('{} Voce tem {} anos e faz parte da categoria: MIRIM '.format(nome, result))
elif result <= 14:
    print('{} Voce tem {} anos faz parte da categoria: INFANTIL '.format(nome, result))
elif result <= 19:
    print('{} Voce tem {} anos faz parte da categoria: JUNIOR '.format(nome, result))
elif result <= 25:
    print('{} Voce tem {} anos faz parte da categoria: SÊNIOR '.format(nome, result))
elif result >= 26:
    print('{} Voce tem {} anos faz parte da categoria: MASTER '.format(nome, result))

