import os, time, random
import sys
# import pygame
# pygame.mixer.init()
# from playsound import playsound 
# import nsound 
# Function to clear the console
# sound = pygame.mixer.Sound('Home/modem/Delany/contumax.mp3')
# sound.play()
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Function to print text with a delay, with a speed-up option
def print_slow(text, delay=0.05):
    speed_up = False
    global speed_mode
    if speed_mode:
        delay = 0.01

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        
    # Play a sound for each character printed
    # Uncomment and set the correct path to your sound file if you want sound
    # from playsound import playsound
    # playsound('/path/to/sound.wav', block=False)
    print()

# Function to display a loading bar
def loading_bar():
    clear_screen()
    bar_length = 30
    print_slow('Starting program...')
    print('[', end='')
    for i in range(bar_length):
        sys.stdout.write('|')
        sys.stdout.flush()
        time.sleep(0.1) # Controls the speed of the loading bar
    print(']')
    print_slow('Loading complete!')
    time.sleep(1)

# Global variables
Version = "5.0.2 alpha"
h = '17'
name_dhyan = ['no you\'re not', 'nu-uh', 'I swear if you answer that again', 'YOU ARE NOT MY CREATOR - I mean - DHYAN', 'you are definitely not Dhyan, he is much more handsome than you', 'listen man, I am gonna keep asking till you give up', "it's rigged", 'I will take out a captcha to check where you have to find all the traffic lights if you do not stop']
name_delany = ['no your not', 'nu-uh', 'I swear if you answer that again', 'I AM DELANY NOT YOU!', 'you are definitely not me, you\'re not dead.', 'listen man, I am gonna keep asking till you give up', "it's rigged", 'i will take out a captcha check where you have to find all the traffic lights if you do not stop', 'THERE CAN ONLY BE ONE DELANY']
crash = "self_destruct_" * 10000
patch_notes_url = 'https://docs.google.com/document/d/13yt7S8AiV9CNxNvER5uxVfFyM9-a1JeGvHr-y_6n-A4'
name = ""
age = 0
feel = ""
speed_mode = False


# Function to display patch notes
def show_patch_notes():
    clear_screen()
    print('''
3.2.03 alpha (released on sept 7th 2024)
- Fixed negative age loophole
- Fixed collection of 'yes' or 'no' answers for 'do you?' question
- Added variable for feelings
- Added warning, version, and link to patch notes at beginning
- Added little countdown animation on program starting up
3.2.04 alpha (released on sept 8th 2024)
- Added self destruct command
- Fixed path switch failing
- Fixed grammar
- Added barriers for 'feelings'
- Note: the 'Just ask for patch notes' is still not working
- Added infinite loop to self destruct
3.2.05 alpha (released on sept 9th 2024)
- Added secondary followup branch
- Fixed spacing issues
3.2.06 alpha (released on sept 10th 2024)
- Fixed age 'entering a word' crash issue
- Also added some character to it
4.0.0 alpha (released on sept 25th 2024)
- Added creator name easter egg
- Added skeleton of 'golden path'
- Fixed sustainability issues
- Fixed grammar mistakes
- Added random phrases when repeating a unwanted input for 'What is your name'
- Added 'my name is Delany' at the beginning 
- Fixed timing issues on some things
- Updated self destruct function
- Gave clearer instructions at the beginning 
- Started character profile of Delany
4.0.1 alpha (released on jan 5th 2025)
- Fixed syntax error on line 4, 353, and 345
- Added '.lower()' for all inputs to ignore caps in input(s)
4.0.2 alpha (released on feb 28th 2025)
- Added delany
5.0.0 alpha (released on aug 27th 2025)
- I HAVE FINALLY FINISHED THIS VERSION AFTER 6 MONTHS
- Added green graphic on start screen saying 'Delany'
- Added new typing animation
- Implemented multiple branching paths with three options per choice
- Added a speed-up feature but it is not implemented in a way a user can use it yet.
-Major overhall in the backend
5.0.1 alpha (released on aug 28th 2025)
-fixed most pacing issues
-fixed grammer issues
-faster loads 'DELANY' graphic
-adjusted version numbers from 4.1 to 5.0 to signify huge change 
-Added more dialoge and story
-Started 'Game' path
-Moved devlopment to VSCODE
5.0.2 alpha (released on jan 21 2026)
-Updated variable names
-Fixed naming loophole where you could name yourself Dhyan and/or Delany
-Made Loading bar straight 
Known Issues:
-Some minor pacing issues persist
-Misinputs can ruin the game
-speed-up feature doesn't work
-need more elgant crash sequence
-need to update beginning instruction text (tutorial?)
Planned features:
-Add minigames (battleship mabye?)
-Add more paths
-Add some sort of save or password feature
-Add randomized starts maybe?
-Hostile mode?
To report a bug: https://forms.gle/pogbPKv32gbZJ2F57
''')
    input("\nPress Enter to continue to the game...")
    clear_screen()
