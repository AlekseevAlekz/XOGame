field_ = [['-' for _ in range(3)]for _ in range(3)]


def print_field(pf):
    for row in pf:
        for cell in row:
            print(cell, end= '   ')
        print()

def check_win (pf, plr):
    for row in pf:
        if row.count(plr) == 3:
            return True

    for i in range(3):
        if pf[0][i] == plr and pf[1][i] == plr and pf[2][2] == plr:
            return True

    if pf[0][0] == plr and pf[1][1] == plr and pf[2][2] == plr:
        return True
    if pf[0][2] == plr and pf[1][1] == plr and pf[2][0] == plr:
        return True

current_player = 'X'

while True:
    print_field(field_)
    print('Ход игрока: ', current_player)
    st = int(input('Введите номер строки: ')) - 1
    column = int(input('Введите номер столбца: ')) - 1

    if field_[st][column] != '-':
        print('Ячейка занята!')
        continue

    field_[st][column] = current_player

    if check_win(field_, current_player):
        print_field(field_)
        print(f'Игрок {current_player} выиграл!')
        break

    if all([cell != '-' for row in field_ for cell in row]):
        print_field(field_)
        print('Ничья')
        break

    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


#print_field(field_)

