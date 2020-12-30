from random_word import pick_a_word
# ------------------------------------------------#

# to display the current state of the word and number of attemps
def print_cur_state(cur_word : str, attempts : int) :
    print('Current word state :', end = ' ')
    for i in cur_word :
        print(i, end = ' ')
    
    print(f"\t Attempts Left : {attempts}")

def change_state(selected_word : str, cur_word : str, input_char : int) -> str:
    modified_state = ''

    for i in range(len(selected_word)) :
        if cur_word[i] == '_' and selected_word[i] == input_char:
            modified_state += input_char
        else :
            modified_state += cur_word[i]

    return modified_state

def check_state(selected_word : str, cur_word : str, input_char : str, attempts : int) :
    if input_char in selected_word :
        cur_word = change_state(selected_word, cur_word, input_char)
    else : 
        attempts -= 1
    
    return cur_word, attempts

def check_game_status(selected_word : str, cur_word : str, attempts : int) -> bool :
    if attempts <= 0 :
        print('Sorry you Lost!!')
        print(f"The word was : {selected_word}")
        return True
    
    if cur_word == selected_word :
        print("Congrats You Won!!")
        return True

    return False

# random word generate, attemps, and user input
def play_game() :
    selected_word = pick_a_word()

    attempts = 5
    cur_word = ""
    for i in selected_word :
        if i in ['a', 'e', 'i', 'o', 'u'] :
            cur_word += i
        else :
            cur_word += '_'

    print_cur_state(cur_word, attempts) # to print the current state

    while True :
        input_char = input("Guess the character : ")
        cur_word, attempts = check_state(selected_word, cur_word, input_char, attempts) # to check whether the input char is present or not
        
        print_cur_state(cur_word, attempts) # to print the current stater

        game_status = check_game_status(selected_word, cur_word, attempts) # to check the current status of the game
        
        if game_status :
            break


#---------------------------------------------------------------------------------#
play_game()
