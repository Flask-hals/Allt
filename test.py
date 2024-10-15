import random

def create_deck(): #Skapar en kortlek
    deck = []
    for i in range(1, 27):
        if i < 14:
            deck.append((i, 1))
        elif i < 27:
            deck.append((i, 2))
    deck.append((27, 1))
    deck.append((27, 2))
    return deck

def copy_deck(deck): #Kopierar en kortlek så man får två likadana
    deck2 = deck.copy()
    return deck2


def shuffle_deck(deck, n=0): #Blandar en kortlek om man endast skickar in deck som argument, skickar man in två argument aktiveras seed och kortleken blandas på samma sätt varje gång
    if n != 0:
        random.seed(n)
        random.shuffle(deck)
    else:
        random.shuffle(deck)
    return deck

def move_card(deck, cards, location): #Flyttar ett kort till en annan plats i kortleken
    card = deck.pop(cards)
    deck.insert(location, card)
    return deck

def remove_card(deck, n): 
    deck.pop(n)
    return deck

def read_card(deck, n):
    deck_dict = {"Ace of spades": (1, 1), "2 of spades": (2, 1), "3 of spades": (3, 1), "4 of spades": (4, 1), "5 of spades": (5, 1), "6 of spades": (6, 1), "7 of spades": (7, 1), "8 of spades": (8, 1), "9 of spades": (9, 1), "10 of spades": (10, 1), "Knight of spades": (11, 1), "Queen of spades": (12, 1), "King of spades": (13, 1), "Ace of hearts": (14, 2), "2 of hearts": (15, 2), "3 of hearts": (16, 2), "4 of hearts": (17, 2), "5 of hearts": (18, 2), "6 of hearts": (19, 2), "7 of hearts": (20, 2), "8 of hearts": (21, 2), "9 of hearts": (22, 2), "10 of hearts": (23, 2), "Knight of hearts": (24, 2), "Queen of hearts": (25, 2), "King of hearts": (26, 2), "Joker of spades": (27, 1), "Joker of hearts": (27, 2)}
    for cards in deck:
        if cards == deck[n - 1]:
            for key, value in deck_dict.items():
                if cards == value:           
                    return key
                
def read_deck(deck):
    deck_dict = deck_dict = {"Ace of spades": (1, 1), "2 of spades": (2, 1), "3 of spades": (3, 1), "4 of spades": (4, 1), "5 of spades": (5, 1), "6 of spades": (6, 1), "7 of spades": (7, 1), "8 of spades": (8, 1), "9 of spades": (9, 1), "10 of spades": (10, 1), "Knight of spades": (11, 1), "Queen of spades": (12, 1), "King of spades": (13, 1), "Ace of hearts": (14, 2), "2 of hearts": (15, 2), "3 of hearts": (16, 2), "4 of hearts": (17, 2), "5 of hearts": (18, 2), "6 of hearts": (19, 2), "7 of hearts": (20, 2), "8 of hearts": (21, 2), "9 of hearts": (22, 2), "10 of hearts": (23, 2), "Knight of hearts": (24, 2), "Queen of hearts": (25, 2), "King of hearts": (26, 2), "Joker of spades": (27, 1), "Joker of hearts": (27, 2)}
    for cards in deck:
        for key, value in deck_dict.items():
            if cards == value:
                return key

def split_deck_switch_order(deck, lowest, biggest):
    card = 0
    deck1 = []
    deck2 = []
    deck3 = []
    for cards in deck:
        if card < lowest:
            deck1.append(cards)
        elif card >= lowest and card <= biggest:
            deck2.append(cards)
        elif card > biggest:
            deck3.append(cards)
        card += 1
    deck.clear()
    deck.extend(deck3 + deck2 + deck1)
    return deck

def change_to_letters(deck, n):
     key_to_letters = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"}
     for key, value in key_to_letters.items():
         if __name__ == "__main__":
             if deck[n - 1][0] == 27: 
                 print("Joker dont have a letter")
                 break
             elif deck[n - 1][0] == key:
                     print(value)
         elif deck[n][0] == key:
             return value

def find_card_place(deck, n):
    deck_dict = deck_dict = {"Ace of spades": (1, 1), "2 of spades": (2, 1), "3 of spades": (3, 1), "4 of spades": (4, 1), "5 of spades": (5, 1), "6 of spades": (6, 1), "7 of spades": (7, 1), "8 of spades": (8, 1), "9 of spades": (9, 1), "10 of spades": (10, 1), "Knight of spades": (11, 1), "Queen of spades": (12, 1), "King of spades": (13, 1), "Ace of hearts": (14, 2), "2 of hearts": (15, 2), "3 of hearts": (16, 2), "4 of hearts": (17, 2), "5 of hearts": (18, 2), "6 of hearts": (19, 2), "7 of hearts": (20, 2), "8 of hearts": (21, 2), "9 of hearts": (22, 2), "10 of hearts": (23, 2), "Knight of hearts": (24, 2), "Queen of hearts": (25, 2), "King of hearts": (26, 2), "Joker of spades": (27, 1), "Joker of hearts": (27, 2)}
    for key, value in deck_dict.items():
        if n == key:
            for cards in deck:
                if cards == value:
                    card_place = deck.index(cards)
                    return card_place

