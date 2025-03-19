import random 

boards = [' ']*9
choices = ['O', 'X']

def display_game():
    print("\n -------------- Welcome to Tic Tac Toe ---------------- \n\n\n")
    print(f'                {boards[0]} | {boards[1]} | {boards[2]} ')
    print("               ---|---|---")
    print(f'                {boards[3]} | {boards[4]} | {boards[5]} ')
    print("               ---|---|---")
    print(f'                {boards[6]} | {boards[7]} | {boards[8]} \n\n\n')

def check_winner(player) :
    condition = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(boards[i] == player for i in win_position) for win_position in condition) 

def check_board_full() :
    return ' 'not in boards

def cpu_choice() :
    positions = [i for i, val in enumerate(boards) if val==' ']
    return random.choice(positions)


while True :
    display_game()

    while True:
        try : 
            user_input = int(input("Enter choices between(1-9) :")) - 1
            user_symbol = input("Enter your choice :").upper()

            if  0 <= user_input <= 9 and boards[user_input]== ' ' and user_symbol in choices :
                boards[user_input] = user_symbol
                break
            else :
                print("Invalid input... ")

        except ValueError:
            print("Enter a valid number ...")

    if check_winner(user_symbol):
        display_game()
        print(f'You win!')
        break

    if check_board_full():
        display_game()
        print("D-R-A-W")
        break

    cpu_move = cpu_choice()
    cpu_symbol = random.choice(choices)
    boards[cpu_move] = cpu_symbol

    print(f'CPU chose position {cpu_move+1} and symbol {cpu_symbol}')

    if check_winner(cpu_symbol):
        display_game()
        print(f"CPU win!")
        break

    if check_board_full():
        display_game()
        print("D-R-A-W")
        break

