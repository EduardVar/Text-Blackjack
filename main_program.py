from Scripts import hand
from Scripts import chips
from Scripts import deck

def hit(current_deck, current_hand):
    current_hand.add_card(current_deck.deal())
    current_hand.adjust_for_ace()

def hit_or_stand(current_deck, current_hand):
    global playing  # to control an upcoming while loop
    
    while True:
        print("Your current hand value is {}".format(current_hand.value))
        answer = input("Enter 'H' for hit or 'S' for stand ")

        if answer.lower() == "h":
            hit(current_deck, current_hand)
        elif answer.lower() == "s":
            print("You stand... Dealer's turn!")
            playing = False
        else:
            print("Sorry, try again...")
            continue
        break

def show_some(player, dealer):
    
    print("\n\n===============\nPlayer Hand:")

    for item in player.cards:
        print(item)

    print("\nDealers Hand:")
    print(dealer.cards[0])

    for i in range(1, len(dealer.cards)):
        print("UNKNOWN")

    print()

def show_all(player, dealer):
    
    print("\n\n===============\nPlayer Hand:")

    for item in player.cards:
        print(item)

    print("\nDealers Hand:")

    for item in dealer.cards:
        print(item)

    print("\nPlayer Value: {}\nDealer Value: {}".format(player.value, dealer.value))
    print()

def player_busts():
    print("\n---------------\nPlayer busted\n---------------")
    player_chips.lose_bet()

def player_wins():
    print("\n---------------\nThe player won!\n---------------")
    player_chips.win_bet()

def dealer_busts():
    print("\n---------------\nThe dealer busted!\n---------------")
    player_chips.win_bet()

def dealer_wins():
    print("\n---------------\nThe Dealer won!\n---------------")
    player_chips.lose_bet()
    
def push():
    print("It's a push! No one wins.")

#Global Attributes
playing = True
player_chips = chips.Chips()

#Main Game
while True:
    print("====================\nWelcome to BlackJack\n====================")
    
    # Create & shuffle the deck, deal two cards to each player
    current_deck = deck.Deck()
    current_deck.shuffle()

    player_hand = hand.Hand()
    dealer_hand = hand.Hand()

    player_hand.add_card(current_deck.deal())
    player_hand.add_card(current_deck.deal())
    dealer_hand.add_card(current_deck.deal())
    dealer_hand.add_card(current_deck.deal())
           
    # Set up the Player's chips

    
    # Prompt the Player for their bet
    player_chips.take_bet()
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(current_deck, player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            show_all(player_hand, dealer_hand)
            player_busts()
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    while player_hand.value <= 21:
    
        # Show all cards

        #Have dealer hit if under 17
        if dealer_hand.value < 17:
            show_all(player_hand, dealer_hand)
            print("\nDealer Hits!")
            hit(current_deck, dealer_hand)
        else:
            print("\nDealer Stays")

            if player_hand.value == dealer_hand.value:
                show_all(player_hand, dealer_hand)
                push()
                break
            elif player_hand.value > dealer_hand.value:
                show_all(player_hand, dealer_hand)
                player_wins()
                break
            elif player_hand.value < dealer_hand.value:
                show_all(player_hand, dealer_hand)
                dealer_wins()
                break 
    
        # Run different winning scenarios
        if dealer_hand.value > 21:
            show_all(player_hand, dealer_hand)
            dealer_busts()
            break
    
    # Inform Player of their chips total 
    print(f"Your current chip total is {player_chips.total}")

    if player_chips.total == 0:
        print("\n\nCongratulations! You ran out of money! What a loser :)")
        break
    
    # Ask to play again
    answer = input("Play again? Y/N ")

    if answer.lower() == "n":
        break
    elif answer.lower() == "y":
        print("\n" * 60)
        playing = True
