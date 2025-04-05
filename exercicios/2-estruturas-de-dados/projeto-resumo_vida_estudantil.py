# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
estudante = {}
estudante['nome'] = input('Olá poderia me dizer seu nome?')
estudante['linkedIn'] = int(input('Em que ano você começou a usar o LinkedIn?'))
estudante['ano_atual'] = int(input('Como estou aprendendo sobre o tempo, em que ano estamos?'))
curs_rel = input('Quantos cursos você ja fez até o momento usando o LinkedIn Learning? Por favor coloque eles em ordem cronologica e separados por virgula.')
estudante['curs_rel'] = curs_rel.split(', ')
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
total_anos = estudante['ano_atual'] - estudante['linkedIn']
total_curs = len(estudante['curs_rel'])

print(f"Olá {estudante['nome']}, desde {estudante['linkedIn']} você tem acesso o LinkedIn. Nesses {total_anos} anos, você realizou {total_curs} cursos na plataforma, sendo o primeiro curso {estudante['curs_rel'][0]} e o ultimo curso {estudante['curs_rel'][-1]}")