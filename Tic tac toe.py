from random import randrange

def display_board(board):
    """Muestra el tablero actual."""
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def enter_move(board):
    """Solicita el movimiento del usuario y lo valida"""
    while True:
        try:
            move = int(input("Ingresa tu movimiento: "))
            if move < 1 or move > 9:
                print("Numero invalido, intente de nuevo")
                continue

            row, col = (move - 1) // 3, (move - 1) % 3
            if board[row][col] in ['0', 'X']:
                print("Ese cuadro ya esta ocupado.")
            else:
                board[row][col] = '0'
                break
        except valueError:
            print("Por favor, ingresa un numero entero.")

def make_list_of_free_fields (board):
    """Retorna una lista con las coordenadas con los cuadros libres."""
    free = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['0', 'X']:
                free.append((r, c))
    return free

def victory_for(board, sign):
    """Verifica si el jugador con el signo dado ha ganado"""
    # Filas y columnas
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)) or \
           all(board[j][i] == sign for j in range(3)):
            return True
    # Diagonales
    if (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or \
       (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign):
        return True
    return False

def draw_move(board):
    """La maquina realiza un movimiento aleatorio"""
    free = make_list_of_free_fields(board)
    if free:
        r, c = free[randrange(len(free))]
        board[r][c] = 'X'

# --- Lógica principal ---
board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
display_board(board)

while True:
    enter_move(board)
    display_board(board)
    if victory_for(board, '0'):
        print("¡Has ganado!")
        break

    if not make_list_of_free_fields(board):
        print("¡Es un empate!")
        break

    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):
        print("¡La maquina ha ganado!")
        break

    if not make_list_of_free_fields(board):
        print("¡Es un empate!")
        break        
