import random

# Card values: J, Q, K are 10; Ace can be 1 or 11
CARD_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10,
    "A": 11  # Start as 11
}

RANKS = list(CARD_VALUES.keys())
SUITS = ["♠", "♥", "♦", "♣"]


def get_random_card():
    """Return a random card as a string like 'A♠' or '10♥'."""
    rank = random.choice(RANKS)
    suit = random.choice(SUITS)
    return rank + suit


def calculate_hand_value(hand):
    """
    Calculate the total value of a hand.
    Aces start as 11, and are turned into 1 if the total is > 21.
    """
    total = 0
    aces = 0

    for card in hand:
        rank = card[:-1]  # everything except the last character (suit)
        value = CARD_VALUES[rank]
        total += value
        if rank == "A":
            aces += 1

    # If total is over 21 and we have aces, turn some Aces from 11 to 1
    while total > 21 and aces > 0:
        total -= 10  # 11 -> 1 (difference is 10)
        aces -= 1

    return total


def display_hand(owner, hand, hide_first_card=False):
    """Print the hand of the player or dealer."""
    if hide_first_card:
        # Show only second card for dealer (first card hidden)
        print(f"{owner}'s hand: [??] " + " ".join(hand[1:]))
    else:
        print(f"{owner}'s hand: " + " ".join(hand) + f"  (Total: {calculate_hand_value(hand)})")


def player_turn(deck_owner_name, hand):
    """
    Handle the player's turn.
    Returns the final hand after the player chooses to stand or busts.
    """
    while True:
        value = calculate_hand_value(hand)
        if value > 21:
            print(f"\n{deck_owner_name} busts with {value}!")
            break

        choice = input("\nDo you want to Hit or Stand? (h/s): ").lower().strip()
        while choice not in ["h", "s", "hit", "stand"]:
            choice = input("Please type 'h' or 's' (Hit / Stand): ").lower().strip()

        if choice in ["s", "stand"]:
            print(f"\n{deck_owner_name} stands with {value}.")
            break
        else:
            new_card = get_random_card()
            hand.append(new_card)
            print(f"{deck_owner_name} draws: {new_card}")
            display_hand(deck_owner_name, hand)

    return hand


def dealer_turn(hand):
    """
    Dealer auto-plays: hit until total >= 17.
    Returns final dealer hand.
    """
    print("\nDealer's turn...")
    display_hand("Dealer", hand, hide_first_card=False)

    while calculate_hand_value(hand) < 17:
        new_card = get_random_card()
        hand.append(new_card)
        print(f"Dealer draws: {new_card}")
        display_hand("Dealer", hand)

    return hand


def determine_winner(player_hand, dealer_hand):
    """
    Compare player and dealer hands and print the result.
    """
    player_total = calculate_hand_value(player_hand)
    dealer_total = calculate_hand_value(dealer_hand)

    print("\nFinal Results:")
    display_hand("Player", player_hand)
    display_hand("Dealer", dealer_hand)

    if player_total > 21:
        print("\n💥 Player busts. Dealer wins.")
    elif dealer_total > 21:
        print("\n💥 Dealer busts. Player wins!")
    elif player_total > dealer_total:
        print("\n🎉 Player wins!")
    elif player_total < dealer_total:
        print("\nDealer wins.")
    else:
        print("\nIt's a tie (push).")


def play_one_round():
    """Play one round of Blackjack."""
    print("\n=== New Round of Blackjack ===")

    # Initial hands
    player_hand = [get_random_card(), get_random_card()]
    dealer_hand = [get_random_card(), get_random_card()]

    # Show initial cards
    display_hand("Player", player_hand)
    # Dealer shows only one card
    display_hand("Dealer", dealer_hand, hide_first_card=True)

    # Player turn
    player_hand = player_turn("Player", player_hand)

    # If player busts, dealer wins directly
    if calculate_hand_value(player_hand) > 21:
        print("\nDealer wins this round.")
        return

    # Dealer turn
    dealer_hand = dealer_turn(dealer_hand)

    # Determine winner
    determine_winner(player_hand, dealer_hand)


def main():
    """Main loop to play multiple rounds."""
    print("Welcome to Blackjack!")

    while True:
        play_one_round()

        again = input("\nDo you want to play another round? (yes/no): ").lower().strip()
        if again != "yes":
            print("Thanks for playing Blackjack. Goodbye!")
            break


if __name__ == "__main__":
    main()