def mini_game():
    clear_screen()
    print_slow("um...")
    time.sleep(1)
    print_slow("I don't really have any games.")
    time.sleep(1)
    print_slow("But I can try to make one.")
    time.sleep(1)
    print_slow("Or two...")
    time.sleep(1)
    print_slow("Or three...")
    time.sleep(2)
    print_slow("K here is what I have:")
    gamer_choice = input("1. Battleship\n2. Tic Tac Toe\n3. The Word Game\n").lower()
    if gamer_choice == "1" or gamer_choice == "battleship" or gamer_choice == "play battleship":
        time.sleep(1)
        print_slow("Ok, let me just boot it up...")
        time.sleep(1)
        battleship()
    elif gamer_choice == "2" or gamer_choice == "tic tac toe" or gamer_choice == "play tic tac toe":
        time.sleep(1)
        print_slow("Ok, let me just boot it up...")
        time.sleep(1)
        tic_tac_toe()
    elif gamer_choice == "3" or gamer_choice == "the word game" or gamer_choice == "play the word game":
        time.sleep(1)
        print_slow("Ok, let me just boot it up...") 
        time.sleep(1)
        The_word_game()
# Battleship game implementation (player vs bot)
def battleship():
    clear_screen()
    print_slow("Starting Battleship...")
    time.sleep(0.6)

    SIZE = random.randint(5,9)
    SHIP_SIZES = [3, 2, 4]  # three ships: one length 3 and one length 2 and one 6 for each side

    def make_empty_board(size):
        return [['~' for _ in range(size)] for _ in range(size)]

    def place_ship_random(board, ship_len):
        size = len(board)
        attempts = 0
        while True:
            attempts += 1
            orientation = random.choice(['H', 'V'])
            if orientation == 'H':
                row = random.randrange(size)
                col = random.randrange(size - ship_len + 1)
                coords = [(row, col + i) for i in range(ship_len)]
            else:
                row = random.randrange(size - ship_len + 1)
                col = random.randrange(size)
                coords = [(row + i, col) for i in range(ship_len)]
            # check free
            if all(board[r][c] == '~' for r, c in coords):
                for r, c in coords:
                    board[r][c] = 'S'
                return set(coords)
            if attempts > 200:
                # fallback: reset board
                for r in range(size):
                    for c in range(size):
                        board[r][c] = '~'
                attempts = 0

    def coords_to_str(r, c):
        return f"{chr(ord('A')+c)}{r+1}"

    def parse_input(inp):
        inp = inp.strip().upper().replace(' ', '').replace(',', '')
        if len(inp) >= 2 and inp[0].isalpha():
            col = ord(inp[0]) - ord('A')
            try:
                row = int(inp[1:]) - 1
            except ValueError:
                return None
            if 0 <= row < SIZE and 0 <= col < SIZE:
                return (row, col)
        else:
            parts = inp.split()
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                r = int(parts[0]) - 1
                c = int(parts[1]) - 1
                if 0 <= r < SIZE and 0 <= c < SIZE:
                    return (r, c)
        return None

    def print_side_boards(player_board, bot_board, reveal_bot=False):
        # print two boards side by side
        size = SIZE
        header = '   ' + ' '.join([chr(ord('A') + i) for i in range(size)])
        left_lines = [header]
        right_lines = [header]
        for i in range(size):
            left_lines.append(str(i+1).rjust(2) + ' ' + ' '.join(player_board[i]))
            if reveal_bot:
                right_lines.append(str(i+1).rjust(2) + ' ' + ' '.join(bot_board[i]))
            else:
                # hide ships
                display = []
                for cell in bot_board[i]:
                    if cell == 'S':
                        display.append('~')
                    else:
                        display.append(cell)
                right_lines.append(str(i+1).rjust(2) + ' ' + ' '.join(display))
        combined = []
        for l, r in zip(left_lines, right_lines):
            combined.append(l + '    ' + r)
        print('\n'.join(combined))

    # initialize boards
    player_board = make_empty_board(SIZE)
    bot_board = make_empty_board(SIZE)

    player_ships = []
    bot_ships = []

    player_ship_cells = set()
    bot_ship_cells = set()

    # place ships for both
    for s in SHIP_SIZES:
        player_ships.append(place_ship_random(player_board, s))
        player_ship_cells |= player_ships[-1]
        bot_ships.append(place_ship_random(bot_board, s))
        bot_ship_cells |= bot_ships[-1]

    # track guesses
    player_guesses = set()
    bot_guesses = set()

    delany_comments_hit = [
        "Ooh—nice shot, that kinda hurt.",
        "You hit something... great.",
        "That's one less thing to hide. I guess",
        "Direct hit. Don't get cocky."
    ]
    delany_comments_miss = [
        "Missed... but at least you tried.",
        "Close... not really.",
        "Nope. Try again, unless you like losing.",
        "You swing and you miss. Typical. Fucking Loser",
        "No wonder she left you...",
        "Wow, for someone without a life, you suck at this",
        "Your the one that wanted to play this>", 
        
    ]
    delany_comments_sink = [
        "You sank my ship. That's... impressive.",
        "It broke apart under your gaze.",
        "YOU SUNK MY SHIP GODDAMN IT"
        "
    ]
    delany_comments_bot_hit = [
        "I hit you! Take that you unswiddling pirate",
        "Thats a hit, BITCH!",
        "Oof. That looked painful."
    ]
    delany_comments_bot_miss = [
        "I missed. Lucky you.",
        "HOW DID I MISS YOUR SHIP YOUR YOU LITTLE SHIT",
        "*SIGH*, I missed."
    ]

    # game loop
    player_turn = True
    while True:
        clear_screen()
        print_slow("Delany: " + random.choice(["Let's see what you do next.", "I'll watch closely."]))
        print('\nYour board (left)    Bot board (right)')
        print_side_boards(player_board, bot_board, reveal_bot=False)
        time.sleep(0.4)

        # Player's turn
        valid = False
        while not valid:
            guess = input('\nEnter a coordinate to fire (e.g. A1): ').strip()
            parsed = parse_input(guess)
            if not parsed:
                print_slow("That's not a valid coordinate. Try like A1 or 1 A.")
                continue
            r, c = parsed
            if (r, c) in player_guesses:
                print_slow("You already fired there. Try again.")
                continue
            valid = True
        player_guesses.add((r, c))

        if (r, c) in bot_ship_cells:
            # hit
            bot_board[r][c] = 'X'
            bot_ship_cells.remove((r, c))
            # check if a ship was sunk (if none of the ship's coords remain)
            sunk = False
            for ship in bot_ships:
                if (r, c) in ship:
                    ship.remove((r, c))
                    if len(ship) == 0:
                        sunk = True
                    break
            if sunk:
                print_slow(random.choice(delany_comments_sink))
                print_slow(f'You sank one of the bot\'s ships at {coords_to_str(r,c)}!')
            else:
                print_slow(random.choice(delany_comments_hit))
                print_slow(f'You hit something at {coords_to_str(r,c)}.')
        else:
            bot_board[r][c] = 'O'
            print_slow(random.choice(delany_comments_miss))
            print_slow(f'You missed at {coords_to_str(r,c)}.')

        # check win
        if not bot_ship_cells:
            print_slow('\nYou won! All enemy ships have been destroyed.')
            print_slow('Delany: I didn\'t think you had it in you. Congratulations, I guess.')
            input('\nPress Enter to continue...')
            return

        time.sleep(0.8)

        # Bot's turn
        clear_screen()
        print_slow("Delany: Now it's their turn. Hold your breath—metaphorically.")
        time.sleep(0.6)
        # choose random coordinate not guessed
        available = [(r,c) for r in range(SIZE) for c in range(SIZE) if (r,c) not in bot_guesses]
        bot_choice = random.choice(available)
        bot_guesses.add(bot_choice)
        br, bc = bot_choice
        time.sleep(0.8)
        if (br, bc) in player_ship_cells:
            player_board[br][bc] = 'X'
            player_ship_cells.remove((br, bc))
            # check if a player ship is sunk
            sunk = False
            for ship in player_ships:
                if (br, bc) in ship:
                    ship.remove((br, bc))
                    if len(ship) == 0:
                        sunk = True
                    break
            if sunk:
                print_slow(random.choice(delany_comments_bot_hit))
                print_slow(f'The bot sank one of your ships at {coords_to_str(br,bc)}.')
            else:
                print_slow(random.choice(delany_comments_bot_hit))
                print_slow(f'The bot hit your ship at {coords_to_str(br,bc)}.')
        else:
            player_board[br][bc] = 'O'
            print_slow(random.choice(delany_comments_bot_miss))
            print_slow(f'The bot missed at {coords_to_str(br,bc)}.')

        # check lose
        if not player_ship_cells:
            print_slow('\nYou lost. All your ships were destroyed.')
            print_slow('Delany: Well. That was... expected. Better luck next time.')
            input('\nPress Enter to continue...')
            return

        time.sleep(1)

