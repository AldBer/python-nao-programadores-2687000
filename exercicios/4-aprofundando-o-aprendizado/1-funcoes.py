# Crie uma função para selecionar o curso desejado em uma trilha profissional
# Crie uma função para percorrer todos os níveis de um curso e imprimir na tela a informação do nível atual
# Execute as funções
def seleciona_trilha_curso():
  curso = int(input('Digite o numero do curso que voce deseja iniciar:1 - Introdução a SQL 2 - Python: Programação Basica'))
  return curso
def percorre_curso (curso_selecionado):
  trilha = {1: {'titulo': 'Introdução a SQL','total_niveis': 3},
            2: {'titulo': 'Python:Programação Basica','total_niveis': 5}}
  curso_atual = trilha[curso_selecionado]['titulo']
  curso_nivel_atual = 1
  curso_total_niveis = trilha[curso_selecionado]['total_niveis']

  print(f'Bem vindo ao curso "{curso_atual}!. Você está iniciando do curso no nivel{curso_nivel_atual}.\n...')
  while curso_nivel_atual <= curso_total_niveis:
    print(f'Parabéns! Você acaba de finalizar a fase {curso_nivel_atual} do curso "{curso_atual}".')
    curso_nivel_atual += 1
  else:
    print(f'Você concluiu o curso {curso_atual} com sucesso.')
curso = seleciona_trilha_curso()
percorre_curso(curso)