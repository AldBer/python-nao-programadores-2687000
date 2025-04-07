# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
# 3. Crie um dicionário vazio para armazenar a nota do curso
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota
cursos_Linkedin = ['JavaSript','R','SQL','Python','C++']
curso_A = 'JavaScript'
curso_B = 'SQL'
curso_C = 'Python'
rank = {}
if curso_A in cursos_Linkedin:
  print(f"O curso {curso_A} está no catalogo. Por favor, avalie o curso.")
  rank[curso_A]= int(input('Qual a nota que você avalia o curso (0 a 5)?'))
if curso_B in cursos_Linkedin:
  print(f"O curso {curso_B} está no catalogo. Por favor, avalie o curso.")
  rank[curso_B]= int(input('Qual a nota que você avalia o curso (0 a 5)?'))
if curso_C in cursos_Linkedin:
  print(f"O curso {curso_C} está no catalogo. Por favor, avalie o curso.")
  rank[curso_C]= int(input('Qual a nota que você avalia o curso (0 a 5)?'))
print(rank)