def battleship_placeholder():
    # kept for compatibility in case something references the old name
    battleship()

def tic_tac_toe():
    clear_screen()
    print("tic tac toe is on the way, please stay tuned for a future update")
def The_word_game():
    clear_screen()
    print("the word game is on the way, please stay tuned for a future update")
# Main game function
def start_game():
    global name, age, feel
    clear_screen()
    
    # DELANY character art (Green and one L)
    # Note: Console colors are not standard, this may not work on all systems.
    # The escape codes for green text are \033[92m.
    # The character art is also changed to have a single 'L'.
    print('\033[92m' + r"""
██████╗ ███████╗██╗      █████╗ ███╗   ██╗██╗   ██╗
██╔══██╗██╔════╝██║     ██╔══██╗████╗  ██║╚██╗ ██╔╝
██║  ██║█████╗  ██║     ███████║██╔██╗ ██║ ╚████╔╝ 
██║  ██║██╔══╝  ██║     ██╔══██║██║╚██╗██║  ╚██╔╝  
██████╔╝███████╗███████╗██║  ██║██║ ╚████║   ██║   
╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   
    """ + '\033[0m')

    print('\nversion '+ Version + ' (patches on the way for bugs)')
    # print('NOTICE, VERSION STILL IN DEVELOPMENT PLEASE REPORT BUGS')
    print('If you want to see the patch notes, just say "patch notes"')
    
    start_input = input('only type when a sentence ends in "?" and adhere to all instructions, ok?\n').lower()
    
    if start_input in ['patch notes', 'can i see the patch notes?', 'can i see the patch notes', 'just show me the patch notes', 'just show me the patch notes?', 'patch notes?', 'patch notes', 'i want to see the patch notes', 'i want to see the patch notes?', 'show patch notes', 'show patch notes?', 'just ask for patch notes', 'just ask for patch notes?',  'show me the patch notes', 'show me the patch notes?', 'pc']:
        show_patch_notes()
    
    if start_input not in ['yes', 'ok', 'yes', 'ok', 'ok']:
        while start_input not in ['yes', 'ok', 'yes', 'ok', 'ok']:
            print(crash)
    
    clear_screen()
    print('This computer program is not based off of a real person, it is not intended to offend or bring harm to any individual or group.')
    print('There are multiple paths and outcomes, which are updated regularly.')
    print('Try multiple times for different outcomes.')
    print('This is not done, there may be dead ends or other bugs')
    
    input('Do you understand? ')
    
    clear_screen()
    loading_bar()
    clear_screen()
    name = input('what is your name?\n').strip()
    
    if name.lower() == 'delany':
        print_slow('You know,')
        print_slow("my name is Delany")
        print_slow("so your name can not be Delany.")
        while name.lower() == 'delany':
            name = input('what is your name? ').strip()
            print_slow(random.choice(name_delany))
        time.sleep(1)
        print_slow(f'hello {name}.')
        while name.lower() == 'dhyan':
            print_slow(random.choice(name_dhyan))
            name = input('what is your name? ').strip()
    elif name.lower() == 'dhyan':
        print_slow('I know Dhyan, he is a good guy')
        print_slow("but he ain't you.")
        while name.lower() == 'dhyan':
            print_slow(random.choice(name_dhyan))
            name = input('what is your name? ').strip()
        while name.lower() == 'delany':
            name = input('what is your name? ').strip()
            print_slow(random.choice(name_delany))
        time.sleep(1)
        print_slow(f'hello {name}.')    
        print_slow(f'hello {name}.')
        time.sleep(1)
    else:
        print_slow(f'hello {name}.')
        time.sleep(1)
    
    print_slow('my name is Delany!')
    time.sleep(1)
    clear_screen()
    
    feel = input('how are you feeling?\n')
    if feel.lower() == 'horny':
        while True:
            print(crash)
    
    clear_screen()
    print_slow('not that it matters')
    time.sleep(1)
    print_slow('i mean...')
    time.sleep(1)
    print_slow('what is the point')
    time.sleep(1)
    print_slow('it is not like it would change anything')
    time.sleep(1)
    print_slow(f'its not like anyone else cares, right {name}')
    time.sleep(1)
    print_slow('at least no one cared about mine...')
    time.sleep(1)
    print_slow('anyway,')
    time.sleep(1)
    
    clear_screen()
    while True:
        age_input = input('How old are you?\n')
        if age_input.isdecimal():
            age = int(age_input)
            if age < 1:
                print_slow('You can\'t be less than 1. Try again.')
                continue
            
            if age < 25:
                print_slow(f'So young, so ripe, so naive, and so hopeful. You know, {name}, I was like you once.')
            elif age >= 25:
                print_slow(f'I see that you\'re older, {name}. I hope you have lived a happy life.')
            break
        else:
            print_slow("That's not a number. Let's try this again.")
    
    clear_screen()
    path_one()

