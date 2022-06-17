# Nicholas Barbosa, Gustavo Fiori e Luis Choinski
import random
import time

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'F', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


def get(linha_index, coluna_index, matriz):
    for l in range(len(matriz)):
        if l == linha_index:
            for c in range(len(matriz[l])):
                if c == coluna_index:
                    return matriz[l][c]


def imprimir_matriz_oculta(matriz):
    print("---Matriz de exibição--- \n %s" % matriz)


def frequencia_letra(letra, matriz):
    vezes = 0
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if matriz[l][c] == letra:
                vezes = vezes + 1
    return vezes


def gera_matriz_combinacoes(matriz):
    print("---Gerando combinações---")
    combinacoes: int = 0
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if frequencia_letra(matriz[l][c], matriz) == 2:
                combinacoes = combinacoes + 1

    return combinacoes


def cria_matriz(numero_linhas, numero_colunas, oculta):
    matriz = []
    for l in range(numero_linhas):
        matriz.append([])
        for c in range(numero_colunas):
            if oculta == 1:
                matriz[l].append("#")
            else:
                matriz[l].append(gera_character())

    return matriz


def gera_character():
    posicao_aleatoria: int = random.randint(0, 25)
    return alfabeto[posicao_aleatoria]


def iniciar(matriz_oculta, matriz):
    vezes_matriz_exibida: int = 0
    respostas_certas: int = 0
    total_combinacoes: int = gera_matriz_combinacoes(matriz)
    if total_combinacoes >= 1:
        print("Existem %s combinações. Acerte todas para completar o jogo!" % total_combinacoes)
        while respostas_certas < total_combinacoes:
            encerar: int = int(input("Deseja encerrar o jogo?1-Sim, 2-Não"))
            if encerar == 1:
                print("Encerrando jogo...")
                break
            if vezes_matriz_exibida <= 2:
                exibir_resposta: int = int((input("Deseja exibir matriz original?1-sim, 2-não")))
                if exibir_resposta == 1:
                    vezes_matriz_exibida = vezes_matriz_exibida + 1
                    print("Matriz estará visivel por apenas 3 segundos!")
                    print(matriz)
                    time.sleep(3)
                    print("\n" * 100)
            linha_primeiro_quadrante: int = int(input("Digite a linha do primeiro quadrante. Baseado em 0!"))
            coluna_primeiro_quadrante: int = int(input("Digite a coluna do primeiro quadrante. Baseado em 0!"))
            letra = get(linha_primeiro_quadrante, coluna_primeiro_quadrante, matriz)
            print("Letra %s! " % letra)
            linha_segundo_quadrante: int = int(
                input("Digite a linha do segundo quadrante. Baseado em 0! Ou -1 para sair!"))
            coluna_segundo_quadrante: int = int(
                input("Digite a coluna do segundo quadrante. Baseado em 0! Ou -1 para sair!"))
            if linha_segundo_quadrante == linha_primeiro_quadrante & coluna_primeiro_quadrante == coluna_segundo_quadrante:
                print(
                    "Jogo será finalizado por tentativa de trapaça! \nMotivo: deslacamentos de quadrantes. Jogue limpo!")
                break;
            letraSegundoQuadrante = get(linha_segundo_quadrante, coluna_segundo_quadrante, matriz)
            if letra == letraSegundoQuadrante:
                print("Você acertou!!")
                matriz_oculta[linha_primeiro_quadrante][coluna_primeiro_quadrante] = letra
                matriz_oculta[linha_segundo_quadrante][coluna_segundo_quadrante] = letraSegundoQuadrante
                print("---Matriz de exibição--- \n %s" % matriz_oculta)
                respostas_certas = respostas_certas + 1
                print("Restam %s pares para completar o jogo!" % (total_combinacoes - respostas_certas))
            else:
                print("Você errou!")
            print("Jogo finalizado!")
    else:
        print("Rodada bonus! Você está com sorte! Não foram geradas combinações. Tente novamente!1-Sim,2-Não")
        tentar_novamente: int = int(input())
        if tentar_novamente == 1:
            iniciar(matriz_oculta, matriz)


def facil():
    print("---Iniciando jogo na dificuldade fácil---")
    matriz4por4 = cria_matriz(4, 4, 0)
    matriz4por4_oculta = cria_matriz(4, 4, 1)
    imprimir_matriz_oculta(matriz4por4_oculta)
    iniciar(matriz4por4_oculta, matriz4por4)


def medio():
    print("---Iniciando jogo na dificuldade média...---")
    matriz8por8 = cria_matriz(8, 8, 0)
    matriz8por8_oculta = cria_matriz(8, 8, 1)
    imprimir_matriz_oculta(matriz8por8_oculta)
    iniciar(matriz8por8_oculta, matriz8por8)


def dificil():
    print("---Iniciando jogo na dificuldade difícil...---")
    matriz10por10 = cria_matriz(10, 10, 0)
    matriz10por1_oculta = cria_matriz(10, 10, 1)
    imprimir_matriz_oculta(matriz10por1_oculta)
    iniciar(matriz10por1_oculta, matriz10por10)


dificuldade: int = int(input("Selecione a dificuldade. 1-Fácil, 2-Médio ou 3-Difícil"));
if dificuldade == 1:
    facil()
elif dificuldade == 2:
    medio()
else:
    dificil()
