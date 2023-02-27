from black_jack.game_function import make_cards
from black_jack.game_function import process_function


def run_game():
    print(process_function.RULES)
    choise = 'more'
    balance = 5000
    bet = 'more'
    bet = process_function.determining_bet(bet, balance)
    if bet == 'Small bet':
        return
    if bet == 'quit':
        return print('See you maybee next time!\nGoodbye!')
    while int(balance) > 0 and choise != 'quit' and bet != 'quit':
        numbers = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        cards_value = (6, 7, 8, 9, 10, 10, 10, 10, 11)
        if bet == 'quit':
            break
        dil_num1, dil_simb1, dil_num2, dil_simb2 = make_cards.make_dill_cards()
        curent_diller_value = (int(cards_value[numbers.index(dil_num1)])
                               + int(cards_value[numbers.index(dil_num2)]))
        print('Diller: ???')
        make_cards.print_deal_secret_cards(dil_num1, dil_simb1)
        pl_num1, pl_simb1, pl_num2, pl_simb2 = make_cards.make_player_cards()
        curent_player_value = (int(cards_value[numbers.index(pl_num1)])
                               + int(cards_value[numbers.index(pl_num2)]))
        print('Player: ' + str(curent_player_value))
        make_cards.print_player_cards(pl_num1, pl_simb1, pl_num2, pl_simb2)
        choise = input('Your decision: (more, stop, leave)\n:')
        if choise == 'more':
            pl_num3, pl_simb3 = make_cards.make_player_third_card()
            curent_player_value = (int(cards_value[numbers.index(pl_num1)])
                                   + int(cards_value[numbers.index(pl_num2)])
                                   + int(cards_value[numbers.index(pl_num3)]))
            print('Player: ' + str(curent_player_value))
            print(f' ___   ___   ___\n|{str(pl_num1)}'
                  f'  | |{str(pl_num2)}  | |{str(pl_num3)}  |\n| {pl_simb1}'
                  f' | | {pl_simb2} | | {pl_simb3} |\n|  {str(pl_num1)}'
                  f'| |  {str(pl_num2)}| |  {str(pl_num3)}|')
            choise = input('Your decision: (stop, leave)\n:')
        if choise == 'stop':
            print('Diller: ' + str(curent_diller_value))
            make_cards.print_dil_cards(dil_num1, dil_simb1, dil_num2, dil_simb2)
            balance = process_function.determine_winner(curent_player_value,
                                                        curent_diller_value,
                                                        balance, bet)
            if balance < 1:
                print("You've lost all the money.")
                print('Better luck next time!\nThank you and goodbye!')
                break
            choise, bet = process_function.answer_to_play_again(balance)
        if choise.lower() == 'leave':
            print('Better luck next time!\nThank you and goodbye!')
            break