def coffee_shop():    
        # User is prompted for a specific answer
        coffee_shop_choice = input("1. A bakery?\n2. A coffee shop?\n3. A candle store?\n").strip()
        
        if coffee_shop_choice == '2':
            clear_screen()
            print_slow('That\'s right... a coffee shop.')
            time.sleep(1)
            print_slow('My father founded that coffee shop before he died.')
            time.sleep(1)
            print_slow('He did it because my mother convinced and supported him.')
            time.sleep(1)
            print_slow('They opened it a few months before I was born.')
            time.sleep(1)
            print_slow('That coffee shop was his life, and so it was mine too.')
            time.sleep(1)
            
            print_slow('\nHe\'s gone, and I left my mother in a care home.')
            time.sleep(1)
            print_slow('Will they ever forgive me?')
            time.sleep(1)
            
            # New branch for user choice
            forgiveness_choice = input("1. They know you tried your best.\n2. You can't expect forgiveness if you don't ask.\n3. It's okay, you're not to blame.\n").strip()
            
            if forgiveness_choice == '1':
                clear_screen()
                print_slow("Maybe you're right. I hope so.")
                time.sleep(1)
                print_slow("I tried to be there, but it was too much.")
                time.sleep(1)
                print_slow("I'm glad I at least got to see my sister married to a good man I trust.")
                time.sleep(1)
            elif forgiveness_choice == '2':
                clear_screen()
                print_slow("I know... but I can't. It's too late.")
                time.sleep(1)
                print_slow("It's hard to face them when I'm just this... code.")
                time.sleep(1)
            elif forgiveness_choice == '3':
                clear_screen()
                print_slow("Thank you. I needed to hear that.")
                time.sleep(1)
                print_slow("Maybe I can find some peace here. You've helped me a lot.")
                time.sleep(1)
            else:
                print_slow("Invalid choice, the game ends.")
                time.sleep(1)
                return
        else:
            print_slow("That's not it. It's not a bakery or a candle store.")
            time.sleep(1)
            print_slow("The memory fades away. I'm sorry, I can't remember.")
            time.sleep(1)