def size_of_deck(deck):
    return len(deck)

def get_value(deck, n):
    if __name__ == "__main__":
        print(deck[n - 1][0])
    else:
        return deck[n][0]

    def create_board():
    board = {}
    return board

board = create_board()

def add_wall(board, y, x):
    board[(y, x)] = '#'
    return board

def add_box(board, y, x):
    board[(y, x)] = 'o'
    return board

def add_player(board, y, x):
    board[(y, x)] = '@'
    return board

def check_coordinate(board, y, x):
    if (y, x) not in board.keys():
        return False
    else:
        return board[(y, x)]


def sokoban_load(n):
    level = []
    with open(n) as file:
        for lines in file:
            level.append(list(lines))
    for index, elements in enumerate(level):
        if '#' in elements:
            for value, items in enumerate(elements):
                if items == '#':
                    board[(index, value)] = '#'
    for index, elements in enumerate(level):
        if '@' in elements:
            for value, items in enumerate(elements):
                if items == '@':
                    board[(index, value)] = '@'
    for index, elements in enumerate(level):
        if 'o' in elements:
            for value, items in enumerate(elements):
                if items == 'o':
                    board[(index, value)] = 'o'
    for index, elements in enumerate(level):
        if '.' in elements:
            for value, items in enumerate(elements):
                if items == '.':
                    board[(index, value)] = '.'
                    
    return board
                    
sokoban_load('/home/jakno825/Downloads/first_level.sokoban')

def get_keys(board, n):
    list_of_keys = []
    for key, value in board.items():
        if value == n:
            list_of_keys.append(key)
    return list_of_keys

storage_key = get_keys(board, '.')


def display_board(board):
    highest_y = max(board.keys())[0]
    highest_x = max([coordinate[1] for coordinate in board.keys()])
    for y in range(highest_y+1):
        for x in range(highest_x+1):
            value = check_coordinate(board, y, x)
            if value:
                print(value, end="")
            else:
                print(" ", end="")
        print()

def player_location(board):
   for key, value in board.items():
       if value == '@':
           return key
       elif value == '+':
           return key

def change_value_back(board, player):
    for keys in storage_key:
        if player in keys:  
            print(f"{storage_key} där")
        if player != keys:
            print(f"{keys} här")
            board.update({keys: '.'})
            return board
            

def change_value(board, player, n, storage_key):
    if n == 'd':
        print(storage_key)
        print(player)
        next_move = (player[0], player[1]+1)
        for keys in storage_key:
            if next_move == keys:
                board.update({player: '+'})
        for keys in storage_key:
            if player != keys:
                
                    print("hej")
            #if player != storage_key:
                #print("då")
                
    print(storage_key)
                #return board
               
       #if next_move = 
        #if player == 
        #if player_value == 
        #player_value = check_coordinate(board, player[0], player[1])
        #if player_value == '@':
        #    print(player_value) 
        #    storage = (player[0], player[1]+1)

        #    return board
        #elif player_value == False:
        #    print("hej")
        #    storage = (player[0], player[1]+1)
        #    board.update({storage: '+'})
        #    change_value_back(board, player, 'd')
            #player_key = (player[0], player[1]-1) 
            #board.update({player_key: '.'})
        #    return board

        #after_storage = (player[0], player[1]-1)
        #print(after_storage)
        #if storage:
        #    last_storage = (player[0], player[1]-1)
        #    print("hej")
        #    print(player)
        
       
        
        

def player_can_move(board, n):
    if n == 'w':
        player = player_location(board)
        spot = check_coordinate(board, player[0]-1, player[1])
        if spot == False:
            return False
        elif spot == 'o':
            return 'o'
    elif n == 'a':
        player = player_location(board)
        spot = check_coordinate(board, player[0], player[1]-1)
        if spot == False:
            return False
        elif spot == 'o':
            return 'o'
    elif n == 'd':
        player = player_location(board)
        next_spot = check_coordinate(board, player[0], player[1]+1)
        if next_spot == False:
            return False
        elif next_spot == 'o':
            return 'o'
        elif next_spot == '.':
            return '.'
        elif next_spot == '*':
            return '*'
    elif n == 's':
        player = player_location(board)
        next_spot = check_coordinate(board, player[0]+1, player[1])
        if next_spot == False:
            return False
        elif next_spot == 'o':
            return 'o'

