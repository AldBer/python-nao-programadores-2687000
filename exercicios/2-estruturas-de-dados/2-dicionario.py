pessoa = {'nome':'Fernanda',
          'idade':36,
          'ano_formatura':2008,
          'linguagens_programacao':['python','r','javascript','ruby'],
          'brasileira':True,
          'hobby':['nadar','ler','caminhar'],
          'animal_estimacao':False}
# Imprima na tela o valor equivalente a chave "hobby"
print(pessoa['hobby'])
# Imprima na tela uma lista apenas com os valores do dicionário
print(pessoa)
# Imprima na tela uma lista apenas com as chaves do dicionário
pessoa.keys()
# Insira um novo par chave-valor no dicionário
pessoa['nascimento'] = 1988