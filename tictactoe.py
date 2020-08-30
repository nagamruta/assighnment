def game_board(char_list):
    print("\n      Tic Tac Toe Game")
    print("\t~~~~~~~~~~~")
    print("\t||"+char_list[0]+"||"+char_list[1]+"||"+char_list[2]+"||")
    print("\t~~~~~~~~~~~")
    print("\t||"+char_list[3]+"||"+char_list[4]+"||"+char_list[5]+"||")
    print("\t~~~~~~~~~~~")
    print("\t||"+char_list[6]+"||"+char_list[7]+"||"+char_list[8]+"||")
    print("\t~~~~~~~~~~~")

def player_gameplay(player_name,char_list):
    player_move=int(input(player_name+":Enter number between (1 to 9):-"))
    if player_move>0 and player_move<=9:
        if char_list[player_move-1]=='_':
            return player_move
        else:
            print("Spot is already taken,TRY AGAIN")
    else:
        print("INVALID spot,TRY AGAIN")

def player_char_on_board(player_name,player_move,char_list):
    char_list[player_move-1]=player_name

def winner(char_list,player_name):
    return((char_list[0]==player_name and char_list[1]==player_name and char_list[2]==player_name)or
           (char_list[3]==player_name and char_list[4]==player_name and char_list[5]==player_name)or
           (char_list[6]==player_name and char_list[7]==player_name and char_list[8]==player_name)or
           (char_list[0]==player_name and char_list[3]==player_name and char_list[6]==player_name)or
           (char_list[1]==player_name and char_list[4]==player_name and char_list[7]==player_name)or
           (char_list[2]==player_name and char_list[5]==player_name and char_list[8]==player_name)or
           (char_list[0]==player_name and char_list[4]==player_name and char_list[8]==player_name)or
           (char_list[6]==player_name and char_list[4]==player_name and char_list[2]==player_name))

player_1='X'
player_2='O'
c_list=['_']*9
n_list=['1','2','3','4','5','6','7','8','9']
game_board(n_list)
game_board(c_list)
while True:
    move=player_gameplay(player_1,c_list)
    player_char_on_board(player_1,move,c_list)
    game_board(n_list)
    game_board(c_list)
    if winner(c_list,player_1):
        print(player_1+"player wins")
        break
    elif '_' not in c_list:
        print("Game tie")
        break
    move=player_gameplay(player_2,c_list)
    player_char_on_board(player_2,move,c_list)
    game_board(n_list)
    game_board(c_list)
    if winner(c_list,player_2):
        print(player_2+"player wins")
        break
    elif '_' not in c_list:
        print("Game tie")
        break
