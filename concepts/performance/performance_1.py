"""performance"""

# nos dois exemplos abaixo existe uma diferenca de performance pois
# no primeiro exemplo, o for ira percorrer cada item de lista
# em contrapartida, no segundo exemplo, como temos um conjunto e este
# conjunto se assemelha a dicionario pelo uso de hash. Buscas por hash
# sao muito rapidas e a diferenca entre velocidade se torna significativa
# em colecoes maiores

x = list((1, 2, 3, 4))
y = set((1, 2, 3, 4))

for i in x:
    pass


for j in y:
    pass

# pesquisas em listas sao O(n)
# pesquisas em dicionarios sao O(1)
            