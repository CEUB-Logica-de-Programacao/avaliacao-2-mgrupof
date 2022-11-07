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
    dict = {}
    for i in range(0,len(names)):
        dict[names[i]] = heights[i]
    def y():
        d = {}
        lista = []
        d2 = sorted(dict.values(), reverse= True)
        for i in d2:
            for j in dict.keys():
                if dict[j] == i:
                    d[j] = dict[j]
        for j in d.keys():
            lista.append(j)
        return lista
    return y()
if __name__ == '__main__':
    print(q1(["Mary", "John", "Emma"], [180, 165, 170]))

