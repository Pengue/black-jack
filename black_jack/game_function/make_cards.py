import random


numbers = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
simbols = (chr(9829), chr(9830), chr(9824), chr(9827))
cards_value = (6, 7, 8, 9, 10, 10, 10, 10, 11)


def make_dill_cards():
    dil_num1 = random.choice(numbers)
    dil_simb1 = random.choice(simbols)
    dil_num2 = random.choice(numbers)
    dil_simb2 = random.choice(simbols)
    return dil_num1, dil_simb1, dil_num2, dil_simb2


def print_deal_secret_cards(dil_num1, dil_simb1):
    return print(f' ___   ___ \n|## | |{str(dil_num1)}'
                 f'  |\n|###| | {dil_simb1}'
                 f' |\n|_##| |__{str(dil_num1)}|\n\n')


def print_dil_cards(dil_num1, dil_simb1, dil_num2, dil_simb2):
    print(f' ___   ___ \n|{str(dil_num2)}  | |{str(dil_num1)}  |\n| '
          f'{dil_simb2} | | {dil_simb1} |\n|__'
          f'{str(dil_num2)}| |__{str(dil_num1)}|')


def make_player_cards():
    pl_num1 = random.choice(numbers)
    pl_simb1 = random.choice(simbols)
    pl_num2 = random.choice(numbers)
    pl_simb2 = random.choice(simbols)
    return pl_num1, pl_simb1, pl_num2, pl_simb2


def print_player_cards(pl_num1, pl_simb1, pl_num2, pl_simb2):
    print(
        f' ___   ___ \n|{str(pl_num1)}  | |{str(pl_num2)}  |\n| '
        f'{pl_simb1} | | {pl_simb2} |\n|__'
        f'{str(pl_num1)}| |__{str(pl_num2)}|')


def make_player_third_card():
    player_num3 = random.choice(numbers)
    player_simb3 = random.choice(simbols)
    return player_num3, player_simb3


def print_player_three_cards(pl_num1, pl_simb1, pl_num2,
                             pl_simb2, pl_num3, pl_simb3):
    print(f' ___   ___   ___\n|{str(pl_num1)}'
          f'  | |{str(pl_num2)}  | |{str(pl_num3)}  |\n| {pl_simb1}'
          f' | | {pl_simb2} | | {pl_simb3} |\n|  {str(pl_num1)}'
          f'| |  {str(pl_num2)}| |  {str(pl_num3)}|')
