import random
import string

alafabeto = string.ascii_uppercase


def get(linhaIndex, colunaIndex, matrix):
    for l in range(len(matrix)):
        if l == linhaIndex:
            for c in range(len(matrix[l])):
                if c == colunaIndex:
                    return matrix[l][c]


def imprimirMatrizOculta(matriz):
    print("---Matriz de exibição--- \n %s" % matriz)

def frequenciaLetra(letra,matriz):
    vezes=0
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if matriz[l][c] == letra:
                vezes = vezes +1
    return vezes
def getMatrizCombinacoes(matriz):
    combinacoes:int = 0
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if frequenciaLetra(matriz[l][c],matriz) == 2:
                combinacoes=combinacoes+1
    return combinacoes

def criaMatriz(numero_linhas, numero_colunas, oculta):
    matriz = []
    for l in range(numero_linhas):
        matriz.append([])
        for c in range(numero_colunas):
            if oculta == 1:
                matriz[l].append("#")
            else:
                matriz[l].append(geraCharacter())

    return matriz


def geraCharacter():
    return ''.join(random.choice(alafabeto) for i in range(1))


def iniciar(matrizOculta, matriz):
    vezesMatrizExibidas: int = 0
    respostasCertas: int = 0
    totalCombinacoes:int= getMatrizCombinacoes(matriz)
    print("Existem %s combinações. Acerte todas para completar o jogo!"%totalCombinacoes)
    while respostasCertas < totalCombinacoes:
        if vezesMatrizExibidas <= 2:
            exibirResposta: int = int((input("Deseja exibir matriz original?1-sim, 2-não")))
            if exibirResposta == 1:
                vezesMatrizExibidas = vezesMatrizExibidas + 1
                print(matriz)
        linhaPrimeiroQuadrante: int = int(input("Digite a linha do primeiro quadrante. Baseado em 0!"))
        colunaPrimeiroQuadrante: int = int(input("Digite a coluna do primeiro quadrante. Baseado em 0!"))
        letra = get(linhaPrimeiroQuadrante, colunaPrimeiroQuadrante, matriz)
        print("Letra %s! " % letra)
        linhaSegundoQuadrante: int = int(input("Digite a linha do segundo quadrante. Baseado em 0!"))
        colunaSegundoQuadrante: int = int(input("Digite a coluna do segundo quadrante. Baseado em 0!"))
        letraSegundoQuadrante = get(linhaSegundoQuadrante, colunaSegundoQuadrante, matriz)
        if letra == letraSegundoQuadrante:
            print("Você acertou!!")
            matrizOculta[linhaPrimeiroQuadrante][colunaPrimeiroQuadrante] = letra
            matrizOculta[linhaSegundoQuadrante][colunaSegundoQuadrante] = letraSegundoQuadrante
            print("---Matriz de exibição--- \n %s" % matrizOculta)
            respostasCertas = respostasCertas + 1
            print("Restam %s pares para completar o jogo!" % (totalCombinacoes - respostasCertas))
        else:
            print("Você errou!")
    print("Jogo completado com sucesso!")


def facil():
    print("---Iniciando jogo na dificuldade fácil---")
    matriz4por4 = criaMatriz(4, 4, 0)
    matriz4por4Oculta = criaMatriz(4, 4, 1)
    imprimirMatrizOculta(matriz4por4Oculta)
    iniciar(matriz4por4Oculta, matriz4por4)
def medio():
    print("---Iniciando jogo na dificuldade média...---")
    matriz8por8 = criaMatriz(8,8,0)
    matriz8por8Oculta = criaMatriz(8,8,1)
    imprimirMatrizOculta(matriz8por8Oculta)
    iniciar(matriz8por8Oculta, matriz8por8)

def dificil():
    print("---Iniciando jogo na dificuldade difícil...---")
    matriz10por10 = criaMatriz(10, 10, 0)
    matriz10por1Oculta = criaMatriz(10, 10, 1)
    imprimirMatrizOculta(matriz10por1Oculta)
    iniciar(matriz10por1Oculta, matriz10por10)

dificuldade: int = int(input("Selecione a dificuldade. 1-Fácil, 2-Médio ou 3-Difícil"));
if dificuldade == 1:
    facil()
elif dificuldade == 2:
    medio()
else:
    dificil()
