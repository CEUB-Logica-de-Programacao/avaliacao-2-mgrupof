# Você recebe uma lista de nomes, e uma lista de alturas que consiste de números inteiros positivos distintos.
# Ambas as listas são de comprimento `n`.
#
# Para cada índice `i`, `nomes[i]` e `alturas[i]` denotam o nome e a altura da i-ésima pessoa.
#
# Retorne os nomes ordenados em ordem decrescente pelas alturas das pessoas.
#
# ### Exemplo 1
#
# ```
# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# ```
#
# ### Exemplo 2
#
# ```
# Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
# Output: ["Bob","Alice","Bob"]
# ```
def q1(names, heights):
    # Escreva seu código aqui
names = []
heights = []
total = []
x = int(input('Digite a quantidade de pessoas a serem adicionadas: '))
for i in range(0,x):
  nome = input('Digite o nome da pessoa: ')
  altura = input('Digite a altura da pessoa em cm (ex: 1,79 = 179): ')
  names.append(nome)
  heights.append(altura)
for i in range(x):
  tuple = (names[i],heights[i])
  total.append(tuple)
sorted(total, key=lambda names: names[1])
print(sorted(total, key=lambda names: names[1], reverse=True))


if __name__ == '__main__':
    print(q1(["Mary", "John", "Emma"], [180, 165, 170]))

