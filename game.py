import random

cards = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def check_val(ans, card_1, card_2):
    # card_1 is the new card, card_2 is the old card
    if cards.index(card_1) < cards.index(card_2):
        if ans == 'h':
            return False
        return True
    else:
        if ans == 'h':
            return True
        return False


def play(points, old_card=None):
    if not old_card:
        old_card = random.choice(cards)
    print('Card selected is ' + old_card)

    while True:
        h_l = input('Higher or lower?\tH / L\n').strip().lower()
        if h_l not in ['h', 'l']:
            print('\nInvalid input!, Enter H or L')
        else:
            break

    while True:
        new_card = random.choice(cards)
        if new_card != old_card:
            break

    if check_val(h_l, new_card, old_card):
        print('Congratulations! You win!')
        points += 1
    else:
        print('You lose!')
        points = 0

    print('Card was ' + new_card)
    print('Score: ' + str(points) + '\n')

    while True:
        again = input('Play again? Y / N\n').strip().lower()
        if again not in ['y', 'n']:
            print('\nInvalid input!, Enter Y or N')
        else:
            break
    if again == 'y':
        play(points, new_card)
    else:
        return


play(0)


