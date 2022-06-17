def get(linhaIndex, colunaIndex, matrix):
    for l in range(len(matrix)):
        if l == linhaIndex:
            for c in range(len(matrix[l])):
                if c == colunaIndex:
                    return matrix[l][c]

def imprimirMatrizOculta(matriz):
    print("---Matriz de exibição--- \n %s" % matriz)

def iniciar(matrizOculta,matriz,paresDeRespostas):
    vezesMatrizExibidas: int = 0
    respostasCertas: int = 0
    totalRespostasCertas: int = paresDeRespostas
    while respostasCertas < totalRespostasCertas:
        if vezesMatrizExibidas <= 2:
            exibirResposta: int = int((input("Deseja exibir matriz original?1-sim, 2-não")))
            if exibirResposta == 1:
                vezesMatrizExibidas = vezesMatrizExibidas + 1
                print(matriz)
        linhaPrimeiroQuadrante: int = int(input("Digite a linha do primeiro quadrante. Baseado em 0!"))
        colunaPrimeiroQuadrante: int = int(input("Digite a coluna do primeiro quadrante. Baseado em 0!"))
        letra = get(linhaPrimeiroQuadrante, colunaPrimeiroQuadrante, matriz)
        print("Letra %s " % letra)
        linhaSegundoQuadrante: int = int(input("Digite a linha do segundo quadrante. Baseado em 0!"))
        colunaSegundoQuadrante: int = int(input("Digite a coluna do segundo quadrante. Baseado em 0!"))
        letraSegundoQuadrante = get(linhaSegundoQuadrante, colunaSegundoQuadrante, matriz)
        if letra == letraSegundoQuadrante:
            print("Você acertou!!")
            matrizOculta[linhaPrimeiroQuadrante][colunaPrimeiroQuadrante] = letra
            matrizOculta[linhaSegundoQuadrante][colunaSegundoQuadrante] = letraSegundoQuadrante
            print("---Matriz de exibição--- \n %s" % matrizOculta)
            respostasCertas = respostasCertas + 1
            print("Restam %s pares para completar o jogo!" % (totalRespostasCertas - respostasCertas))
        else:
            print("Você errou!")
    print("Jogo completado com sucesso!")

def facil():
    print("---Iniciando jogo na dificuldade fácil---")
    matriz4por4 = [['Z', 'A', 'Z', 'A'], ['X', 'O', 'P', 'Z'], ['N', 'P', 'M', 'N'], ['M', 'C', 'O', 'X']]
    matriz4por4Oculta = [["#", "#", "#", "#"], ["#", "#", "#", "#"], ["#", "#", "#", "#"], ["#", "#", "#", "#"]]
    imprimirMatrizOculta(matriz4por4Oculta)
    iniciar(matriz4por4Oculta,matriz4por4,7)
def medio():
    print("---Iniciando jogo na dificuldade média...---")
    matriz8por8 = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], ['Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X'],
                   ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'], ['Y', 'Z', 'Z', 'B', 'Y', 'D', 'E', 'F'],
                   ['G', 'N', 'P', 'I', 'I', 'P', 'G', 'N'], ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'],
                   ['Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']]
    matriz8por8Oculta = [['#', '#', '#', '#', '#', '#', '#', '#'], ['#', '#', '#', '#', '#', '#', '#', '#'],
                         ['#', '#', '#', '#', '#', '#', '#', '#'], ['#', '#', '#', '#', '#', '#', '#', '#'],
                         ['#', '#', '#', '#', '#', '#', '#', '#'], ['#', '#', '#', '#', '#', '#', '#', '#'],
                         ['#', '#', '#', '#', '#', '#', '#', '#'], ['#', '#', '#', '#', '#', '#', '#', '#']]

    imprimirMatrizOculta(matriz8por8Oculta)
    iniciar(matriz8por8Oculta,matriz8por8,26)

dificuldade: int = int(input("Selecione a dificuldade. 1-Fácil, 2-Médio ou 3-Difícil"));
if dificuldade == 1:
    facil()
elif dificuldade == 2:
   medio()
else:
    print("---Iniciando jogo na dificuldade difícil...---")
