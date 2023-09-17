
teams = [1, 2, 3, 4]

team_dict = {
    '1': 'A',
    '2': 'B',
    '3': 'C',
    '4': 'D'
}

def print_answer(board):
    f = open('confrontos.txt', 'a')
    print('Confrontos: \n')
    f.write('Confrontos: \n\n')       
    for i in range(0, 12):
        print(team_dict[str(board[i][0])] + ' X ' + team_dict[str(board[i][1])])
        f.write(team_dict[str(board[i][0])] + ' X ' + team_dict[str(board[i][1])] + '\n')
        if(i == 5):
                print("-----")
                f.write("-----\n")    
    print('\n\n')
    f.write('\n\n\n')

def check_answer(board, line):

    confrontos_0to6 = [
        {"2": 0, "3": 0, "4": 0}, {"1": 0, "3": 0, "4": 0}, {"1": 0, "2": 0, "4": 0}, {"1": 0, "2": 0, "3": 0}
    ]

    confrontos_6to12 = [
        {"2": 0, "3": 0, "4": 0}, {"1": 0, "3": 0, "4": 0}, {"1": 0, "2": 0, "4": 0}, {"1": 0, "2": 0, "3": 0}
    ]

    for j in range(0, min(line, 6)):
        confrontos_0to6[board[j][0]-1][str(board[j][1])] = confrontos_0to6[board[j][0]-1][str(board[j][1])]+1
        confrontos_0to6[board[j][1]-1][str(board[j][0])] = confrontos_0to6[board[j][1]-1][str(board[j][0])]+1

    for x in confrontos_0to6:
        for y in x:
            if(line <= 6):
                if(x[y] > 1): return False

    if(line >= 7):
        for j in range(6, min(line, 12)):
            confrontos_6to12[board[j][0]-1][str(board[j][1])] = confrontos_6to12[board[j][0]-1][str(board[j][1])]+1
            confrontos_6to12[board[j][1]-1][str(board[j][0])] = confrontos_6to12[board[j][1]-1][str(board[j][0])]+1

        for x in confrontos_6to12:  
            for y in x:
                if(line >= 7):
                    if(x[y] > 1): return False

    for i in range(0, 4):
        count = 0
        count_2 = 0

        count_n_j = 0
        count_n_j_2 = 0

        for j in range(0, line):
            if(board[j][0] == teams[i] or board[j][1] == teams[i]):
                count+=1
                count_n_j = 0
            else:
                count = 0
                count_n_j += 1

            if(count > 2): return False
            elif(count == 2): count_2+=1

            if(count_n_j > 2): return False
            elif(count_n_j == 2): count_n_j_2 += 1


        if(count_n_j_2 > 1 or count_2 > 1): return False

        if(line >= 12):
            if(count_n_j_2 != 1 or count_2 != 1): return False

    if(line >= 12):
        print("Got a Answer")
        print_answer(board)
        return True  
    else:
        print("Got a False End State")
        return True



def backtrack(board, line, col, count):

    ret = check_answer(board, line)

    if(ret == False): return False
    
    if(ret == True and line == 12): return False

    for x in teams:
        if(count[x-1] <= 6):
            if(board[line][(col+1)%2] != x):
                board[line][col] = x
                count[x-1] += 1
                ret = False
                if col == 0:
                    ret = backtrack(board.copy(), line, col+1, count.copy())
                else:
                    ret = backtrack(board.copy(), line+1, 0, count.copy())
                count[x-1] -= 1

                if(ret == True): return True


    return False

init_state = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0]
]

if backtrack(init_state, 0, 0, [0, 0, 0, 0]) == False:
    print("No Solution")
else:
    print("Got Solution")



