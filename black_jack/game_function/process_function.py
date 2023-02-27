RULES = ("Hey, cowboy! Welcome to the hottest bar in the entire wild west."
        "\nThis is your chance to play Black Jack with America's most notorious crooks and outlaws!"
        "\nThe stakes are high, but the winnings will make you very happy. Do not miss the chance and be a sweetheart."
        "\nHere's all you need to know: there's only one deck of 36 cards." 
        "\nThe dealer will put himself 2 cards and give you 2. Your job is to score more points than this cheater."
        "\nTake more cards or stop at your own discretion, but remember and be careful, "
        "because if you outscore 21 points -\nweep for your wife's new shoes, someone at the bar will "
        "surely blow a hole in you.\nTry to give it your all and good luck "
        "(if you get 100 000 - you'll get a pleasant surprise")


def check_correct_bet(bet, balance):
    if bet == 'quit':
        return False 
    try:
        if int(bet) > 0 and int(bet) <= balance:
            return True
        elif int(bet) < 1:
            return None
        elif int(bet) > balance:
            return 'Sorry, but it is too much for you'
    except:
        return f'Incorrect answer, please choose 1-{balance}, or quit'


def determining_bet(bet, balance):
    if bet == 'more':
        bet = input(
                    f'Nice to meet you. Your balance is still {balance} coins.'
                    '\nHow much do you bet? (1-{balance}, or quit)\n:')
    while check_correct_bet(bet, balance) != True and check_correct_bet(bet,balance) != False:
        if check_correct_bet(bet, balance) == None:
            print('Hey! We are serious gamers! Get the f@ck out of here!')
            return 'Small bet'
        print(check_correct_bet(bet, balance))
        bet = input(f'How much do you bet? (1-{balance}, or quit)\n:')
    if check_correct_bet(bet, balance) == False:
        return 'quit'
    print('Your bet is ' + bet)
    bet = int(bet)
    return bet


def determine_winner(curent_player_value, curent_diller_value, balance, bet):
    if curent_player_value > 21:
        print("Oh no, it's to much.")
        balance -= int(bet)
        return balance
    elif curent_player_value > curent_diller_value:
        balance += int(bet)
        print(f'Congratulations, you are lucky son of a beach\nYour current balance is {balance}')
        return balance
    elif curent_diller_value == curent_player_value:
        print('He-he, it is not the worst option. You are always able to try again')
        print(f'\nYour balance now is {balance} coins')
        return balance
    else:
        balance -= int(bet)
        print("Sheet hapens, you're better try next time.")
        print(f'\nYour balance now is {balance} coins')
        return balance


def answer_to_play_again(balance): 
    choise = input('Your decision: (more, leave)\n:')
    while choise != 'leave' and choise != 'more':
        print("This is incorrect answer, don't try to crash my game.")
        choise = input('Your decision: (more, leave)\n:')
    if choise == 'leave':
        print('Better luck next time!\nGoodbye!')
        return 'quit', 'quit'
    elif choise == 'more':
        bet = input(f'Your balance is {balance} coins now.\nHow much do you bet? (1-{balance}, or quit)\n:')
        return 'more', bet
