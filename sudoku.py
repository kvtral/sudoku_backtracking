#################################################################
# El codigo es una implementación de un taller de               #
# resolución con BACKTRACKING                                   #
# El autor del algoritmo es Tech With Tim                       #
# https://www.youtube.com/watch?v=eqUwSA0xI-s&pbjreload=10      #
#                                                               #
#################################################################


# Este es el tablero inicial del juego, los 0 representan los espacios vacios
brd = [
    [9, 0, 0, 1, 0, 0, 0, 0, 4],
    [0, 6, 0, 7, 0, 2, 0, 8, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 6, 3, 0, 0],
    [4, 3, 0, 2, 0, 0, 0, 0, 8],
    [0, 0, 6, 4, 9, 0, 0, 0, 0],
    [0, 2, 0, 9, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 6, 0, 0]
]


def resuelve(board):
    vacio = find_empty(board)
    if not vacio:
        return True
    else:
        fila, colu = vacio

    for num in range(1, 10):
        if valido(board, num, (fila, colu)):
            board[fila][colu] = num

            if resuelve(board):
                return True

            board[fila][colu] = 0

    return False


def valido(board, num, pos):
    
    #Valida las filas
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Valida las columnas
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Valida cada cuadro
    cuadro_x = pos[1] // 3
    cuadro_y = pos[0] // 3

    for i in range(cuadro_y*3, cuadro_y*3 + 3):
        for j in range(cuadro_x*3, cuadro_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def show_board(board):
    for i in range(len(board)):
        if i % 3 == 0:
            if i == 0:
                print(" ┎─────────┰─────────┰─────────┒")
            else:
                print(" ┠─────────╂─────────╂─────────┨")

        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" ┃ ", end=" ")

            if j == 8:
                if board[i][j] == 0:
                    print("   ┃")
                else:    
                    print(board[i][j], " ┃")
            else:
                if board[i][j] == 0:
                    print(" ", end=" ")
                else:
                    print(board[i][j], end=" ")

    print(" ┖─────────┸─────────┸─────────┚")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j  # fila, columna

    return None

print ("Tablero Ingresado")
show_board(brd)
print('\n____________________________________\n')
resuelve(brd)
show_board(brd)