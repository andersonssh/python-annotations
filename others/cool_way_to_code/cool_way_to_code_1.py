# pegar extensao do arquivo
# (lê da esquerda para a direita e separa a string
#  por "." apenas uma vez)

filename, extension = 'joao.test.jpg'.rsplit('.', 1)
print(extension)  # >>> jpg

# desempacotamento
n1, *nx = [1, 2, 3, 4, 5, 6]
print(n1, nx)  # >>> 1 [2, 3, 4, 5, 6]

first_number, *middle, last_number = [1, 2, 3, 4]
print(first_number, middle, last_number)  # >>> 1 [2, 3] 4

# cuidado ao fazer esse codigo
four_lists = [[]] * 4
four_lists[0].append('Oi')  # adicionando oi apenas ao primeiro item da lista de listas
print(four_lists)  # >>> [['Oi'], ['Oi'], ['Oi'], ['Oi']]
