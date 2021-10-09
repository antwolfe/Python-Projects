import random
from art import logo

def play_again():
    play_again = input("Do you want to play a game of Blackjack? 'y' or 'n'?: ")
    if play_again == 'y':
        blackjack()



def blackjack():

    print(logo)

    def deal_card():
        '''Returns random card from deck'''
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)

    user_cards = []
    computer_cards = []

    user_score = []
    computer_score = []

    game_over = False


    def card_to_player(players_cards):
        '''Gives 2 cards to players'''
        for _ in range(2):
            players_cards.append(deal_card())
        return players_cards


    def calculate_scores(list_of_cards):
        '''Take card list and return score calculated from list'''

        calc_score = sum(list_of_cards)

        if 11 in list_of_cards and calc_score > 21:
            list_of_cards.remove(11)
            list_of_cards.append(1)
            if_11 = calculate_scores(list_of_cards)
            return if_11

        else:
            return calc_score


    card_to_player(user_cards)
    card_to_player(computer_cards)

    user_total = calculate_scores(user_cards)
    computer_total = calculate_scores(computer_cards)


    ###CARD OUTPUT BELOW###
    print(f"Your cards are: {user_cards}, and your score is {user_total}")
    # print(f"The computer's cards are: {computer_cards}")
    print(f"Dealer's card: {computer_cards[0]}")
    ######


    while not game_over:
        if input("Do you want another card? Type 'y' or 'n': ") == 'y' \
            and len(user_cards) < 6:
            new_card = deal_card()
            user_cards.append(new_card)
            user_total = calculate_scores(user_cards)
            print(f"Your cards are now: {user_cards} and your score is {user_total}")

        else:
            break

        # compare()

        # computer_total = computer_score
        # user_total = user_score

        while computer_total < 17:
            computer_cards.append(deal_card())
            computer_total = calculate_scores(computer_cards)


        if user_total == 21:
            game_over = True
            print("Blackjack! You Win")

        elif user_total >= 22:
            print("You're over! You lose")
            game_over = True

        elif computer_total == 21:
            print("Computer Blackjack. You lose.")
            game_over = True

        elif computer_total >= 22:
            print("Computer went over! You win")
            game_over = True

    if user_total <= 21 and user_total > computer_total:
        print("You had the higher number. You Win")
        game_over = True

    elif computer_total <= 21 and computer_total > user_total:
        print("Computer had higher number. You Lose")
        game_over = True

    elif computer_total == user_total:
        print("Draw")
        game_over = True
    else:
        game_over = True


    def showCards():
        '''This shows the final cards and score of the game or can be used for debug testing'''
        print(f"Your cards: {user_cards}, and total: {user_total}")
        print(f"Computer's Cards: {computer_cards}, and score: {computer_total}")

    showCards() #showing the final score
    play_again()



play_again()