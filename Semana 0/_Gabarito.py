p_1 = input('pessoa 1: ')
p_2 = input('pessoa 2: ')
p_3 = input('pessoa 3: ')

dif = int(input(f'Diferença entre {p_1} e {p_3}: '))
soma = int(input('Somatorio de todas as idades: '))
div = float(input(f'Divisão entre {p_2} por {p_1}: '))

idade_p_3 = (soma - (dif + div*dif))/(2 + div)
idade_p_1 = dif + idade_p_3
idade_p_2 = div*(dif + idade_p_3)

print(f'|{"Nomes":^10} || {"idades":^10}|')
print(f'|{p_1:^10} -> {idade_p_1:^10}|')
print(f'|{p_2:^10} -> {idade_p_2:^10}|')
print(f'|{p_3:^10} -> {idade_p_3:^10}|')
