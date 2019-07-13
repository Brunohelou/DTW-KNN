import csv   #importa a biblioteca que le os txt como csv para serem importados como lista
import time


def funcaocriterio(q, matrizauxiliar, criterio, u, valor):
    if q <= 12:  # rodará  as 12 posições de 1a 12  da lista matrizauxiliar
        if criterio == matrizauxiliar[q] : # compara se os valores são iguais
            if matrizauxiliar[q] == 0:
                return funcaocriterio(q+1, matrizauxiliar, criterio, u, valor)
            matrizauxiliar.sort()
            if criterio == matrizauxiliar[len(matrizauxiliar)-1]:
                u+=1
                matrix=[] # declara novamente matrix, para poder zerá-la
                makematrix(matrix, 0 ,u) # cria matrix novamente adicionando mais um valor a k , desse modo haverá um valor a mais de rótulo até que haja desempate
                e=0
                matrizauxiliar=[]
                while e <= 12:
                    matrizauxiliar.append(matrix.count(e))
                    e += 1 # gera novamente a matrizauxiliar com os novos valores de rotulos
                return funcaocriterio(1,matrizauxiliar,0, u,0)
            else:
                return funcaocriterio(q + 1, matrizauxiliar, criterio, u, valor)
        if criterio < matrizauxiliar[q]:
            criterio = matrizauxiliar[q]
            valor=q
            return funcaocriterio(q+1, matrizauxiliar, criterio,u, valor)
        if criterio > matrizauxiliar[q]:
            return funcaocriterio(q + 1, matrizauxiliar, criterio, u, valor)
    else:
        return valor
    # funcaocriterio escolhe o valor de rótulos que mais aparece para comparar com o rótulo de teste.
def makematrix(matrix, b, u):
    while b < u:
        if matrizurna[b][1]!=None:
            matrix.append(matrizurna[b][1])
            b += 1
    return None
# def makematrix cria a função make matrix, responsável por setar na lista matrix os rotulos dos 'k' meores valores(tamanho da vizinhança)
def geramatrizauxiliar(e, matrix):
    while e<=12:
        matrizauxiliar.append(matrix.count(e))
        e+=1
# define como função 'geramatriauxiliar' que recebe o valor de vezes que os rotulos de 0 a 12 se repetem na matrix nas posições de 0 a 12.
u = int(input('qual valor de K desejado?')) #u é o valor k desejado para acurácia
inicio = time.clock()
listas12 = [] # lista teste que nao ficará sem os rotulos
listas22 = [] # lista treino que nao ficará sem os rotulos
listas1 = [] # lista teste que ficará sem os rotulos
with open('teste.txt') as csvfile: # abre o arquivo teste.txt como arquivo csv
    testes = csv.reader(csvfile, delimiter=' ') #cria o csv definido anteriormente a partir da divisão ' '
    for linha in testes:
        listas1.append(linha)  # adiciona a lista desejada cada linha do txt como uma lista
listas2 = []
with open('treino.txt') as csvfile:
    testes = csv.reader(csvfile, delimiter=' ')
    for linha in testes:
        listas2.append(linha)
with open('teste.txt') as csvfile:
    testes = csv.reader(csvfile, delimiter=' ')
    for linha in testes:
        listas12.append(linha)
with open('treino.txt') as csvfile:
    testes = csv.reader(csvfile, delimiter=' ')
    for linha in testes:
        listas22.append(linha)
f = len(listas1) # da a f o valor do tamanho da lista desejada, nesse caso listas1
correto =0 # seta valor inicial para testes corretos
errado = 0 #seta valor inicial para testes incorreots
n = 0
while n < f:
    del listas1[n][0]
    n += 1                  #deleta da listas1 os rótulos
f = len(listas2)
n = 0
while n < f:
    del listas2[n][0]
    n += 1
                            #deleta da listas2 os rótulos
a = []  # lista qualquer para servir como modo de comparação a uma lista vazia
w = 0   # w é a linha do txt teste a qual será usada
while w < len(listas1):

    k = 0 # k será a linha do txt treino a qual sera usada
    matrizurna = [] # cria matriz urna, que reseta para cada linha de teste
    temp1 = time.clock()
    while k < len(listas2):

        matriz2 = [] # a matriz2 será a lista que receberá os valores calculados pelo dtw
        c = 0
        j = 0
        t = len(listas2[k])
        tempodtw1 = time.clock()
        while j < t:


            ma2 = float(listas2[k][j])
            i = 0
            matriz = [] # cada lista que será calculada e adicionada a matriz2, pode ser entendida como cada linha da matriz do dtw

            while i < len(listas1[w]):
                ma1 = float(listas1[w][i])
                if matriz2 != a and matriz == a:
                    c = matriz2[j - 1][i]
                if matriz2 != a and matriz != a:
                    c = min(matriz2[j - 1][i - 1], matriz2[j - 1][i], matriz[i - 1])
                s = abs(ma1 - ma2) + c
                matriz.append(s)
                if matriz2 == a:
                    c = s
                i += 1


            matriz2.append(matriz)

            j += 1


            # de 80 a 100 faz o calculo do dtw
        tempodtw2 = time.clock()

        p = len(matriz2) - 1 # recebe o numero de linhas do dtw
        x = len(matriz2[p - 1]) - 1 # recebe o tamanho da linha p-1 do dtw
        j = float(listas22[k][0])  #  transforma em float o rotulos da linha do treino usada
        voto = matriz2[p][x], j #
        #print('dtw', matriz2)
        matrizurna.append(voto) # recebe o ultimo valor do DTW e o rótulo da lista treino usada no calculo
        k += 1
    tempoknn1 = time.clock()
    tempoal1 = time.clock()
    #print(matrizurna)
    matrizurna.sort() # ordena com timsort a matrizurna, colocando do menor pro maior de acordo com o valor do DTW os votos.
    tempoknn2 = time.clock()



    matrix = [] # lista que receberá com os rotulos dos menores valores

    makematrix(matrix, 0, u) # seta dos valores para matrix. (explicação do que faz está após o def maakematrix)
    matrizauxiliar=[]  # recebe em cada posição o numero de votos que teve para o rotulo. por exemplo: a posição 0 recebe o numeros de votos que o rotulo 0 recebeu, a posição 1 recebe a quantidade de votos que o rotulo 1 recebeu e assim por diante

    geramatrizauxiliar(0, matrix) # gera a matrzizauxiliar, que está explicada apos o def matrizauxiliar

    valor = funcaocriterio(1,matrizauxiliar,0, u, 0)
    tempoal2 = time.clock()

    #print(temp2-temp1)
    r = float(listas12[w][0]) # transforma em float o valor do rótulo do txt teste em questão
    if valor == r: # compara os rótulos
        correto+=1
        print('estão corretos:',correto)
        print('estão errados:', errado)
    else:
        errado+=1
        print('estão corretos:', correto)
        print('estão errados:', errado)
    temp2 = time.clock()
    #print('tempo 1 classificação:', temp2 - temp1)
    w += 1
#print('porcentagem de acerto:',correto/960,'%')
fim = time.clock()
#print('total do códido',fim - inicio)
#print('tempo knn inteiro',tempoal2-tempoal1)
#print('tempo ordenação k vizinhos:', tempoknn2-tempoknn1)
#print('tempo dtw ', tempodtw2 - tempodtw1)
print('estão corretos:',correto)
print('estão errados:', errado)