def crate_can_move(board, n):
    if n == 'w':
        player = player_location(board)
        next_spot = check_coordinate(board, player[0]-2, player[1])
        if next_spot == False:
            return False
        elif next_spot == '#':
            return 'Wall'
    elif n == 'a':
        player = player_location(board)
        next_spot = check_coordinate(board, player[0], player[1]-2)
        if next_spot == False:
            return False
        elif next_spot == '#':
            return 'Wall'
    elif n == 'd':
        player = player_location(board)
        next_spot = check_coordinate(board, player[0], player[1]+2)
        if next_spot == False:
            return False
        elif next_spot == '#':
            return 'Wall'
    elif n == 's':
        player = player_location(board)
        next_spot = check_coordinate(board, player[0]+2, player[1])
        if next_spot == False:
            return False
        elif next_spot == '#':
            return 'Wall'


def move_player(board):
    while True:
        display_board(board)
        nav = input()
        player = player_location(board)
        if nav == "w":
            spot = player_can_move(board, 'w')
            if spot == False:
                moved_player = (player[0]-1, player[1])
                board[moved_player] = board.pop(player)
                display_board(board)
            elif spot == "o":
                box_spot = move_box(board, player, 'w')
                if box_spot == None:
                    continue
                else:
                    moved_player = (player[0]-1, player[1])
                    board[moved_player] = board.pop(player)
                    display_board(board)
        elif nav == "a":
            spot = player_can_move(board, 'a')
            if spot == False:
                moved_player = (player[0], player[1]-1)
                board[moved_player] = board.pop(player)
                display_board(board)
            elif spot == "o":
                box_spot = move_box(board, player, 'a')
                if box_spot == None:
                    continue
                else:
                    moved_player = (player[0], player[1]-1)
                    board[moved_player] = board.pop(player)
                    display_board(board)
        elif nav == "d":
            #print(storage_key)
            spot = player_can_move(board, 'd')
            if spot == False:
                moved_player = (player[0], player[1]+1)
                board[moved_player] = board.pop(player)
                display_board(board)
            elif spot == "o":
                box_spot = move_box(board, player, 'd')
                if box_spot == None:
                    continue
                else:
                    moved_player = (player[0], player[1]+1)
                    board[moved_player] = board.pop(player)
                    display_board(board)
            elif spot == ".":
                player1 = player_location(board)
                moved_player = (player[0], player[1]+1)
                print(f"{player1} här")
                
                #board.pop(moved_player)
                
                #print(player)
                #display_board(board)
                if player1 == '+':
                    board.pop(player, '+')
                    board.update({player: '.'})
                    board.update({moved_player: '+'})
                #change_value(board, player, 'd', storage_key)
                #board[moved_player] = board.pop(player)
                #change_value_back(board, storage_key)
                else:
                    board.pop(player, '@')
                    board.update({moved_player: '+'})
                
                #print(check_coordinate(board, player[0], player[1]))
                display_board(board)
            elif spot == "*":
                box_spot = move_box(board, player, 'd')
                if box_spot == None:
                    continue
                else:
                    moved_player = (player[0], player[1]+1)
                    board[moved_player] = board.pop(player)
                    display_board(board)
        elif nav == "s":
            spot = player_can_move(board, 's')
            if spot == False:
                moved_player = (player[0]+1, player[1])
                board[moved_player] = board.pop(player)
                display_board(board)
            elif spot == "o":
                box_spot = move_box(board, player, 's')
                if box_spot == None:
                    continue
                else:
                    moved_player = (player[0]+1, player[1])
                    board[moved_player] = board.pop(player)
                    display_board(board)

def move_box(board, player, n):
    if n == "w":
        next_spot = crate_can_move(board, 'w')
        if next_spot == False:
            box = (player[0]-1, player[1])
            moved_box = (box[0]-1, box[1])
            board[moved_box] = board.pop(box)
            return board
        else:
            return None
    elif n == "a":
        next_spot = crate_can_move(board, 'a')
        if next_spot == False:
            box = (player[0], player[1]-1)
            moved_box = (box[0], box[1]-1)
            board[moved_box] = board.pop(box)
            return board
        else:
            return None
    elif n == "d":
        next_spot = crate_can_move(board, 'd')
        if next_spot == False:
            box = (player[0], player[1]+1)
            moved_box = (box[0], box[1]+1)
            board[moved_box] = board.pop(box)
            return board
        else:
            return None
    elif n == "s":
        next_spot = crate_can_move(board, 's')
        if next_spot == False:
            box = (player[0]+1, player[1])
            moved_box = (box[0]+1, box[1])
            board[moved_box] = board.pop(box)
            return board
        else:
            return None
move_player(board)

