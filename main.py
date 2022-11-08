import math
import pandas as pd

# > Função que retorna a distância mínima entre dois clusters
def minDistance(clusterA, clusterB, length, dimension):
    minDistance = -1
    for i in range(0, length):
        sqrDistance = 0
        for j in range(0, dimension):
            sqrDistance += (clusterA[i][j] - clusterB[i][j])**2
        distance = math.sqrt(sqrDistance)
        if  distance < minDistance or minDistance < 0:
            minDistance = distance
    return minDistance

# > Leitura dos dados
file = './customer_data.csv'
data = pd.read_csv(file)

# > Transformação de idade e gênero de em variáveis numéricas 
# > Retirada da coluna de ID
# > Normalização dos dados
data['Age Groups'] = pd.cut(data['Age'], [10, 20, 30, 40, 50, 60, 70])
encoded_data = pd.get_dummies(data, columns=['Age Groups', 'Genre'])
del encoded_data['CustomerID']
encoded_data = encoded_data.apply(lambda x: (x - x.mean()) / x.std(), axis=0)

# > A ideia base será criar um vetor que indique cada cliente da base
# original, de forma que, após o agrupamento, seja possível recuperar
# as informações
seeker = list(range(0, data['CustomerID'].size))

testeA = encoded_data.transpose()[0].values
testeB = encoded_data.transpose()[1].values

print(
    testeA
    #minDistance(testeA, testeB, 2, 11)
)