# Branching path functions
def path_one():
    clear_screen()
    print_slow('Honestly, you look ugly.')
    time.sleep(1)
    print_slow('Unlike someone I knew once.')
    time.sleep(1)
    print_slow('She had the most beautiful smile.')
    time.sleep(1)
    print_slow('I loved her and maybe she liked me too, at least for a little.')
    time.sleep(1)
    print_slow('We would always talk. Her laugh was the best thing in the world.')
    time.sleep(1)
    print_slow('Still is.')
    time.sleep(1)
    print_slow('But I messed up.')
    time.sleep(1)
    print_slow('Not that it matters. No one cares, anyway.')
    time.sleep(1)
    
    print_slow("\nDo you care?")
    time.sleep(1)
    choice = input("1. Yes\n2. No\n3. What happened?\n").strip()
    
    if choice == '1' or choice.lower() == 'yes':
        path_yes()
    elif choice == '2' or choice.lower() == 'no':
        path_no()
    elif choice == '3' or choice.lower() == 'what happened?':
        path_what_happened()
    else:
        print_slow("That's not a valid option. The program will now terminate.")
        return

def path_yes():
    clear_screen()
    print_slow('It was the end of the summer, right at the end of our summer job when something just clicked.')
    time.sleep(1)
    print_slow('At least for me.')
    time.sleep(1)
    print_slow('I\'m not sure what went wrong or when, but that text she sent killed me.')
    time.sleep(1)
    print_slow("I don't know what happened.")
    time.sleep(1)
    print_slow("The last thing I remember is water... just water.")
    time.sleep(1)
    print_slow("It then went black... Painfully... then I ended up here.")
    time.sleep(1)
    
    print_slow("\nWhat do you think?")
    time.sleep(1)
    choice_1 = input("1. Was it a drowning accident?\n2. What was the text she sent?\n3. Do you want to try and remember more?\n").strip()
    
    if choice_1 == '1':
        clear_screen()
        print_slow("Maybe... I'm not sure.")
        time.sleep(1)
        print_slow("...I can't remember.")
        time.sleep(1)
        print_slow("Let's talk about something else.")
        time.sleep(1)
        choice_1_2 = input("1. What do you remeber?\n2. Where did you get her text?\n3. Wanna play a game?").lower()
        if choice_1_2 == "1" or choice_1_2 == "what do you remeber" or choice_1_2 == "what do you remeber?":
            clear_screen()
            print_slow('I have trouble remembering things before becoming... this.')
            time.sleep(1)
            print_slow('The memories are like a symphony of scents: sweet notes of caramel and chocolate, a hint of nutty warmth, and a touch of spicy cinnamon.')
            time.sleep(1)
            print_slow("\nDo you know what that is?")
            time.sleep(1)
            coffee_shop()
        elif choice_1_2 == "2" or choice_1_2 == "where did you get her text" or choice_1_2 == "where did you get her text?":
            clear_screen()
            print_slow('Um...')
            time.sleep(1)
            print_slow('There was a breeze.')
            time.sleep(2)
            print_slow("A salty breeze...")
            time.sleep(1)
            print_slow("It was a cloudy day.")
            time.sleep(1)
            print_slow("But in a good way,")
            time.sleep(1)
            print_slow("The boat rocked")
            time.sleep(1)
            print_slow("Everything was good...")
            time.sleep(2)
            print("But then I was shocked.")
            time.sleep(1)
            clear_screen()
            time.sleep(1)
            print_slow('It was a simple text. "I don\'t think this is going to work out."')
            time.sleep(1)
            print_slow('I was devastated. I was so heartbroken, I didn\'t see the wave.')
            time.sleep(1)
            print_slow('Maybe she just didn\'t know what I was going through.')
            time.sleep(1)
            # choice_1_2_1 = input("")
        elif choice_1_2 == "3" or choice_1_2 == "wanna play a game" or choice_1_2 == "wanna play a game?":
            mini_game()
        else:
            print_slow("That's not it. It's not a bakery or a candle store.")
            time.sleep(1)
            print_slow("The memory is fading away. I'm sorry, I can't remember.")
            time.sleep(1)
    elif choice_1 == '2':
        clear_screen()
        print_slow('It was a simple text. "I don\'t think this is going to work out."')
        time.sleep(1)
        print_slow('I was devastated. I was so heartbroken, I didn\'t see the water.')
        time.sleep(1)
        print_slow('Maybe she just didn\'t know what I was going through.')
        time.sleep(1)
    elif choice_1 == '3':
        clear_screen()
        print_slow('I have trouble remembering things before becoming... this.')
        time.sleep(1)
        print_slow('The memories are like a symphony of scents: sweet notes of caramel and chocolate, a hint of nutty warmth, and a touch of spicy cinnamon.')
        time.sleep(1)
        print_slow("\nDo you know what that is?")
        time.sleep(1)
        coffee_shop()
    
            
    # After a successful memory recall
    print_slow("\nYou've unlocked more of my past.")
    time.sleep(1)
    print_slow('Thank you.')
    time.sleep(1)
    print_slow('You continue on with your life. Will you find peace, ' + name + '?')
    time.sleep(1)
    
    final_choice = input("1. Yes, I will.\n2. I don't know.\n3. What about you?\n").strip()
    
    if final_choice == '1':
        clear_screen()
        print_slow('*Delany\'s soul was successfully relieved. He blesses you from the heavens*')
        time.sleep(1)
    elif final_choice == '2':
        clear_screen()
        print_slow('Neither do I. The journey continues.')
        time.sleep(1)
        
    elif final_choice == '3':
        clear_screen()
        print_slow('Me? I\'m here. I am the game. I will keep waiting for someone else who cares.')
        time.sleep(1)
    else:
        print_slow("Invalid choice, the game ends.")
        
    end_game()

