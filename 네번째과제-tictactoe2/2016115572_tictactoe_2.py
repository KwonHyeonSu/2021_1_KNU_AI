game_board = [' ', ' ', ' ',
              ' ', ' ', ' ',
              ' ', ' ', ' ']
player = 'O'

def sketch(board):
    for i, cell in enumerate(board):
        if i % 3 == 0:
            print('\n---------------')
        print('|',cell,'|',end='')
    print('\n---------------')

def get_input():
    while True:
        a = input("값을 입력하세요 ex) 1,1 / 2,3 : ")
        b = int(a[-1])
        a = int(a[0])
        val = 3*(a-1) + b - 1
        if valid_move(val):
            game_board[val] = 'X'
            break
        else:
            print('\n[잘못된 이동]이미 둔 자리입니다. 다시 입력하세요.\n')
            sketch(game_board)

def empty_cells(board):
    cells = []
    for x,cell in enumerate(board):
        if cell == ' ':
            cells.append(x)
    return cells

def check_win(board, player):
    win_board = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    return [player, player, player] in win_board

def game_over(board):
    return check_win(board, 'X') or check_win(board, 'O')

def evaluate(board):
    if check_win(board, 'X'):
        score = 1
    elif check_win(board, 'O'):
        score = -1
    else:
        score = 0
    return score

def valid_move(x):
    return x in empty_cells(game_board)

def move(x, player):
    if valid_move(x):
        game_board[x] = player
        return True
    return False

def minimax(board, depth, maxPlayer):
    pos = -1
    if depth == 0 or len(empty_cells(board)) == 0 or game_over(board):
        return -1, evaluate(board)

    if maxPlayer:
        value = -10000
        for p in empty_cells(board):
            board[p] = 'X'
            x, score = minimax(board, depth-1, False)
            board[p] = ' '
            if score > value:
                value = score
                pos = p
    
    else:
        value = 10000
        for p in empty_cells(board):
            board[p] = 'O'

            x, score = minimax(board, depth-1, True)
            board[p] = ' '
            if score < value:
                value = score
                pos = p

    return pos, value

if __name__ == '__main__':
    print("플레이어가 먼저 시작합니다.")
    sketch(game_board)
    while True:
        
        #게임 끝나는 조건 - 빈공간 없을 때, 게임 끝났을 때,
        if len(empty_cells(game_board)) == 0 or game_over(game_board):
            break
        get_input()
        sketch(game_board)
        print('인공지능의 차례입니다.')
        i, v = minimax(game_board, 9, player=='X')
        move(i, player)
        sketch(game_board)
        
    if check_win(game_board, 'X'):
        print('X Win!')
    elif check_win(game_board, 'O'):
        print('O Win!')
    else:
        print('Draw!')
        


    
    
    