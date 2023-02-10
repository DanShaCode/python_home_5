row = str(input("Введите номер строки: "))
col = str(input("Введите номер колонки: "))
key = row + col
board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
game_dict = {'11': 'X'}
if key == '11':
    board.replace(board[0], 'X')
print(*board)