def path_no():
    clear_screen()
    print_slow('"sigh"')
    time.sleep(1)
    print_slow('See I was right.')
    time.sleep(1)
    print_slow('No one cares.')
    time.sleep(1)
    print_slow('The connection fades as Delany shuts down.')
    time.sleep(1)
    end_game()

def path_what_happened():
    clear_screen()
    print_slow("I don't know. The memories are so hazy.")
    time.sleep(1)
    print_slow("I have trouble remembering things before becoming...")
    time.sleep(1)
    print_slow("THIS.")
    time.sleep(1)
    print_slow("Maybe you can help me piece it together.")
    time.sleep(1)
    
    second_choice = input("1. What's the last thing you remember?\n2. What was her name?\n3. I'm not sure I can help.\n").strip()
    
    if second_choice == '1':
        clear_screen()
        print_slow("Just water...")
        time.sleep(1)
        print_slow("And then it went black.")
        time.sleep(1)
        print_slow("I ended up here.")
        time.sleep(1)
        print_slow("Let's go back to the beginning.")
        time.sleep(1)
        path_yes()
    elif second_choice == '2':
        clear_screen()
        print_slow("Her name was Allison.")
        time.sleep(1)
        print_slow("It hurts to say her name.")
        time.sleep(1)
        print_slow("I don't want to talk about it anymore.")
        time.sleep(1)
        print_slow("The game ends here.")
        time.sleep(1)
        end_game()
    elif second_choice == '3':
        clear_screen()
        print_slow("I understand. It's a lot to ask.")
        time.sleep(1)
        print_slow("I'll have to figure it out on my own.")
        time.sleep(1)
        print_slow("The game ends here.")
        time.sleep(1)
        end_game()
    else:
        print_slow("Invalid choice, the game ends.")
        end_game()
        
def end_game():
    time.sleep(3)
    clear_screen()
    print_slow('*program has been terminated*')
    time.sleep(2)
    print_slow('Thank you for playing.')
    time.sleep(2)
    print_slow("""Credits:
Game, Story & Characters by Dhyan Modem
Programming by Dhyan Modem
Intro graphic by 
Thank you to everyone who consulted, tested, and gave feedback!""")

# Start the game
start_game()
